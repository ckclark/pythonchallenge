from zipfile import ZipFile
import re

def main():
    pattern = re.compile(r'\d{2,}')
    zf = ZipFile('channel.zip')
    fp = zf.open('readme.txt')
    chain = open('chain.txt', 'w')
    text = fp.read()
    number = pattern.search(text).group(0)
    while True:
        finfo = zf.getinfo(number + '.txt')
        print finfo.comment
        print number
        text = zf.open(finfo).read()
        chain.write(finfo.comment)
        number = pattern.search(text).group(0)

if __name__ == '__main__':
    main()
