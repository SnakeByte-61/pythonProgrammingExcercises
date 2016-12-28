# ipAddress = input('please enter an ip address : ')
# print(ipAddress.count('.'))


# parrotList = [' non pinin',' no more',' a stiff',' bereft of live']
#
# parrotList.append('Norwegian blue')
# for state in parrotList:
#     print('The parrot is ' + state)

# even = [2,4,6,8]
# odd = [1,3,5,7,9]
#
# numbers = even + odd
# #numbers.sort()
# print("The numbers are {}".format(sorted(numbers)))


# list1 =[]
# list2 = list()
#
# print("List 1: {}".format(list1))
#
# print("List 2: {}".format(list2))
#
# if list1 == list2:
#     print("the lists are equal")
#
# print(list("the lists are equal"))


# even = [2,4,6,8]
#
# anotherEven = list(even)
#
# print(anotherEven is even)
# anotherEven.sort(reverse=True)
# print(even)

# even = [2,4,6,8]
# odd = [1,3,5,7]
#
# numbers = [even , odd]
#
# for numberSet in numbers:
#     print(numberSet)
#
#     for value in numberSet:
#         print(value)

# menu = []
# menu.append(['egg','spam','bacon'])
# menu.append(['egg','sausage','bacon'])
# menu.append(['egg','spam'])
# menu.append(['egg','bacon','spam'])
# menu.append(['egg','bacon','sausage','spam'])
# menu.append(['spam','bacon','sausage','spam'])
# menu.append(['spa,','egg','spam','spam','bacon','spam'])
# menu.append(['spam','egg','sausgae','spam'])


#print(menu)

# for meal in menu:
#     if not 'spam' in meal:
#         print(meal)
#
#         for ing in meal:
#             print(ing)


list1 = [1,2,3,4,5,6,7,8,9,10]

listIterator = iter(list1)

for eachNumber in range(0,len(list1)):
    print(next(listIterator))

# for char in string:
#     print(char)

#my_iterator = iter(string)
#print(my_iterator)# shows the object and the place in memory
#print(next(my_iterator))
