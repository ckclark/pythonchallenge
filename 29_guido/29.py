bzdata = []
for line in open('guido.html').readlines()[12:]:
    bzdata.append(chr(len(line) - 1))
print ''.join(bzdata).decode('bz2')
