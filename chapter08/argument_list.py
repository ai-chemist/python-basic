def upper_list(name_list):
    """list를 매개변수로 받는 메서드"""
    for i_name in name_list:
        print(i_name.upper())

names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 인수로 리스트 전달
upper_list(names)
