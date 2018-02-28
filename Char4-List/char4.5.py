foods = (12, 34, 56, 78)
for food in range(1, len(foods)+1):
    print(foods[food-1])

print("------------------------------")

# when u try to change value in tuple
# foods[1] = 5
#    foods[1] = 5
# TypeError: 'tuple' object does not support item assignment

foods = (15, 45, 78)
print("new")
for food in range(1, len(foods)+1):
    print(foods[food-1])
