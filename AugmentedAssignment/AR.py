# number = '9,223,372,836,775,887'
#
# cleanedNumber = ''
#
# for i in range(0, len(number)):
#     if number[i] in '0123456789':
#         cleanedNumber += number[i]
#
# newNumber = int(cleanedNumber)
# print('The number is {}'.format(newNumber))
#
# x = 23
# x += 1
# print(x)

# ipAddress = input("Enter your IP Address :")
# if ipAddress[-1] != '.':
#     ipAddress += '.'
#
# segment = 1
# segmentLength = 0
# #character =""
# for character in ipAddress:
#     if character == ".":
#         print("Segment {} contains {} character".format(segment,segmentLength))
#         segment += 1
#         segmentLength = 0
#     else:
#         segmentLength += 1
# # #unless the final character in the string was a . , the we havenot printed the last segment
# # if character != '.':
# #     print("Segment {} contains {} character".format(segment,segmentLength))
#


# for i in range(10):
#     print('i is now {}'.format(i))

# i = 0
# while i <10:
#     print('i is now {}'.format(i))
#     i +=1

# availableExists = ['east','north east','south']
#
# chosenExits = ""
#
# while chosenExits not in availableExists:
#     chosenExits = input("Please choose a direction: ")
#     if chosenExits == 'quit':
#         print('Game over')
#         break
# else:
#     print('are you no glad you are out of a here')
#

import random
highest = 10
answer = random.randint(1,highest)

print('Please guess your number between 1 and {}: '.format(highest))
guess = 0 # initialze for the while loop to any number
numGuess = 1
while guess != answer:
    guess = int(input())
    if guess == 0:
        break
    elif guess == answer:
        print("well  you guessed it correctly")
        print("You guessed it in {} times".format(numGuess))
    elif guess < answer:
        print("Please guess higher")
    else:
        print("please guess lower")

    numGuess += 1





