# Result: accepted

n_queries = int(input())
res = []

for k in range(n_queries):
    l, r = list(map(int, input().split()))
    if l == 1:
        res.append((1, r))
    else:
        flag = True
        while flag:
            if 2 * l <= r:
                res.append((l, 2*l))
                flag = False
            else:
                l += 1

for r in res:
    print('{} {}'.format(r[0], r[1]))