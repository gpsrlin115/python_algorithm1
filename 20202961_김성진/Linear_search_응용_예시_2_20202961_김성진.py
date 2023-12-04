def linear_search(user_ids, user_input):
    """사용자 ID 목록에서 특정 ID 찾아 반환"""
    for i in range(len(user_ids)):
        if user_ids[i] == user_input:
            return True
    return False

registerd_ids = ["user123", "user456", "user789", "member500"]

user_input = input("사용자 ID를 입력하세요: ")

if linear_search(registerd_ids, user_input):
    print("사용자 ID가 존재합니다.")
else:
    print("사용자 ID가 존재하지 않습니다.")