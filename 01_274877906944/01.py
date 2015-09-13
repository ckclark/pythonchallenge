from string import maketrans, lowercase
fr = lowercase
to = lowercase[2:] + lowercase[:2]
tab = maketrans(fr, to)
problem = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
print problem.translate(tab)
print 'map'.translate(tab) + '.html'
