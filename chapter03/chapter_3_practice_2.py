guests = ['종길', '성화', '수길', '진석']
print(f"Invited guest : {guests[0]}")
print(f"Invited guest : {guests[1]}")
print(f"Invited guest : {guests[2]}")
print(f"Invited guest : {guests[3]}")

can_not_visit = guests.pop(3)
guests.insert(2, '럼프')
print(f"Edited guest : {guests[0]}")
print(f"Edited guest : {guests[1]}")
print(f"Edited guest : {guests[2]}")
print(f"Edited guest : {guests[3]}")

print(f"{can_not_visit} is not guest now")

guests.insert(0, '킨')
guests.insert(2, '휘웅')
guests.append('꼭두')
print(f"More guests : {guests[0]}")
print(f"More guests : {guests[1]}")
print(f"More guests : {guests[2]}")
print(f"More guests : {guests[3]}")
print(f"More guests : {guests[4]}")
print(f"More guests : {guests[5]}")

print("Table is Full...")
popped_guest = guests.pop()
print(f"Popped guest : {popped_guest}, Sorry")
popped_guest2 = guests.pop()
print(f"Popped guest : {popped_guest2}, Sorry")
popped_guest3 = guests.pop()
print(f"Popped guest : {popped_guest3}, Sorry")
popped_guest4 = guests.pop()
print(f"Popped guest : {popped_guest4}, Sorry")

print(f"You survived : {guests[0]}")
print(f"You survived : {guests[1]}")
print(f"You survived : {guests[2]}")

del guests[2]
print(guests)
del guests[1]
print(guests)
del guests[0]
print(guests)

# practice 3-9
print(len(guests))