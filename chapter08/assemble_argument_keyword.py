# **kwargs 를 통해 임의의 키워드 인수를 모으는 매개변수 사용
def sign_on(name, email, **kwargs):
    kwargs['name'] = name
    kwargs['email'] = email
    return kwargs

# 메서드의 매개변수에 'key'가 없는 인수들은 **kwargs에 모아짐
user_0 = sign_on('kofi', 'kofi@a.net', age=13, password='********')

print(user_0)