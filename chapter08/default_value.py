# 함수의 매개변수에는 기본값 (default value) 지정 가능
def city_and_country(city, country = "korea"):
    """기본값이 있는 매개변수는 반드시 기본값이 없는 매개변수보다 뒤에 위치해야함"""
    print(f"{city.title()} in {country.upper()}")

# 매개변수를 전달하지 않을 시 기본 값 사용
city_and_country(city = "seoul")

# 매개변수 전달 시 전달된 값 사용
city_and_country(city = "tokyo", country = "japan")