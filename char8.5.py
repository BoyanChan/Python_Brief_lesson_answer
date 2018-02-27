def make_sandwich(*toppings):
    print("Making sandwich with following thing")
    for topping in toppings:
        print("- " + topping)


make_sandwich('ai')
make_sandwich('bw', 'ce', 'dq')
make_sandwich('as', 'zx')


def user_profile(first, last, **user_info):
    profile = {}
    profile['first name'] = first
    profile['last name'] = last

    for k, v in user_info.items():
        profile[k] = v

    return profile


def show_profile(profile):
    for k, v in profile.items():
        print((str(k).title()) + " is " + str(v).title())


user = user_profile('boyan', 'chan', location='hefei', grade=1)

show_profile(user)
