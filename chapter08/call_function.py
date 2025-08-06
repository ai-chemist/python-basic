def same(a, b = 'b'):
    print(f"{a.title()} in {b.title()}")

# 아래 호출은 모두 같은 결과를 반환
same('a')
same(a = 'a')
same('a', 'b')
same(a = 'a', b = 'b')
same(b = 'b', a = 'a')