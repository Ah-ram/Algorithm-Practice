s = input()
num = 0
str_arr = []

for i in range(len(s)):
    if s[i].isdigit():
        num += int(s[i])
    else:
        str_arr.append(s[i])
str_arr.sort()
print(''.join(str_arr) + str(num))


# ss = list(input())
# st, num = [i for i in ss if i.isalpha()], [int(i) for i in ss if i.isdigit()]
# print(''.join(sorted(st)) + str(sum(num)))