# 클래스 상속

class Human:
    """Super Class"""

    def __init__(self, name, age, gender):
        """Human constructor"""
        self.name = name
        self.age = age
        self.gender = gender
        self.grade = 0

    def get_profile(self):
        """Get profile"""
        profile = f"{self.name}, {self.age} years old"
        return profile.title()

    def set_profile(self, age):
        """Set profile"""
        if age < 0 or age > 100:
            print("age must be between 0 and 100")
            return
        else:
            self.age = age

    def get_grade(self):
        """Get grade"""
        print(f"Grade: {self.grade}")

    def set_grade(self, grade):
        """Set grade"""
        self.grade += grade

    # def get_uid(self):
    #     print("No UID")


# 서브 클래스 정의 시 class Sub(Super) 형식으로 정의
class User(Human):
    """Sub Class"""

    def __init__(self, name, age, gender):
        """User constructor"""
        # super()메서드로 슈퍼 클래스 요소 호출
        super().__init__(name, age, gender)
        # 서브 클래스는 서브 클래스만의 요소를 가짐
        # self.id = "id"
        self.uid = Uid()

    # 슈퍼 클래스의 메서드를 같은 이름으로 재정의 - 오버라이드 (Override)
    # def get_uid(self):
    #     """Get uid"""
    #     print(f"{self.id} is UID")



# 합성(composition) 을 위해 클래스 분리
class Uid:
    """Other Class"""

    def __init__(self, uid='id'):
        self.uid = uid

    def get_uid(self):
        """Get id"""
        return self.uid

    def get_user(self):
        """Get user"""
        if self.uid == 'id':
            message = "ID 설정 필요"
        else:
            message = f"ID : {self.uid}"

        print(message)

new_user = User('john', 32, 'M')
print(new_user.get_profile())
print(new_user.uid.get_uid())
new_user.uid.get_user()