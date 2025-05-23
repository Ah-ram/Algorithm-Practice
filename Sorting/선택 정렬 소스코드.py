# 처리 되지 않은 데이터 중에서 제일 작은 값을 맨 앞과 바꿈
# 시간 복잡도 O(N**2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i    # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]    # 스와프

print(array)