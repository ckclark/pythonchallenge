import urllib2
import re
import sys

def main():
    auth = urllib2.HTTPBasicAuthHandler()
    auth.add_password('pluses and minuses', 'www.pythonchallenge.com', 'butter', 'fly')
    urllib2.install_opener(urllib2.build_opener(auth))
    url = 'http://www.pythonchallenge.com/pc/hex/unreal.jpg'
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)

    req.headers['Range'] = 'bytes=30203-'
    resp = urllib2.urlopen(req)
    #print resp.headers['Content-Range']
    print resp.read()

    req.headers['Range'] = 'bytes=30237-'
    resp = urllib2.urlopen(req)
    #print resp.headers['Content-Range']
    print resp.read()

    req.headers['Range'] = 'bytes=30284-'
    resp = urllib2.urlopen(req)
    #print resp.headers['Content-Range']
    print resp.read()

    req.headers['Range'] = 'bytes=30295-'
    resp = urllib2.urlopen(req)
    #print resp.headers['Content-Range']
    print resp.read()

    req.headers['Range'] = 'bytes=30313-'
    resp = urllib2.urlopen(req)
    #print resp.headers['Content-Range']
    print resp.read()

    req.headers['Range'] = 'bytes=2123456789-'
    resp = urllib2.urlopen(req)
    #print resp.headers['Content-Range']
    print resp.read()[::-1]

    req.headers['Range'] = 'bytes=2123456743-'
    resp = urllib2.urlopen(req)
    #print resp.headers['Content-Range']
    print resp.read()

    req.headers['Range'] = 'bytes=1152983631-'
    resp = urllib2.urlopen(req)
    print resp.headers['Content-Range']
    open('out.zip', 'w').write(resp.read())

if __name__ == '__main__':
    main()
