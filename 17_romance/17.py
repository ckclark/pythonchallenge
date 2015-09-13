import sys
import re
from urllib import unquote_plus, quote_plus
import xmlrpclib
from lxml import etree
sys.path.append('..')
from fetch_web import fetch_web

def get_cookie():
    parser = etree.HTMLParser()
    web_src = fetch_web('http://www.pythonchallenge.com/pc/def/linkedlist.php')
    #open('first.html', 'w').write(web_src)
    root = etree.fromstring(web_src, parser)
    a = root.xpath('//a')[0]
    link = a.attrib['href']
    firstpat = re.compile(r'\d+')
    fout = open('chain.txt', 'w')
    fcookie = open('cookie.txt', 'w')
    number = firstpat.search(link).group(0)
    fout.write(number + '\n')
    pat = re.compile(r'busynothing is (\d+)')
    cookiepat = re.compile(r'info=(.+?);')
    while True:
        web_src, header = fetch_web('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=' + number, need_header=True)
        #open('page%d.html' % count, 'w').write(web_src)
        info = cookiepat.search(header.getheader('Set-Cookie')).group(1)
        fcookie.write(info + '\n')
        number = pat.search(web_src).group(1)
        fout.write(number + '\n')
        print number, info

def get_message():
    #get_cookie()
    data = ''.join(open('cookie.txt').read().split('\n'))
    print unquote_plus(data).decode('bz2')
    # is it the 26th already? call his father and inform him that "the flowers are on their way". he'll understand.

def phone_leopold():
    url = 'http://www.pythonchallenge.com/pc/phonebook.php'
    phonebook = xmlrpclib.Server(url)
    print phonebook.phone('Leopold')

def send_message_to_leopold():
    message = quote_plus('the flowers are on their way')
    result = fetch_web('http://www.pythonchallenge.com/pc/stuff/violin.php', Cookie="info=" + message + ";")
    open('result.html', 'w').write(result)

def main():
    #get_message()
    #phone_leopold()
    send_message_to_leopold()

if __name__ == '__main__':
    main()

