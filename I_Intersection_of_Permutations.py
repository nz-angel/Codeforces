# Incompleto: time limit exceeded

size, queries = list(map(int, input().split()))

a = list(map(int, input().split()))
b = list(map(int, input().split()))


n_intersec = []
universe = set(range(1, size+1))

for n in range(queries):
    nro = 0
    rule = list(map(int, input().split()))
    if rule[0] == 2:
        b[rule[1]-1], b[rule[2]-1] = b[rule[2]-1], b[rule[1]-1]
    else:
        if rule[1] == 1 and rule[2] == size:
            nro = rule[4] - rule[3] + 1
        elif rule[3] == 1 and rule[4] == size:
            nro = rule[2] - rule[1] + 1
        else:
            a_slice = a[rule[1]-1:rule[2]]
            b_slice = b[rule[3]-1:rule[4]]
            if len(a_slice) >= len(b_slice):
                bigger = a_slice
                smaller = b_slice
            else:
                bigger = b_slice
                smaller = a_slice
            nro = len(set(smaller).intersection(bigger))
        n_intersec.append(nro)

for i in n_intersec:
    print(i)