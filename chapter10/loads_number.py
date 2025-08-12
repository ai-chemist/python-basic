from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()

# json.loads() - json 문자열을 데이터 타입으로 변환
numbers = json.loads(contents)
print(numbers)