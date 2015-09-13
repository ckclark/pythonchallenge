import zlib
data = open('package.pack').read()

steps = []

while True:
    if data.startswith('\x78\x9c'):
        data = zlib.decompress(data)
        steps.append('z')
    elif data.startswith('BZh'):
        data = data.decode('bz2')
        steps.append('b')
    elif data.endswith('\x9c\x78'):
        data = data[::-1]
        steps.append('\n')
    else:
        open('result.bin', 'w').write(data)
        break
print ''.join(steps)
