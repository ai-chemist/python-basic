from pathlib import Path
import json

path = Path('user.json')

# path 경로의 파일에서 텍스트 읽음
contents = path.read_text()

# 읽어온 텍스트를 json 형식으로 변환
name = json.loads(contents)

print(f"Welcome back, {name}!")