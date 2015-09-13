from PIL import Image
def main():
    im = Image.open('wire.png')
    imOut = Image.new('RGB', (100, 100))
    pixOut = imOut.load()
    data = im.getdata()
    w, h = 100, 100
    x, y = 0, 0
    v = (1, 0)
    for c in data:
        pixOut[x, y] = c
        if x >= y and x + y == w - 1:
            v = (0, 1)
        elif x + y >= w and x == y:
            v = (-1, 0)
        elif x < y and x + y == w - 1:
            v = (0, -1)
        elif x + y < w and x + 1== y:
            v = (1, 0)
        x, y = x + v[0], y + v[1]
    imOut.save('out.png')

if __name__ == '__main__':
    main()
