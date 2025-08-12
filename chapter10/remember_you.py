from pathlib import Path
import json

username = input('Enter your username: ')

path = Path('user.json')

# 입력받은 데이터를 json 문자열로 변환
contents = json.dumps(username)

# json 문자열로 변환한 데이터를 path 경로의 파일에 작성
path.write_text(contents)

print(f"We won't forget you {username}!")
