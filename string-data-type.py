"""
Your module description
"""
myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("Whats is your name? ")
print(name)

color = input("whats is your favorite color? ")
animal = input("whats is your favorite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))

