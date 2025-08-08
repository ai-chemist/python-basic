# '*' 기호를 사용하여 임의의 개수의 인수를 하나로 모을 수 있음
def assemble(leader, *humans):
    """*humans 부분은 관례상 *args 사용하는 경우가 많음"""
    print("\nAssemble")
    print(f"Leader: {leader}")
    print("Team")
    # if로 확인하지 않아도 humans에 전달된 값이 없는 경우 실행되지 않음
    for human in humans:
        print(f"- {human}")

assemble('eden')

# 위치 인수와 함께 사용
assemble('eden', 'jena')
assemble('steve', 'tony', 'bruce')
