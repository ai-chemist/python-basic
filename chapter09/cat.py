class Cat:
    """Cat 클래스"""

    # 생성자 함수 __init__(self, ...)
    # self - 인스턴스 자체를 의미
    def __init__(self, name, species):
        """name, species 속성 초기화"""
        self.name = name
        self.species = species

    def sleep(self):
        """잠자기"""
        print(f"{self.name.title()} Sleeping")

    def eat(self):
        """먹기"""
        print(f"{self.name.title()} Eating")

# 인수를 전달하여 __init__ 메서드 호출
my_cat = Cat("J", "British Shorthair")

# 인스턴스.속성 - 인스턴스의 속성에 접근
print(my_cat.name)
print(my_cat.species)

# 인스턴스.메서드 - 인스턴스의 메서드 호출
my_cat.sleep()
my_cat.eat()

# 인스턴스는 여러 개 생성 가능
unknown_cat = Cat("U", "Korean Shorthair")

print(unknown_cat.name)
print(unknown_cat.species)

unknown_cat.sleep()
unknown_cat.eat()