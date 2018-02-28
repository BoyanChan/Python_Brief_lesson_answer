class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name: " + str(self.restaurant_name).title())
        print("Cuisine type: " + str(self.cuisine_type).title())
        print("Served people: " + str(self.number_served).title())

    def open_restaurant(self):
        print(str(self.restaurant_name).title()+"Opening")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number