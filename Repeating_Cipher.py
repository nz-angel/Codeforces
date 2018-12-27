n = int(input())
word = input()

res = ''
letters_pos = [0, 1, 3]
for x in range(3,11):
    letters_pos.append(x+letters_pos[-1])

if n == 1:
    print(word)
else:
    word = list(word)
    relevant = [word[i] for i in letters_pos if i <= n-1]
    res = ''.join(relevant)
    print(res)
