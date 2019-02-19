# Result: Accepted
# url: https://codeforces.com/contest/1118/problem/A

n_queries = int(input())

for q in range(n_queries):
    n, a, b = list(map(int, input().split()))
    if b >= 2*a:
        print(n*a)
    else:
        if n % 2:
            print((n//2)*b + a)
        else:
            print((n//2)*b)