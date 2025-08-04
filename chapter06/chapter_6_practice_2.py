real_dictionary = {
    'if' : 'condition',
    'for' : 'loop',
    'elif' : 'condition',
    'in' : 'with for',
    'and' : 'replace "&"',
    'or' : 'replace "|"',
}

for key, value in real_dictionary.items():
    print(f"{key} : {value}")