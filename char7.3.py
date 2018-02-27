sandwich_order = ['a', 'b', 'c', 'c', 'c']
finished_order = []
while sandwich_order:
    sandwich = sandwich_order.pop()
    print(sandwich+" finished.")
    finished_order.append(sandwich)

print("All sandwich has finished: ")
for sand in range(0,len(finished_order)):
    print("\t"+finished_order[sand])

print("------------------------------")

print("One kind of sandwich sold out\nNow we have: ")
while 'c' in finished_order:
    finished_order.remove('c')

for sand in range(0,len(finished_order)):
    print("\t"+finished_order[sand])

print("------------------------------")
dream_place = {}
while True:
    name = input("What's your name?: ")
    place = input("Where do you want to travel?: ")

    dream_place[name] = place

    repeat = input("Press any key to continue,or press no to exit")
    if repeat.lower() == 'no':
        break

for n, p in dream_place.items():
    print(n+" wants to go:")
    print("\t"+p)
