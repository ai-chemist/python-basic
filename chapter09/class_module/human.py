"""파일의 처음에 독스트링 적는 습관"""

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

class User(Human):
    """Sub Class"""

    def __init__(self, name, age, gender):
        """User constructor"""
        super().__init__(name, age, gender)
        self.uid = Uid()


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