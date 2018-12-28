# Incompleto: Time Limit exceeded

def is_completed(w):
    if len(set(w)) == 1:
        return True
    return False


def can_add_brick(w, max_h):
    # if (w[0] != w[1] and w[1] != w[2]) or (w[-1] != w[-2] and w[-2] != w[-3]):
    #     return -1, False
    # else:
    for i in range(len(w)-1):
        if w[i+1] == w[i] and w[i] != max_h:
            return i, True
    return -1, False


def candidates(w, max_h):
    cand = []
    for i in range(len(w)-1):
        if w[i+1] == w[i] and w[i] != max_h:
            cand.append((i, i+1))
    return cand


def add_brick(w, duo, max_h, cand):
    w[duo[0]] += 1
    w[duo[1]] += 1
    if w[duo[0]] == max_h:
        cand.remove(duo)
    else:
        if duo[0] != 0 and w[duo[0]] == w[duo[0]-1]:
            cand.append((duo[0]-1, duo[0]))
        if duo[1] != (len(w)-1) and w[duo[1]] == w[duo[1]+1]:
            cand.append((duo[1], duo[1]+1))


length = int(input())
wall = list(map(int, input().split()))
max_height = max(wall)
pairs = candidates(wall, max_height)

res = 'YES'

while pairs:
    add_brick(wall, pairs[0], max_height, pairs)
    if not is_completed(wall) and not pairs:
        res = 'NO'
    # brick, pos = can_add_brick(wall, max_height)
    # if pos:
    #     wall[brick] += 1
    #     wall[brick+1] += 1
    # else:
    #     res = 'NO'
    #     break

print(res)


