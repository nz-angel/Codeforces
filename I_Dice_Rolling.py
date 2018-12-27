n_queries = int(input())

desired_n = []
for k in range(n_queries):
    desired_n.append(int(input()))

for i in desired_n:
    n_rolls = i // 2
    print(n_rolls)
