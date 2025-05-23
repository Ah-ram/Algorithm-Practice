# 화폐의 종류가 K개라고 할 때, 시간 복잡도는 O(K)
n = 1260
count = 0

# 큰 화폐 단위부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin    # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)