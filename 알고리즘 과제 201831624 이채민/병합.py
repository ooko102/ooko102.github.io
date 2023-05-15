import random

# 병합 정렬 기준 잡기 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid] # 왼쪽
    right = arr[mid:] # 오른쪽

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right) # 

# 병합하기
def merge(left, right):
    merged = [] 
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left): # 왼쪽 인덱스 정렬
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right): # 오른쪽 인덱스 정렬
        merged.append(right[right_index])
        right_index += 1

    return merged # 병합

# 랜덤 20개의 정수 생성
num = [random.randint(1, 100) for _ in range(20)]
print("Before sorting:", num)

# 병합 정렬 실행
sorted_num = merge_sort(num)
print("After sorting:", sorted_num)
