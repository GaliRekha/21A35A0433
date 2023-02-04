#program to create and access an object
class abc:
    attribute=10
    def display(self):
        print("this is in a class")
obj=abc()
print(obj.attribute)
obj.display()
