def sequential_search(A, key):
    """순차 탐색 알고리즘"""
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1


A = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # 숫자 리스트
key = int(input("찾고자 하는 숫자를 입력하세요: "))  # 사용자로부터 찾고 싶은 숫자를 입력받음

index = sequential_search(A, key)  # 순차 탐색

if index == -1:
    print("찾고자 하는 숫자가 리스트 내에 존재하지 않습니다.")
else:
    print(f"찾고자 하는 숫자가 리스트 내에 존재합니다. 인덱스는 {index}입니다.")