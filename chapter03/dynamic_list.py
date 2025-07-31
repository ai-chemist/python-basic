animals = ['lion', 'tiger', 'whale']
print(animals)

# List 요소의 값 변경
animals[-1] = 'eagle'
print(animals)

# append() 로 마지막에 요소 추가
animals.append('cow')
animals.append('pig')
animals.append('horse')
print(animals)

# insert() 로 원하는 부분에 요소 삽입 - 다른 값들은 삽입된 부분 기준 우측으로 이동
animals.insert(3, 'Jaguar')
print(animals)

# del 문을 사용하여 요소 제거
del animals[2]
print(animals)
print(animals[2])

# pop() 으로 요소 제거 후 값 사용
popped_animal = animals.pop()
print(animals)
print(popped_animal)

# pop() 인덱스 지정으로 원하는 위치 요소 제거 후 값 사용
message = f"Popped Animal is {animals.pop(2)}"
print(animals)
print(message)

# remove() 로 값 기반 제거 - 지정한 요소와 일치하는 첫 요소만 제거
animals.remove('pig')
print(animals)