from PIL import Image
def main():
    im = Image.open('cave.jpg')
    imOdd = Image.new('RGB', im.size)
    imEven = Image.new('RGB', im.size)

    pix = im.load()
    pixOdd = imOdd.load()
    pixEven = imEven.load()

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            if (i + j) % 2 == 0:
                pixEven[i, j] = pix[i, j]
                pixOdd[i, j] = (0, 0, 0)
            else:
                pixOdd[i, j] = pix[i, j]
                pixEven[i, j] = (0, 0, 0)
    imOdd.save('odd.png')
    imEven.save('even.png')

if __name__ == '__main__':
    main()
