def get_title(first_name, last_name, middle_name = ''):
    """결과 표시 대신 반환값을 가지는 함수"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

# 인수 전달 후 함수를 통해 가공된 값 반환받아 name 변수에 저장
name = get_title('kurt', 'cobain')
print(name)

name_with_middle = get_title(first_name='john', middle_name='anthony', last_name='smith')
print(name_with_middle)
