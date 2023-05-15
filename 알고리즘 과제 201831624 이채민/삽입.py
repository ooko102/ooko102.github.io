import random

#삽입 정렬 구현
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i] # 키 선정
        j = i - 1
        while j >= 0 and arr[j] > key: # j가 키보다 크면
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key

# 랜덤 20개의 정수 생성
num = [random.randint(1, 100) for _ in range(20)]
print("Before sorting:", num)

# 삽입 정렬 실행
insertion_sort(num)
print("After sorting:", num)