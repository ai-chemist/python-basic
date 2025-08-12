from pathlib import Path

path = Path('unknown.txt')
try:
    # 타 컴퓨터에서 작성된 파일을 읽을 수도 있기에 encoding 인수 지정
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print("File not found")