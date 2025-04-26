n, m = map(int, input().split())
k = list(map(int, input().split()))

# total = 0
# for i in range(1, n):
#     total += i
#
# print(total - (n-m))


answer = 0

for i in range(len(k)):
    for j in range(i + 1, len(k)):
        if k[i] != k[j]:
            answer += 1
print(answer)
