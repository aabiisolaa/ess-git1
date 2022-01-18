class Fruit:
    def __init__(self):
        print("this is an apple")
    
    def nutrition(self):
        print("gives vitamin b")

    def fruit_shape(self):
        print("circle")


class Coconut(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("you created a new fruit instance")

    def nutrition(self):
        print("gives vitamin c")

    def color(self):
        print("coconuts are brown")

f = Fruit()
f.nutrition()
f.fruit_shape()


c = Coconut()
c.nutrition()
c.fruit_shape()
c.color()