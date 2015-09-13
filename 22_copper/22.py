from PIL import Image, ImageSequence, ImageDraw

def main():
    im = Image.open('white.gif')
    iterIm = ImageSequence.Iterator(im)

    chars = []
    dirs = []
    prevx, prevy = 100, 100
    for frame in iterIm:
        data = list(frame.getdata())
        y, x = divmod(data.index(8), 200)
        x, y = x - 100, y - 100
        dirs.extend((prevx, prevy))
        if x == y == 0:
            chars.append(dirs)
            prevx, prevy = 100, 100
            dirs = []
        else:
            prevx, prevy = prevx + x, prevy + y
    chars.append(dirs)
    count = 0
    for char in chars:
        print char
        imOut = Image.new('RGB', im.size)
        draw = ImageDraw.Draw(imOut)
        draw.line(char)
        imOut.save('%d.png' % count)
        count += 1

if __name__ == '__main__':
    main()
