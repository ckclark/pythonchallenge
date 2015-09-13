def main():
    data = open('evil2.gfx').read()
    for i in range(5):
        open('%d.jpg' % i, 'w').write(data[i::5])

if __name__ == '__main__':
    main()
