def upper_list(lower_list, upper_list):
    """lower to upper"""
    while lower_list:
        item = lower_list.pop()
        print(f"\nCurrent Item : {item}")
        upper_list.append(item.upper())

def print_list(target_list):
    """print all items in target_list"""
    print("\nPrint All")
    for item in target_list:
        print(item)

raw_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
modified_list = []

# 인수에 raw_list[:] 를 통해 사본 전달 가능 - 리스트 값 변경 X
upper_list(raw_list, modified_list)
print_list(modified_list)