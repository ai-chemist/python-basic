# def 키워드를 통해 함수를 정의
def greet_user(username): # username - 매개변수 (parameter)
    """Docstring - 함수 선언 부 다음에 함수의 역할을 설명"""
    print(f"Hello {username.title()}!")

# 함수 호출부
greet_user("smith") # smith - 인수 (argument)