# Result: ???

class graph:

    def __init__(self, vertices):
        self.vert = vertices
        self.adj_list = [[] for x in range(vertices)]

    def dfs(self, temp, v, visited):

        visited[v] = True
        temp.append(v)

        for i in self.adj_list[v]:
            if not visited[i]:
                temp = self.dfs(temp, i, visited)
        return temp

    def addEdge(self, v, w):
        self.adj_list[v].append(w)
        self.adj_list[w].append(v)

    def connected(self):
        visited = [False]*self.vert
        cc = []
        for v in range(self.vert):
            if not visited[v]:
                temp = []
                cc.append(self.dfs(temp, v, visited))
        return cc


def have_common_point(i1, i2):
    if i1[0] == i2[-1] or i1[-1] == i2[0]:
        return True
    elif max(0, min(i1[1], i2[1]) - max(i1[0], i2[0])) == 0:
        return False
    return True


n_queries = int(input())

for k in range(n_queries):

    n_intervals = int(input())
    distribution = [0]*n_intervals
    inters = []
    belongs_to_somewhere = [0]*n_intervals
    for i in range(n_intervals):
        inters.append(tuple(map(int, input().split())))
    A = set([])
    B = set([])
    g = graph(n_intervals)

    for idx, interval in enumerate(inters):
        if idx == n_intervals-1:
            continue
        for idx2, intrv in enumerate(inters[idx+1:]):
            if have_common_point(interval, intrv):
                g.addEdge(idx, idx2+idx+1)

    cc = g.connected()
    if len(cc) == 1:
        distribution = [-1]
    else:
        last = 1
        for comp in cc:
            for x in comp:
                distribution[x] = ((last+1) % 2) + 1
                last += 1


    # inters.sort(key=lambda x: x[0])
    # for interval in inters:
    #     if belongs_to(A, interval):
    #         distribution.append(1)
    #     elif belongs_to(B, interval):
    #         distribution.append(2)
    #     else:
    #         distribution.append(1)

    # if not A or not B:
    #     distribution = [-1]
    print(' '.join(map(str, distribution)))
