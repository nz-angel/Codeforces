n_students = int(input())
skillz = list(map(int, input().split()))

n_exercises = 0
skillz.sort()
for i in range(1,len(skillz)+1):
    if i % 2 == 1:
        n_exercises += skillz[i] - skillz[i-1]

print(n_exercises)