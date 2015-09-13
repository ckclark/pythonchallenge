from PIL import Image
def main():
    im = Image.open('beer2.png')
    while True:
        data = im.getdata()
        max_used_color = max(data)
        filtered_data = filter(lambda x: x < max_used_color - 1, im.getdata())
        if not filtered_data:
            break
        size = len(filtered_data)
        #brightest = max(filtered_data)
        #shift = 255. / brightest
        #filtered_data = map(lambda x:int(x * shift), filtered_data)
        side = int((size + 1)** .5)
        if side * side != size:
            break
        im = Image.new('L', (side, side))
        im.putdata(filtered_data)
        im.save('%d.png' % len(filtered_data))


if __name__ == '__main__':
    main()
