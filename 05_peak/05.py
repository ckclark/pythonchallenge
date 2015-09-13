import cPickle
obj = cPickle.load(open('banner.p'))
for row_elem in obj:
    print ''.join(map(lambda x:x[0] * x[1], row_elem))
