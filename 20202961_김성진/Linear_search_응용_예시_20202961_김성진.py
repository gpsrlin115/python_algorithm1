def linear_search(words, target):
    """특정 단어를 문장에서 찾아 위치를 반환합니다."""
    for i in range(len(words)):
        if words[i] == target:
            return i
    return -1

def main():
    # 사용자로부터 문장과 찾고자 하는 단어 입력받기
    sentence = input("문장을 입력하세요: ")
    target = input("찾고자 하는 단어를 입력하세요: ")

    # 문장을 단어로 분리
    words = sentence.split()

    # 순차 탐색 실행
    position = linear_search(words, target)

    # 결과 출력
    if position == -1:
        print(f"'{target}' 단어가 문장에 없습니다.")
    else:
        print(f"'{target}' 단어는 문장의 {position + 1}번째 단어입니다.")

if __name__ == "__main__":
    main()