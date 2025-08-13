from city_country import city_country

def test_city_country():
    """Test city country"""
    city = "seoul"
    country = "korea"
    result = city_country(city, country)
    assert result == "Seoul, Korea"
    result_2 = city_country(city, country, 500000)
    assert result_2 == "Seoul, Korea : 500000"