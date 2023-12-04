def linear_search(books, target):
    """도서목록에서 특정 도서를 찾아 위치를 반환"""
    for i in range(len(books)):
        if books[i].lower() == target.lower():
            return i
    return -1

book_list = ["파이썬 프로램래밍", "점프 투 파이썬", "인공지능의 기초"]

search_title = input("찾고자 하는 책의 제목을 입력하세요: ")

position = linear_search(book_list, search_title)

if position == -1:
    print("찾고자 하는 책이 존재하지 않습니다.")
else:
    print(f"찾고자 하는 책이 존재합니다. {position + 1}번 책장에 위치해 있습니다.")