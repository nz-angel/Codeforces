import itertools


def works(degs, turn_sequence):
    pos = 0
    for idx, i in enumerate(turn_sequence):
        if i:
            pos += degs[idx]
        else:
            pos -= degs[idx]
    if pos % 360 == 0:
        return True
    return False

n_turns = int(input())
degrees = []
for i in range(n_turns):
    degrees.append(int(input()))

if sum(degrees) == 360:
    print('YES')
else:
    maximum = max(degrees)
    idx = degrees.index(maximum)
    degrees.remove(maximum)
    if sum(degrees) == maximum:
        print('YES')
    elif sum(degrees) < maximum:
        print('NO')
    else:
        degrees.insert(idx, maximum)
        ls = list(itertools.product([0, 1], repeat=n_turns))
        for combination in ls:
            if works(degrees, combination):
                print('YES')
                break
        else:
            print('NO')