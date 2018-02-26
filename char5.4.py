names = ["Adam", "Jerry", "Tome", 'Eric', 'admin']

if names:
    for name in names:
        if name == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello "+name+".")
else:
    print("We need find some users!")


print("------------------------------")

current_users = ["adam", "jerry", "tome", 'eric', 'admin']
new_users = ["Willam", "Jerry", 'Mike', "Sherry", 'Tome']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user+", You need to change your name")
    else:
        print("It has not been used")

print("------------------------------")

numbers = [value for value in range(1, 25)]
for number in range(0, len(numbers)):
    if numbers[number] == 11 or numbers[number] == 12:
        print(str(numbers[number])+"th")
    elif numbers[number] % 10 == 1:
        print(str(numbers[number])+"st")
    elif numbers[number] % 10 == 2:
        print(str(numbers[number])+"ed")
    elif numbers[number] % 10 == 3:
        print(str(numbers[number])+"rd")
    else:
        print(str(numbers[number])+"th")
