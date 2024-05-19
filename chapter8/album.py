def make_album(artist_name, album_title, no_of_songs=None):
    """Describe a music album"""
    album = {'name': artist_name, 'title': album_title}

    if no_of_songs:
        album['songs'] = no_of_songs
    return album

# album = make_album('tay swift', 'red')
# print(album)
#
# album = make_album('frank ocean', 'moon river', 5)
# print(album)


while True:
    print("\nTell us your favourite artist")
    print("(Enter q to quit anytime)")

    artist_name = input('Your favourite artist: ')
    if artist_name == 'q':
        break

    album_title = input('Album title: ')
    if album_title == 'q':
        break

    album = make_album(artist_name, album_title)
    print(f"\n{album}")
