def city_country(city, country):
    place = city + "," + country
    return place


city1 = city_country('guangzhou', 'china')
print(city1)

print("------------------------------")


def make_album(singer_name, album_name, numbers=''):
    songs = {'Singer Name': singer_name,
             'Album Name': album_name}
    if numbers:
        songs['Number'] = numbers
    return songs


while True:
    sn = input("Enter singer name or press 'q' to exit")
    if sn == 'q':
        break
    al = input("Enter album name or press 'q' to exit")
    if al == 'q':
        break
    else:
        num = input("Tell the number of album or press ENTER")
        if num:
            song = make_album(sn, al, num)
        else:
            song = make_album(sn, al)
    print(song)
