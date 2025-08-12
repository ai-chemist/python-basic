from pathlib import Path
from random import randint

# json 데이터 타입을 지원하는 json 모듈 import
import json

numbers = [randint(1, 10) for i in range(5)]

path = Path('numbers.json')
# json.dumps() - json 문자열로 변환 후 저장
contents = json.dumps(numbers)
path.write_text(contents)