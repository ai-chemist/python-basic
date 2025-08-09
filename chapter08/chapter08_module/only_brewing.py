# from 모듈명 import 함수명 - 특정 모듈의 특정 함수 가져오기
# as 를 사용하여 다른 이름으로 사용 가능
# from 모듈명 import * - 특정 모듈의 모든 함수 가져오기 (지양)
from coffee import brew_coffee as brew

brew("Name", "option1", "option2")