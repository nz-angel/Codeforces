# Result: accepted

from math import sqrt

n_squares = int(input())
if n_squares == 1:
    print(2)
elif n_squares == 2:
    print(3)
else:
    s = sqrt(n_squares)
    if s % 1 > 0.5:
        print((int(s)+1)*2)
    elif s % 1 != 0:
        print(int(s)*2+1)
    else:
        print(int(s)*2)


