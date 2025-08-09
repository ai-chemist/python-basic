def brew_coffee(orderer, *options):
    """커피 만드는 함수"""
    print(f"\n{orderer.title()}'s Coffee")
    for option in options:
        print(f"- option: {option.title()}")