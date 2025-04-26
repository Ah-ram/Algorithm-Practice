# 완전 탐색 알고리즘: 가능한 경우의 수를 모두 검사
# 일반적으로 비효율적인 시간 복잡도를 가짐 -> 데이터가 100만 개 이하일 때 적절

# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)