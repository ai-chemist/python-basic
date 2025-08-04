names = {
    'd.trump' : {
        'first' : 'donald',
        'last' : 'trump',
    },
    'v.putin' : {
        'first' : 'vladimir',
        'last' : 'putin',
    },
    'e.musk' : {
        'first' : 'elon',
        'last' : 'musk',
    },
}

for name, info in names.items():
    print(f"Name : {name.title()}")
    full_name = f"{info['first'].title()} {info['last'].title()}"
    print(f"Full name : {full_name.title()}")