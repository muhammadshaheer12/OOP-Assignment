# Base class A
class A:
    def show(self):
        print("Method from class A")

# Class B inherits from A and overrides show()
class B(A):
    def show(self):
        print("Method from class B")

# Class C inherits from A and overrides show()
class C(A):
    def show(self):
        print("Method from class C")

# Class D inherits from both B and C
class D(B, C):
    pass

# Create an object of D and call show()
obj = D()
obj.show()

# Print the Method (MRO) from Class D
print(D.__mro__)
