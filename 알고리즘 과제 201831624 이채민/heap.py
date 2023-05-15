import random
import heapq

# 힙 정렬
def heap_sort(arr): 
    heap = [] # 힙 리스트
    for num in arr:
        heapq.heappush(heap, num)
    sorted_nums = []
    while heap:
        sorted_nums.append(heapq.heappop(heap))
    return sorted_nums

# 랜덤 20개의 정수 생성
num = [random.randint(1, 100) for _ in range(20)]
print("Before sorting:", num)

# 힙 정렬 실행
sorted_nums = heap_sort(num)
print("After sorting:", sorted_nums)
