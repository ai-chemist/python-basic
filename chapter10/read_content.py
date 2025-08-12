# pathlib 라이브러리의 Path 클래스 import
from pathlib import Path

path = Path('pi_digits.txt')
m_path = Path('pi_million_digits.txt')

# path에 저장된 데이터에 read_text() 실행 - 메서드 체인 방식으로 rstrip() 추가 호출
contents = path.read_text().rstrip()
m_contents = m_path.read_text().rstrip()

# splitlines() - 문자열을 행 리스트로 변환
# lines = contents.splitlines()
pi_string = ''

# 리스트 형태 확인
# print(lines)

# 12줄 lines 변수 생성 대신 contents.splitlines()로 바로 접근 가능
for line in contents.splitlines():
    # print(f"Line : {line}")
    # line 마다 공백 제거
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
print(contents)

print(len(m_contents))
print(m_contents[:52])