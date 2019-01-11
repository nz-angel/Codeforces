# Result: Accepted

accordion = list(input())

opening = accordion.index('[')
accordion.reverse()
closing = len(accordion) - accordion.index(']') - 1
accordion.reverse()
relevant = accordion[opening:closing + 1]
n_colons = relevant.count(':')
if n_colons < 2:
    print(-1)
else:
    frst_colon = relevant.index(':')
    relevant.reverse()
    lst_colon = len(relevant) - relevant.index(':') - 1
    relevant.reverse()
    new_acc = '[:'+''.join([x for x in relevant[frst_colon:lst_colon] if x == '|'])+':]'
    print(len(new_acc))
