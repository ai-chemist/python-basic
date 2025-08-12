from pathlib import Path
import json

def get_stored_name(path):
    """저장된 사용자 이름 가져오기"""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_user(path):
    """새로운 사용자 생성"""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """인사 하기"""
    path = Path('user.json')
    username = get_stored_name(path)

    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_user(path)
        print(f"We won't forget you {username}!")

greet_user()