import csv
import string
from PIL import Image
csvReader = csv.reader(open('yankeedoodle.csv'))
data = []
for line in csvReader:
    data.extend(filter(None, map(string.strip, line)))

im = Image.new('L', (53, 139))
im.putdata(map(lambda x: int(x * 256), map(float, data)))
im = im.transpose(Image.FLIP_LEFT_RIGHT)
im = im.transpose(Image.ROTATE_90)
im.save('out.png')

ans = []
for i in range(len(data) / 3):
    ans.append(chr(int(data[i * 3][5] + data[i * 3 + 1][5] + data[i * 3 + 2][6])))

print ''.join(ans)

