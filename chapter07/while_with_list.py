unconfirmed_list = ['a', 'b', 'c']
confirmed_list = []

while unconfirmed_list:
    # pop() - 리스트의 마지막 요소를 리스트에서 제거하며 반환
    current = unconfirmed_list.pop()

    print("Confirmed :", current)
    confirmed_list.append(current)

print("Confirmed :", confirmed_list)

lists = ['a', 'a', 'b', 'c']

# 모든 값이 사라질 때까지 반복
while 'a' in lists:
    lists.remove('a')
print("List :", lists)