# None 은 플레이스홀더의 역할을 함
def make_dict(name, age, city, email=None):
    """make dictionary"""
    person = {'name': name.title(), 'age': age, 'city': city.upper()}

    # None을 기본값으로 두고 값이 들어온 경우에는 딕셔너리에 키-값 추가 후 반환
    if email:
        person['email'] = email
    return person

human = make_dict('kurt',25,'Berlin')
print(human)
print(human['name'])
print(human['age'])
print(human['city'])

alien = make_dict('piposiso', 972834, 'unknown city', 'alien@gmail.com')
print(alien)
print(alien['name'])
print(alien['age'])
print(alien['city'])
print(alien['email'])

# while & method
while True:
    print('Press "i" to Stop')
    i_name = input('What is your name? ')
    if i_name == 'i':
        break
    i_age = input('Age? ')
    if i_age == 'i':
        break
    else:
        i_age = int(i_age)
    i_city = input('City? ')
    if i_city == 'i':
        break
    f_dict = make_dict(i_name, i_age, i_city)
    print(f_dict)


