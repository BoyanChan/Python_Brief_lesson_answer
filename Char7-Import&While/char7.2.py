while True:
    pizza_add = input("Tell us some toppings you want: \n(Enter 'quit' to exit)")
    if pizza_add == 'quit':
        break;
    else:
        print(pizza_add+" added.a")

print("------------------------------")

while True:
    age = input("Tell us your age: \n(Enter 'quit' to exit)")
    if age == 'quit':
        break
    if int(age) <= 3:
        print("free")
    elif int(age) <= 12:
        print("10 dollars")
    else:
        print("15 dollars")

