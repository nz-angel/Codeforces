# Result: Time Limit Exceeded
# url: https://codeforces.com/contest/1234/problem/D


string = input()
ls_string = list(string)
queries = int(input())
for q in range(queries):
    inst_type, int_1, int_2 = input().split()
    if int(inst_type) == 1:
        ls_string[int(int_1)-1] = int_2
    else:
        print(len(set(ls_string[int(int_1)-1: int(int_2)])))