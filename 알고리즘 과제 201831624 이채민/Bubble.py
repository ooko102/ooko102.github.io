import random

# 버블 정렬 구현
def bubble_sort(arr): 
    n = len(arr)
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]: # 조건 + 자리 바꾸기 
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 랜덤 20개의 정수 생성
num = [random.randint(1, 100) for _ in range(20)]
print("Before sorting:", num)

# 버블 정렬 실행
bubble_sort(num)
print("After sorting:", num)