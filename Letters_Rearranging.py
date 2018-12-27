
def is_palindrome(w):
    if len(w) % 2 == 0:
        for i in range(len(w)//2):
            if w[i] != w[len(w)-i-1]:
                return False
    else:
        for i in range(len(w)//2):
            if w[i] != w[len(w)-i-1]:
                return False
    return True


def easy_ransform(w):
    ls_w = list(w)
    idx = next(i for i in range(len(w)) if w[i] != w[0])
    ls_w[idx], ls_w[-1] = ls_w[-1], ls_w[idx]
    return ''.join(ls_w)


n_queries = int(input())

res = []

for i in range(n_queries):
    word = input()
    if len(set(word)) == 1:
        res.append(-1)
    elif not is_palindrome(word):
        res.append(word)
    else:
        res.append(easy_ransform(word))

for i in res:
    print(i)


