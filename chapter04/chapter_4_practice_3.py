num_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print(num_list[:3])
print(num_list[3:5])
print(num_list[-3:])

drinks = ['coke', 'jack daniels', 'milk', 'coffee']
favorite = drinks[:]

drinks.append('water')
favorite.append('ade')

for d in drinks:
    print(d)

for f in favorite:
    print(f)