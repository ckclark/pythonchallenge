import re
print ''.join(re.findall(r'(?:^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3}(?:[^A-Z]|$)', open('3.txt').read()))
