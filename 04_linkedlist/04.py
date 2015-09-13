import sys
import re
sys.path.append('..')
from fetch_web import fetch_web
#from lxml import etree


def main():
    #parser = etree.HTMLParser()
    #web_src = fetch_web('http://www.pythonchallenge.com/pc/def/linkedlist.php')
    ##open('first.html', 'w').write(web_src)
    #root = etree.fromstring(web_src, parser)
    #a = root.xpath('//a')[0]
    #link = a.attrib['href']
    pat = re.compile(r'\d+')
    fout = open('chain.txt', 'a')
    number = '63579' #pat.search(link).group(0)
    fout.write(number + '\n')
    count = 0
    while True:
        web_src = fetch_web('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + number)
        #open('page%d.html' % count, 'w').write(web_src)
        count += 1
        number = pat.search(web_src).group(0)
        fout.write(number + '\n')
        print number


if __name__ == '__main__':
    main()

# peak.html
