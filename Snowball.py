# Result: accepted

w, h = list(map(int, input().split()))
u1, d1 = list(map(int, input().split()))
u2, d2 = list(map(int, input().split()))

while h != 0:
    w += h
    if h == d1:
        w = max(w-u1, 0)
    elif h == d2:
        w = max(w-u2, 0)
    h -= 1
print(w)
