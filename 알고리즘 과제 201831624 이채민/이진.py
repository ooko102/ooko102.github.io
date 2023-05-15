import random

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 이진트리
def insert_node(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert_node(root.left, val)
    else:
        root.right = insert_node(root.right, val)

    return root
# 검색
def search_node(root, val):
    if root is None or root.val == val:
        return root

    if val < root.val:
        return search_node(root.left, val)
    else:
        return search_node(root.right, val)
# 8번째로 큰 수 검색하기
def find_kth_largest(root, k):
    stack = []
    node = root

    while True:
        while node:
            stack.append(node)
            node = node.right

        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val

        node = node.left
# 삭제 노드
def delete_node(root, val):
    if root is None:
        return root

    if val < root.val:
        root.left = delete_node(root.left, val)
    elif val > root.val:
        root.right = delete_node(root.right, val)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = find_minimum(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)

    return root

def find_minimum(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# 랜덤한 20개의 정수 생성
numbers = [random.randint(1, 100) for _ in range(20)]
print("인덱스는:", numbers)

# 이진 트리 생성
root = None
for num in numbers:
    root = insert_node(root, num)

# 랜덤 검색
target = random.choice(numbers)
found_node = search_node(root, target)
if found_node:
    print("랜덤 노드는 ", target, "입니다")
else:
    print("랜덤 노드를", target, "못 찾았습니다.")

# 8번째로 큰 수 찾기
kth_largest = find_kth_largest(root, 8)
print("8번째로 큰 수는:", kth_largest)

# 하나씩 삭제되는 상황 구현
deleted_numbers = []
for _ in range(len(numbers)):
    deleted_number = random.choice(numbers)
    numbers.remove(deleted_number)
    deleted_numbers.append(deleted_number)
    root = delete_node(root, deleted_number)
    print("삭제 노드", deleted_number)
    print("현 리스트:", numbers)
    print("삭제된 노드:", deleted_numbers)
    print()
