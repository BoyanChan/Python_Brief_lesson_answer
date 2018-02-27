car = input("What kind of car do you want to rent?: ")
print("Let me see if I can find you a "+car)

print("------------------------------")

people = input("How many people are there?: ")
people = int(people)
if people >= 8:
    print("There is no free table")
else:
    print("Please come with me")

print("------------------------------")
number = input("Input a number and i will tell you if this number integer times of 10: ")
number = int(number)
if number%10 == 0:
    print("Yes")
else:
    print("No")
