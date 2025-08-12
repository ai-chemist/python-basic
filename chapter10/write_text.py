from pathlib import Path

path = Path('text.txt')

# write_text() 메서드로 파일에 쓰기
path.write_text('hello world')

# 숫자 저장시 str() 을 통해 문자열로 변환 필요
path.write_text(str(123413241))

# 여러 행 저장 시 문자열 합치기
contents = 'Hello World\n'
contents += str(3.141592)

path.write_text(contents)