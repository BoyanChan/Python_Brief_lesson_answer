adam = {
    'first_name': "Adam",
    'last_name': "Lax",
    'city': 'New york'
    }

aeinstein = {
    'first_name': "albert",
    'last_name': "einstein",
    'city': 'princeton'
    }

mcurie = {
    'first_name': "marie",
    'last_name': "curie",
    'city': 'paris'
    }

names = [adam, aeinstein, mcurie]

for name in names:
    print('first_name: ' + name['first_name'].title())
    print('last_name: ' + name['last_name'].title())
    print('city: ' + name['city'].title())
    print("\n")

print("------------------------------")

favourite_places = {
    'jack': ["paris", "guangzhou"],
    'tom': ["new york", "shanghai"],
    'mary': ["san fansico", "beijing"]
    }

for name, places in favourite_places.items():
    print("\nName: "+name.title())
    print("Place liked: ")
    for place in places:
        print("\t"+place.title())

print("------------------------------")

cities = {
    'guangzhou': {
        'country': "china",
        'language': "chinese"
                 },
    'new york': {
        'country': 'america',
        'language': "english"
                },
    'paris': {
        'country': 'france',
        'language': "french"
             }
         }

for place,i_country in cities.items():
    print("\nCity: "+place.title())
    coun = i_country['country']
    lang = i_country["language"]
    print("\tCountry: "+coun.title())
    print("\tLanguage: "+lang.title())

