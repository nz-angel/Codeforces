# Result: Accepted
# url: https://codeforces.com/contest/1234/problem/A

queries = int(input())
for q in range(queries):
    n_objects = int(input())
    prices = list(map(int, input().split()))
    big_money = sum(prices)
    if big_money//n_objects*n_objects >= big_money:
        print(big_money//n_objects)
    else:
        print(big_money//n_objects+1)
