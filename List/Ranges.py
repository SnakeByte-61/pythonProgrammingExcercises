#print(range(100))
#
# myList = list(range(10))
# print(myList)

# even = list(range(0,1000,2))
# odd = list(range(1,1000,2))
#
# print(even)
# print(odd)

# myString ='abcdefghijklmnopqrstuvwxyz'
#
# print(myString.index('e'))
# print(myString[4])

# smallDecimals = range(0,10)
# # print(smallDecimals)
# # print(smallDecimals.index(985))
# # print(smallDecimals[985])
# #
# # sevens = range(7,100000,7)
# # x = int(input("please put a positive number"))
# #
# # if x in sevens:
# #     print("{} is divisible by  seven ".format(x))
#
# myRange = smallDecimals[::2]
# print(myRange)
# print(myRange.index(6))

# decimals = range(0,100)
#
# print(decimals)
#
# myRange = decimals[3:40:3]
# print(myRange)
#
# print('=' * 40)
#
# for i in range(3,40,3):
#     print(i)

#This is a tuple
t ="a","b","c"
# print(t)
#
# print("a","b","c")
# print(("a","b","c"))
# Tuple doesnot always need a parantheses

imelda = "More Mayhem","Emilda May",2011,((1,'Pulling the Rug'),(2,"Psycho"),(3,'Mayhem'),(4,'Kentish Town Waltz'))

print(imelda)
# In tuples this gives an error
# imelda[1] = "Imelda May"

# #way to change a tuple is
# imelda = imelda[0],"Imelda May",imelda[2]
# print(imelda)
#
# #the following does not work on the list
# #works on tuples, following is called unwrapping a tuple
title,artist,year,tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
    track,title = song
    print("\t Track number {} , Title: {}".format(track,title))










