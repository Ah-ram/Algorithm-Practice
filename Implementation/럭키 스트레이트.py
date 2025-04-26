n = int(input())

arr = [int(i) for i in str(n)]
print(arr)

half = len(arr) // 2
s1 = arr[:half]
s2 = arr[half:]

if sum(s1) == sum(s2):
    print("LUCKEY")
else:
    print("READY")


