# Nesting(중첩) - 리스트를 딕셔너리의 값으로 사용하거나, 딕셔너리를 리스트에 저장하는 것
human_0 = {'name' : 'arthur', 'age' : 30,}
human_1 = {'name' : 'john', 'age' : 40,}
human_2 = {'name' : 'matt', 'age' : 20,}

humans = [human_0, human_1, human_2]

for human in humans:
    print(human)

# range() 메서드를 사용해 자동 생성
aliens = []
for alien_num in range(20):
    new_alien = {'color' : 'purple', 'points': 5, 'speed' : 'normal'}
    aliens.append(new_alien)

for alien in aliens[:10]:
    print(alien)
print("---")

print(f"total : {len(aliens)}")

for alien in aliens[3::4]:
    if alien['color'] == 'purple':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 20
    elif alien['color'] == 'yellow':
        alien['color'] = 'blue'
        alien['speed'] = 'slow'
        alien['points'] = 3

for alien in aliens[:10]:
    print(alien)
print("---")