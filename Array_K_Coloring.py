# Result: Wrong


def m_mod(x, y):
    z = x % y
    if not z:
        return y
    else:
        return z


n, k = list(map(int, input().split()))
seq = list(map(int, input().split()))

ocurrences = {num: 0 for num in seq}
indices = {num: set([]) for num in seq}
for idx, num in enumerate(seq):
    ocurrences[num] += 1
    indices[num].add(idx)

if max(ocurrences.values()) > k:
    print('NO')
elif k > n:
    print('NO')
elif k == n:
    print('YES')
    print(list(range(1, k+1)))
else:
    colour_choice = [0]*n
    last_colour = {num: 0 for num in ocurrences.keys()}
    last_used = 0
    for idx, nro in enumerate(seq):
        new = m_mod(last_used+1, k)
        if last_colour[nro] == new:
            new = m_mod(last_colour[nro]+1, k)
        last_colour[nro] = new
        colour_choice[idx] = new
        last_used = m_mod(last_used+1, k)
    print('YES')
    print(' '.join(map(str,colour_choice)))



