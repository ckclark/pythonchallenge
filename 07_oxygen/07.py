from PIL import Image
import re
def main():
    im = Image.open('oxygen.png')
    hoffset = 47
    woffset = 5
    w = 7
    pix = im.load()
    x = woffset
    y = hoffset
    ans = []
    while True:
        if x >= im.size[0]:
            break
        if pix[x, y][0] == pix[x, y][1] == pix[x, y][2]:
            ans.append(chr(pix[x, y][0]))
            x += w
        else:
            break
    print ''.join(map(chr, map(int, re.findall(r'\d+', ''.join(ans)))))

if __name__ == '__main__':
    main()
