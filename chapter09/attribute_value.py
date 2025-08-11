# 인스턴스 속성도 기본값 지정 가능 - __init__() 메서드에서 할당

class Human:
    """Human class"""
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



human_0 = Human("John", "25", "male")
print(human_0.get_profile())
human_0.get_grade()

# 인스턴스 속성 변경 - 속성 값 직접 수정
human_0.name = "Changed"
print(human_0.get_profile())

# 인스턴스 속성 변경 - 메서드를 통한 값 수정
human_0.set_profile(50)
print(human_0.get_profile())

# 인스턴스 속성 변경 - 메서드를 통한 값 증감
human_0.set_grade(5)
human_0.get_grade()