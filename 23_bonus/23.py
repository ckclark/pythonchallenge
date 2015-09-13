import this
import re
from string import maketrans, lowercase
article = ''.join([this.d.get(c, c) for c in this.s])
question = 'va gur snpr bs jung?'
tab = maketrans(lowercase, lowercase[13:] + lowercase[:13])
substr = re.match(r'(.*) what', question.translate(tab)).group(1)
print re.search(substr + r' (\w+)', article, re.I).group(1)
