from restaurant import Restaurant


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['a', 'b', 'c']

    def describe_restaurant(self):
        print("Restaurant name: " + str(self.restaurant_name).title())
        print("Cuisine type: " + str(self.cuisine_type).title())
        print("Served people: " + str(self.number_served).title())
        print("There are lots of ice cream to choose: ")
        for flavor in self.flavors:
            print(" -  " + str(flavor))


ics = IceCreamStand('q', 'w')
ics.describe_restaurant()
