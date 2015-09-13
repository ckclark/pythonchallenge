from PIL import Image
from keyword import kwlist

def main():
    im = Image.open('zigzag.gif')
    imOut = Image.new('RGB', im.size)
    pix = im.load()
    pixOut = imOut.load()
    palette = im.getpalette()[::3]
    prev = None
    bzdata = []
    for y in range(im.size[1]):
        for x in range(im.size[0]):
            c = pix[x, y]
            if prev is not None and palette[prev] != c:
                bzdata.append(chr(c))
                pixOut[x, y] = (255, 0, 0)
            prev = c
    imOut.save('out.gif')
    data = ''.join(bzdata).decode('bz2')
    print set(data.split()) - set(kwlist)

if __name__ == '__main__':
    main()
