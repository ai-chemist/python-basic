# 매개변수 여러 개 사용
def pet_and_owner(pet_name, owner_name):
    print(f"Hello {owner_name.title()} and PET : {pet_name.title()}!")

# 선언부의 매개변수 순서에 맞게 인수 전달
pet_and_owner("george", "arthur")
pet_and_owner("smith", "bark")

# 의도적으로 순서 바꿔 전달
pet_and_owner("owner", "pet")