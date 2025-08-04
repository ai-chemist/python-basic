favorite_languages = {
    'dennis ritchie' : 'python',
    'james gosling' : 'c++',
}

survey_list = ['dennis ritchie', 'james gosling', 'guido van rossum', 'mac']
for name in survey_list:
    if name in favorite_languages:
        print(f"{name.title()}'s favorite language is {favorite_languages[name].upper()}")
    else:
        print(f"Please fill out the survey {name.title()}")