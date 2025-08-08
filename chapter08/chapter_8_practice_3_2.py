def make_album(singer, title):
    i_album = f"{singer}'s Album : {title}"
    return i_album

album_1 = make_album('Nirvana', 'Nevermind')
album_2 = make_album('Oasis', '(What\'s the Story) Morning Glory?')
album_3 = make_album('Queen', 'A Night at the Opera')

album_list = [album_1, album_2, album_3]

for album in album_list:
    print(album)