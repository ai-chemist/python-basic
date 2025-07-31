for value in range(1, 21):
    print(value)

num_list = [value for value in range(1, 1000001)]
for num in num_list:
    print(num)

print(min(num_list))
print(max(num_list))
print(sum(num_list))

odds = [value for value in range(1, 21, 2)]
for odd in odds:
    print(odd)

threes = [value for value in range(1, 31, 3)]
for three in threes:
    print(three)

cubes = [value ** 3 for value in range(1, 11)]
for cube in cubes:
    print(cube)