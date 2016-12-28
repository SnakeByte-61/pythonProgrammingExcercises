name = input("Type in your name: ")
age = int(input("How old are you,{0}? ".format(name)))

if(age >17) and (age < 31):
    print("Welcome to the holdiay ,{}".format(name))
else:
    print("Sorry we cannot allow you, {}".format(name))