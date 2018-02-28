adam = {
    'first_name': "Adam",
    'last_name': "Lax",
    'age': 18,
    'city': 'New york',
    'tall': "180cm",
    }

for k, v in adam.items():
    print("\nKey: "+str(k))
    print("Value: "+str(v))

print("------------------------------")

rivers = {
    'nile': 'egypt',
    'pearl river': 'guangzhou',
    'chang jiang': 'shanghai'
}

for k, v in sorted(rivers.items()):
    print("The "+str(k.title())+" runs through "+str(v.title()))

any_rivers = ['nile', 'huang he', 'chang jiang']

print("------------------------------")

for any_river in any_rivers:
    if any_river in rivers.keys():
        print(any_river.title()+" is in the dictionary")
    else:
        print(any_river.title()+" is not in the dictionary")



