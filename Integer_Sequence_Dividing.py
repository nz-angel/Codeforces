# Result: Accepted

n = int(input())

if n % 2 == 1:
    if ((n+1)//2) % 2 == 0:
        print(0)
    else:
        print(1)
else:
    if (n//2) % 2 == 0:
        print(0)
    else:
        print(1)
