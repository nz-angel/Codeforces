# Result: Accepted

card = input()
hand = input().split()

res = 'NO'
for c in hand:
    if c[0] == card[0] or c[1] == card[1]:
        res = 'YES'
        break

print(res)