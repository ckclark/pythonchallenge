def main():
    a = ['1']
    for i in range(30):
        value = a[-1]
        prev = None
        count = 0
        ans = []
        for c in value:
            if prev == c:
                count += 1
            else:
                if prev is not None:
                    ans.append('%d%s' % (count, prev))
                prev = c
                count = 1

        if prev is not None:
            ans.append('%d%s' % (count, prev))
        a.append(''.join(ans))
    print len(a[30])

if __name__ == '__main__':
    main()
