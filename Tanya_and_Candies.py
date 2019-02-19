# Result: Time Limit Exceeded
# url: https://codeforces.com/contest/1118/problem/B


def is_good(ls):
    even = 0
    odd = 0
    for i in range(len(ls)):
        if i % 2 == 0:
            even += ls[i]
        else:
            odd += ls[i]
    return even == odd


n_candies = int(input())
weights = list(map(int, input().split()))

# good = set([])
# bad = set([])
good_candies = 0
# for i in range(n_candies):
#     B = tuple(weights[:i] + weights[i+1:])
#     if B in good:
#         good_candies += 1
#     elif B in bad:
#         continue
#     elif is_good(B):
#         good.add(B)
#         good_candies += 1
#     else:
#         bad.add(B)
was_good = 0
for idx, x in enumerate(weights):
    if idx == 0 and is_good(weights[1:]):
        good_candies += 1
        was_good = 1
    else:
        if x == weights[idx-1]:
            good_candies += was_good
            continue
        elif is_good(weights[:idx]+weights[idx+1:]):
            good_candies += 1
            was_good = 1
        else:
            was_good = 0


print(good_candies)

