fp = open('left')
fpdiff = open('out2')
fpout = open('common.png', 'w')

def main():
    ignore_lines = set()
    for line in fpdiff:
        ignore_lines.add(int(line.strip()))

    count = 1
    for line in fp:
        if count not in ignore_lines:
            for c in filter(None, line.split()):
                fpout.write(chr(int(c, 16)))
        count += 1



if __name__ == '__main__':
    main()
