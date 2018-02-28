class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant name: " + str(self.restaurant_name).title())
        print("Cuisine type: " + str(self.cuisine_type).title())

    def open_restaurant(self):
        print("Opening")


ddd = Restaurant("diandoude", "moring tea")
ddd.describe_restaurant()
ddd.open_restaurant()
