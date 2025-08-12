from pathlib import Path
import json

path = Path('user.json')

# 경로에 파일이 존재하는지 확인
if path.exists():
    contents = path.read_text()
    name = json.loads(contents)
    print(f"Welcome back, {name}!")
else:
    name = input("What is your name? ")
    contents = json.dumps(name)
    path.write_text(contents)
    print(f"We won't forget you {name}!")