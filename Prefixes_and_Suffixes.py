
def solve(l, w, w1, w2):
    wrd = w1 + w2[-1]
    pre = [0]*l
    suf = [0]*l
    res = [0]*(2*l-2)
    for i, s in enumerate(w):
        if wrd.startswith(s) and pre[len(s)] == 0:
            pre[len(s)] = 1
            res[i] = 'P'
        elif wrd.endswith(s) and suf[len(s)] == 0:
            suf[len(s)] = 1
            res[i] = 'S'
    if 0 in res:
        return False, res
    return True, res

length = int(input())
words = []
for k in range(2*length-2):
    words.append(input())

lng1, lng2 = [l for l in words if len(l) == length-1]
done, result = solve(length, words, lng1, lng2)
if not done:
    done, result = solve(length, words, lng2, lng1)
print(''.join(result))


