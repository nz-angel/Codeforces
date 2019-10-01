# Result: Accepted
# url: https://codeforces.com/contest/1234/problem/B1

n, k = list(map(int, input().split()))
incoming_msg = list(map(int, input().split()))
screen = []
for friend in incoming_msg:
    if friend in screen:
        continue
    elif len(screen) < k:
        screen = [friend] + screen
    else:
        screen.pop()
        screen = [friend] + screen
print(len(screen))
print(' '.join(map(str, screen)))





