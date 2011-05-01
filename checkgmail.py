#!/usr/bin/env python
"""
Gmail Notifier

by Wang Lu
2011.05.01
"""

import pynotify
import feedparser
import subprocess
import time

FEEDURL = 'https://mail.google.com/gmail/feed/atom'
#FEEDURL = 'https://mail.google.com/mail/feed/atom/unread'
USERNAME = "coolwanglu"
PASSWORD = subprocess.Popen(['gkeyring','-1', '-p','user=%s,server=mail.google.com'%(USERNAME,)], stdout=subprocess.PIPE).stdout.read()
INTERVAL=60

def getfeed():
    return subprocess.Popen(['wget', FEEDURL, '--quiet', '--user=%s'%(USERNAME,), '--password=%s'%(PASSWORD,), '-O-'], stdout=subprocess.PIPE).stdout.read()


def getUnreadMsgCount(feed):
    atom = feedparser.parse(feed)
    newmails = len(atom.entries)
    return newmails

if __name__ == "__main__":
    pynotify.init('WL Gmail Notifier')
    noti = pynotify.Notification('no new email')
    count = 0
    while True:
        feed = getfeed()
        count = getUnreadMsgCount(feed)
        if count > 0:
    #        subprocess.call(['notify-send', '--icon=indicator-messages-new', '--urgency=critical','%d new email(s)!' % (count,)])
            noti.set_property('summary', '%d new email(s)!' % (count,))
            noti.set_property('icon-name', 'indicator-messages-new')
            noti.set_urgency(pynotify.URGENCY_CRITICAL)
            noti.show()
        else:
            noti.close()
        time.sleep(INTERVAL)


