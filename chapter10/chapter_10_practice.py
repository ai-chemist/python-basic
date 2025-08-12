from pathlib import Path

names = ''
while True:
    print("Enter 'q' to quit")
    name = input('Enter your name: ')
    if name == 'q':
        break
    else:
        names += f"{name.title()}\n"

path = Path('name.txt')

path.write_text(names)