# Result: Accepted

import string

n_queries = int(input())

words = []
num2alpha = dict(zip(range(1, 27), string.ascii_lowercase))

for query in range(n_queries):
    n, k = list(map(int, input().split()))
    ocurrence = n // k
    mx = n % k
    s = ''
    for letter in range(1,k+1):
        if letter == 1:
            s += 'a' * (ocurrence + mx)
        else:
            s += num2alpha[letter] * ocurrence
    words.append(s)

for w in words:
    print(w)


