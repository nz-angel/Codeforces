# Result: Time Limit Exceeded

s = input()

a = list(s)
pairs = 0

v = True
while v:
    for idx, x in enumerate(a):
        if idx == len(a) - 1:
            continue
        elif x == a[idx+1]:
            c = 1
            i = idx+1
            while x == a[i]:
                c += 1
                if i == len(a) - 1:
                    break
                i += 1
            pairs += c // 2
            for j in range(c):
                del a[idx]
            break
    else:
        v = False

begin = 0


if pairs % 2:
    print('Yes')
else:
    print('No')