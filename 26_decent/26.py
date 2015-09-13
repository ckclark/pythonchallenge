from hashlib import md5
from cStringIO import StringIO

def main():
    data = StringIO()
    data.write(open('mybroken.zip').read())
    for offset in range(len(data.getvalue())):
        data.seek(offset)
        oldchar = data.read(1)
        for c in range(256):
            data.seek(offset)
            data.write(chr(c))
            fixdata = data.getvalue()
            if md5(fixdata).hexdigest() == 'bbb8b499a0eef99b52c7f13f4e78c24b':
                print 'offset:', offset, ', byte:', c
                open('fixed.zip', 'w').write(fixdata)
                return

        data.seek(offset)
        data.write(oldchar)


if __name__ == '__main__':
    main()

# offset: 1234 , byte: 168
