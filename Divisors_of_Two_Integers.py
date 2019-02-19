# Result: Accepted
# url: https://codeforces.com/contest/1108/problem/B

length = int(input())
seq = list(map(int, input().split()))

seq.sort()
x = seq[-1]
count = {val: 0 for val in seq}
new_seq = []
for k in seq:
    if x % k:
        new_seq.append(k)
    elif not x % k and count[k]:
        new_seq.append(k)
    else:
        count[k] += 1

y = new_seq[-1]
print(x, y)
