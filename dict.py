#!/usr/bin/env python

"""
Get a word from command line or GUI dialog
And show the translation (by youdao) through notification

register an youdao API, and write them into JSON in a file name 'dict.conf' located in the same dir of this script

the content should be
["keyfrom", "key"]

by WangLu
2013.04.08
"""

import os.path
import subprocess
import sys
import pynotify
import requests
import json

script_path = os.path.dirname(os.path.realpath(__file__))
keyfrom, key = json.load(open(os.path.join(script_path, 'dict.conf')))
BASEURL='http://fanyi.youdao.com/openapi.do?'
params = {
        'keyfrom' : keyfrom,
        'key' : key,
        'type' : 'data',
        'doctype' : 'json',
        'version' : '1.1'
        }

def query_youdao(query):
    global params
    params['q'] = query
    result = ''
    try:
        obj = requests.get(BASEURL, params=params).json
        if obj['errorCode'] == 0:
            title = obj['query'].encode('utf-8')
            result = '\n'.join([i.encode('utf-8') for i in obj['translation']])
            try:
                result += '\n' + 'PHONETIC: ' + obj['basic']['phonetic'].encode('utf-8')
            except:
                pass
            try:
                result += ''.join(['\n'+i.encode('utf-8') for i in obj['basic']['explains']])
            except:
                pass
            try:
                web_translation =  ''.join(['\n'+i['key'].encode('utf-8')+' -> '+','.join('  '+j.encode('utf-8') for j in i['value'][:1]) for i in obj['web'][:3]])
                if web_translation != '':
                    result += '\n' + 'WEB:' + web_translation
            except:
                pass
    except:
        pass
    return (result == '', result)

if __name__ == '__main__':
    if not pynotify.init('youdao'):
        print 'Error'
        sys.exit(-1)

    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        query = subprocess.Popen(['zenity', '--entry', '--text=', '--entry-text=', '--title=Dictionary'], stdout=subprocess.PIPE).stdout.read()

    title = query
    ok, result = query_youdao(query)
    if not ok:
        pass

    n = pynotify.Notification(title, result, '')
    n.set_urgency(pynotify.URGENCY_CRITICAL)
    n.set_timeout(200)
    n.show()

