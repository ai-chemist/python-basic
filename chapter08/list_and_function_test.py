def not_change(words):
    """word 는 for 문 내부의 변수일 뿐?"""
    for word in words:
        word = word.upper()
    return words

word_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
after_list = not_change(word_list)

print(word_list)
print(after_list)