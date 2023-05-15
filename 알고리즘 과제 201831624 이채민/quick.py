import random

def quick_sort(array):
    if len(array) <= 1: # 리스트가 하나 이하의 원소만 담고 있다면 종료
        return array
    pivot = array[len(array) // 2] # 기준 = 피봇
    left = [x for x in array if x < pivot] # 기준 왼쪽
    middle = [x for x in array if x == pivot] # 기준 
    right = [x for x in array if x > pivot] # 기준 오른쪽
    return quick_sort(left) + middle + quick_sort(right) #각각 정렬 수행 후 전체 리스트 반환

# 랜덤 20개 정수 생성
num = [random.randint(1, 100) for _ in range(20)]
print("Before sorting:", num)

# 퀵 정렬 실행
sorted_num = quick_sort(num)
print("After sorting:", sorted_num)