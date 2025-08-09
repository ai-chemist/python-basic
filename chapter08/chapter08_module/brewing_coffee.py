# import 모듈명 - 다른 파일에서 모듈을 가져오기
# as 를 사용하여 다른 이름으로 사용 가능
import coffee as c

# 모듈명.함수명() - 가져온 모듈의 함수 실행
c.brew_coffee("paul bassett", "Grand", "Lungo")
c.brew_coffee("john", "americano")