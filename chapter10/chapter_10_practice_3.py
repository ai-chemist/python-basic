from pathlib import Path
import json

def get_information(path):
    """파일 읽기"""
    contents = path.read_text()
    return json.loads(contents)

def new_information(path):
    """새롭게 파일 작성"""
    name = input("What is your name? ")
    f_language = input("What is your favorite programming language? ")
    f_color = input("What is your favorite color? ")
    user = {'name': name, 'language': f_language, 'color': f_color}
    path.write_text(json.dumps(user))
    print(f"We won't forget you {user['name']}!")

def main():
    path = Path('favorite.json')

    """경로에 파일 유무"""
    if path.exists():
        information = get_information(path)
        print(f"Information : {information}")

        """정보 일치 여부 확인"""
        truth = input("Is this your information correct? (Y/N)")
        if truth == "n" or truth == "N":
            new_information(path)
        else:
            """불일치인 경우 새롭게 정보 받기"""
            print(f"Welcome back, {information['name']}!")
        # print(type(information)) - dictionary 여부 확인용
    else:
        new_information(path)

main()