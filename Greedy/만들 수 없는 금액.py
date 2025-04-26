# 1부터 target - 1까지의 모든 금액을 만들 수 있는지

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    if target < x:
        # 만들 수 없는 금액을 찾았을 때 반복 종료
        break

    target += x

print(target)
