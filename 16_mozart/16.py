from PIL import Image

def main():
    im = Image.open('mozart.gif').convert('RGB')
    imOut = Image.new('RGB', im.size)
    pixOut = imOut.load()

    pix = im.load()
    for y in range(im.size[1]):
        first = None
        for x in range(im.size[0]):
            if pix[x, y] == (255, 0, 255):
                first = x
                break
        if first is None:
            print 'Not found at row', y
        else:
            for x in range(im.size[0]):
                pixOut[x, y] = pix[(x + first) % im.size[0], y]
    imOut.save('out.png')


if __name__ == '__main__':
    main()
