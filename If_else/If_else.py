# age = int(input("How old are you?"))
#
# # if 15 < age < 66:
# #     print
# #it is very important during class
# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("have a nice day")

# weird used
# x = 'false'
# if x:
#     print('x is true')

# x = input("Please enter some text")
#
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print('You entered nothing')

# print(not False)
# print(not True)

parrot = "Norweginian Blue"
letter = input('Enter a character: ')

if letter not in parrot:
    print('Give me an {}, Bob'.format(letter))
else:
    print("I donot need that letter")
