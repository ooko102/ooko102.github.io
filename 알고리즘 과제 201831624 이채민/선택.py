import random

#선택 정렬 구현
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i # 최솟값을 인덱스로 선정
        for j in range(i+1, n):
            if arr[j] < arr[min_index]: # index보다 작으면
                min_index = j # index 바꿔주기
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 랜덤 20개의 정수 생성
num = [random.randint(1, 100) for _ in range(20)]
print("Before sorting:", num)

# 선택 정렬 실행
selection_sort(num)
print("After sorting:", num)