# Result: Accepted
# url: https://codeforces.com/contest/1108/problem/A

n_queries = int(input())

for k in range(n_queries):
    a, b, c, d = list(map(int, input().split()))
    if a != c:
        print(a, c)
    else:
        print(a, d)