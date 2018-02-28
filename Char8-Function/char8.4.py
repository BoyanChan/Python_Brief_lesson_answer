magicians = ['a', 'b', 'c']


def show_magicians(magicians):
    for name in range(0, len(magicians)):
        print(magicians[name])


def make_great(magicians):
    for name in range(0, len(magicians)):
        magicians[name] = "The great " + magicians[name]

def make_great_defualt(magicians):
    for name in range(0, len(magicians)):
        magicians[name] = "The great " + magicians[name]
    return magicians

show_magicians(magicians)
make_great(magicians)
show_magicians(magicians)

print("------------------------------")

magicians = ['a', 'b', 'c']

magi=make_great_defualt(magicians[:])
show_magicians(magicians)
show_magicians(magi)

