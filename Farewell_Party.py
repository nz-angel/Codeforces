# Incompleto: Time Limit Exceeded

class Grupo():

    def __init__(self, cap):
        self.group = set()
        self.capacity = cap
        self.full = 0

    def membership(self):
        return self.capacity

    def is_full(self):
        if len(self.group) == self.capacity:
            self.full = 1
            return True
        else:
            return False

    def add_member(self, new_member):
        self.group.add(new_member)

    def get_members(self):
        return self.group


n = int(input())
seq = list(map(int, input().split()))

groups_list = []

for i, nro in enumerate(seq):
    added = 0
    belongs_to = n - nro
    for g in groups_list:
        if not g.is_full() and g.membership() == belongs_to:
            g.add_member(i)
            added = 1
            break
    if added == 0:
        new_g = Grupo(belongs_to)
        new_g.add_member(i)
        groups_list.append(new_g)

sombreros = [-1]*n
sombrero = 1
imp = 0
for g in groups_list:
    if not g.is_full():
        imp = 1
        break
    else:
        for k in g.get_members():
            sombreros[k] = sombrero
        sombrero += 1

if imp:
    print('Impossible')
else:
    print('Possible')
    print(' '.join(str(x) for x in sombreros))








