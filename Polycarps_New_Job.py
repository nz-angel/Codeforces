# Result: Time Limit Exceeded

n_queries = int(input())

replies = []

max_width = 0
max_height = 0

for k in range(n_queries):
    query = input()
    action = query[0]
    if action == '+':
        x, y = sorted(list(map(int, query[1:].split())))
        max_width = max(max_width, x)
        max_height = max(max_height, y)
    else:
        h, w = list(map(int, query[1:].split()))
        if (max_width <= h and max_height <= w) or (max_width <= w and max_height <= h):
            print('YES')
        else:
            print('NO')
