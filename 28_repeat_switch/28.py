from PIL import Image
def main():
    im = Image.open('bell.png')
    pix = im.load()
    greens = []
    for y in range(im.size[1]):
        for x in range(im.size[0] / 2):
            greens.append((pix[x * 2, y][1], pix[x * 2 + 1, y][1]))

    excep = filter(lambda x:abs(x[0] - x[1]) != 42, greens)
    print ''.join(map(chr, map(lambda x:abs(x[0] - x[1]), excep)))

if __name__ == '__main__':
    main()
