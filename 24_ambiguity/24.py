from PIL import Image
from Queue import Queue
def main():
    im = Image.open('maze.png')
    pix = im.load()
    w, h = im.size
    start = (1, h - 1)
    end = (w - 2, 0)
    white = (255, 255, 255, 255)
    dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))

    q = Queue()
    q.put(start)
    pix[start] = pix[start][:3] + (0,)
    while not q.empty():
        cur = q.get()
        if cur == end:
            break

        for i, d in enumerate(dirs):
            nx, ny = cur[0] + d[0], cur[1] + d[1]
            if 0 <= nx < w and 0 <= ny < h and pix[nx, ny] != white and pix[nx, ny][3] == 255:
                pix[nx, ny] = pix[nx, ny][:3] + (i ^ 0x1,)
                q.put((nx, ny))

    cur = end
    ans = []
    while cur != start:
        c = pix[cur]
        ans.append(pix[cur][0])
        cur = (cur[0] + dirs[c[3]][0], cur[1] + dirs[c[3]][1])
    ans.append(pix[cur][0])
    open('result.zip', 'w').write(''.join(map(chr, ans[1::2])))


if __name__ == '__main__':
    main()
