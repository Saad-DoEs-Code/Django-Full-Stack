import math


class Circle:

    # Global Properties that will remain same for each instance of the class
    pi = math.pi

    # Local Properties that will be defined for each instance separately
    def __init__(self, radius = 0):
        self.radius = radius

    def area(self):
        # using "self" to refer to the concerned/ currently assigned "radius"
        # using "Cirlcle" to refer to the object level value of "pi"
        print("Calculating Area:")
        return (self.radius*self.radius)*Circle.pi

    def set_radius(self, new_radius):
        print(f"Old Radius {self.radius}")
        self.radius = new_radius
        print(f"New Radius {self.radius}")


myCircle = Circle()
myCircle.radius = 2.5
print(myCircle.area())  # Output: 19.634954084936336
myCircle.set_radius(3)
print(myCircle.area())  # Output: 28.274333882308138
