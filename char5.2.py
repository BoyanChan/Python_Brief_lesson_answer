str1 = "Benz"
str2 = "benz"

if str1 == str2:
    print("Equals")
else:
    print("Not Equals")


if str1.lower() == str2:
    print("Equals")
else:
    print("Not Equals")

age1 = 18
age2 = 14
age3 = 22

if (age1 >= 18) and (age2 >= 18):
    print("All Adult")
else:
    print("Not all adult")

if (age1 >= 18) or (age3 >= 18):
    print("All Adult")
else:
    print("Not all adult")

names = ["Adam", "Jerry", "Tome"]
name = "Tome"
if name in names:
    print(name.title() + " is in the list")
else:
    print(name.title() + " is not in the list")
name = "Amy"
if name in names:
    print(name.title() + " is in the list")
else:
    print(name.title() + " is not in the list")

