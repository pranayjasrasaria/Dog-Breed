# create class
class animal:

    # class attribute
    species = "dog"

    # instance attribute
    def __init__(self, name, color):
        self.name = name
        self.color = color

# instantiate the animal class
blu = animal("Blu", "blue")
woo = animal("Woo", "green")

# access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# access the instance attributes
print("{} is {}".format(blu.name, blu.color))
print("{} is {}".format(woo.name, woo.color))