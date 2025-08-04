# 비슷한 객체 딕셔너리

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['jen']
print("Jen's Favorite :", language)

# get()
alien_0 = {'color': 'purple'}

# get('키', '키가 없을 경우 할당 값')
point = alien_0.get('points', 'No assigned value')
print(point)

# get() 두번 째 인수 생략 시 - None 반환
speed = alien_0.get('speed')
print(speed)