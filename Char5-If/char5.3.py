alien_colors = ['green', 'yellow', 'red', 'pink', 'blue']
alien_color = alien_colors[0]

if alien_color == 'green':
    print("You kill the "+alien_color+" alien,get 5 points")
elif alien_color == 'yellow':
    print("You kill the " + alien_color + " alien,get 10 points")
else:
    print("You kill the " + alien_color + " alien,get 15 points")

alien_color = alien_colors[1]

print("------------------------------")

if alien_color == 'green':
    print("You kill the "+alien_color+" alien,get 5 points")
elif alien_color == 'yellow':
    print("You kill the " + alien_color + " alien,get 10 points")
else:
    print("You kill the " + alien_color + " alien,get 15 points")

alien_color = alien_colors[2]

print("------------------------------")

if alien_color == 'green':
    print("You kill the "+alien_color+" alien,get 5 points")
elif alien_color == 'yellow':
    print("You kill the " + alien_color + " alien,get 10 points")
else:
    print("You kill the " + alien_color + " alien,get 15 points")

print("------------------------------")

if 'blue' in alien_colors:
    print("has blue alien")
if 'pink' in alien_colors:
    print("has pink alien")