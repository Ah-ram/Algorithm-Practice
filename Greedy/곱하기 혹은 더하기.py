# input + map
s = list(map(int, list(input())))
s.sort()

result = s[0]

for i in range(1, len(s)):
    if result <= 1:
        result += s[i]
    else:
        result *= s[i]
    print(result)
