# Dictionary - key-value collection, 키를 통해 값에 접근 가능

alien_0 = {'color': 'red', 'points': 5}

# 키를 통해 요소에 접근 가능
print(alien_0['color'])
print(alien_0['points'])
print(alien_0)

user_point = alien_0['points']
print(f"You earned {user_point} points.")

# 새로운 키-값 할당
alien_0['x_position'] = 200
alien_0['y_position'] = 500
print(alien_0)

# 빈 딕셔너리로 시작
alien_1 = {}
print("alien_1 :", alien_1)

alien_1['color'] = 'green'
alien_1['points'] = 300

print("alien_1 :", alien_1)

# 딕셔너리 값 수정
alien_1['color'] = 'blue'
print("alien_1 :", alien_1)

# 응용
alien_2 = {'x_position': 0, 'y_position': 0, 'speed': 'fast'}

print("alien_2 :", alien_2)

if alien_2['speed'] == 'fast':
    x_increment = 30
elif alien_2['speed'] == 'slow':
    x_increment = 10
else:
    x_increment = 20

alien_2['x_position'] = alien_2['x_position'] + x_increment

print("alien_2 moved X :", alien_2['x_position'])

alien_2['speed'] = 'slow'

if alien_2['speed'] == 'fast':
    x_increment = 30
elif alien_2['speed'] == 'slow':
    x_increment = 10
else:
    x_increment = 20

alien_2['x_position'] = alien_2['x_position'] + x_increment

print("alien_2 moved X :", alien_2['x_position'])

# 키-값 제거 - del dict['key']
print(alien_2)

del alien_2['speed']
print(alien_2)