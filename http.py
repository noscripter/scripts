#!/usr/bin/env python
# HTTP Client with cookie handling
# should be handy for bots...
#
# Programmed by WangLu
# Last changed: 2011.05.16

import cookielib
import time
import urllib
import urllib2

############# configuration

HTTP_PROXY = urllib2.ProxyHandler()
HTTP_HEADERS = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:2.0) Gecko/20100101 Firefox/4.0' }

HTTP_RETRY_COUNT = -1 # how many time do we need to retry when failed, negative for always retry
HTTP_RETRY_INTERVAL = 5 # seconds

# Handle cookie, and auto-retry while meet error 
class HTTPHandler():

    def __init__ (self, proxy=HTTP_PROXY):
        self.cookie = cookielib.CookieJar() 
        self.http = urllib2.build_opener(proxy, urllib2.HTTPCookieProcessor(self.cookie))
        self.last_request = None
        self.last_response = None

    # auto retry when meet error
    def get_url (self, url, data=None, headers=None, retry_count = None):
        if retry_count is None:
            retry_count = HTTP_RETRY_COUNT
        count = 0
        if (data is not None) and (type(data) is not str):
            data = urllib.urlencode(data)
        if headers is None:
            headers = {}
        else:
            headers = dict(headers)
        headers.update(HTTP_HEADERS)
        while (retry_count < 0) or (count < retry_count):
            count += 1
            try:
                self.last_request = urllib2.Request(url, data, headers)
                self.last_response = self.http.open(self.last_request)
                content = self.last_response.read()
                return content
            except: 
                print 'HTTPHandler: error while fetching:', url
                pass
            time.sleep(HTTP_RETRY_INTERVAL)
#        print 'HTTPHandler: max retries reached'
        return None

if __name__ == '__main__':
    print HTTPHandler().get_url('http://www.google.com')
