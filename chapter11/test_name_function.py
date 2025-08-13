# test 파일은 test_ 로 시작해야함
from name_function import get_upper_name

# test 함수는 test_ 로 시작해야함
def test_upper_name():
    """Upper Test"""
    upper_name = get_upper_name('AAAA', 'BBBB')
    assert upper_name == 'AAAA BBBB'

def test_upper_name_with_middle():
    """Middle Test"""
    upper_name = get_upper_name('AAA', 'CCC', 'BBB')
    assert upper_name == 'AAA BBB CCC'