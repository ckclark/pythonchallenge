import urllib2

#COOKIE = 'Force=TG9vaywgYSBwYXNzd29yZCFVM0JsYkd4R2IzSmpaUT09; POSTNUKESID=eed81538658fbe878eb548ca919682a7; phpbb2mysql_data=a%3A1%3A%7Bs%3A6%3A%22userid%22%3Bs%3A6%3A%22170514%22%3B%7D; phpbb2mysql_sid=56389b48e7a5e270194be2aafc26af30; ChallUID=170514; ChallUNAME=ckclark'
#REFERER = 'http://www.hackquest.com'
#USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'
#HOST = 'hackquest.com'

def fetch_web(path, body=None, need_header=False, **kwargs):
    req = urllib2.Request(path, body)
    if body:
        req.add_header('Content-type', 'application/x-www-form-urlencoded')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')
    req.add_header('Accept-Language', 'en-US,en;q=0.8')
    req.add_header('Cache-Control', 'max-age=0')
    req.add_header('Connection', 'keep-alive')
    for key, value in kwargs.iteritems():
        req.add_header(key, value)
    #req.add_header('Cookie', COOKIE)
    #req.add_header('Host', HOST)
    #req.add_header('Referer', REFERER)
    #req.add_header('User-Agent', USER_AGENT)

    fp = urllib2.urlopen(req)
    result = fp.read()
    if need_header:
        return result, fp.info()
    else:
        return result

def main():
    pass

if __name__ == '__main__':
    main()
