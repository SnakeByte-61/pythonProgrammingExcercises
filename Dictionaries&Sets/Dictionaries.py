fruit = {'orange': 'a,sweet,citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a sour,yellow citrus fruit',
         'grape': 'a small, sweet fruit growing in bunches',
         'lime': 'a sour , green citrus fruit'}


# print(fruit['lemon'])

# bike = {'make': 'Honda',
#         'model': '250 dream',
#         'color': 'red',
#         'engineSize': 250}
# print(bike['engineSize'])

# fruit['pear'] = "an odd shaped apple"
# print(fruit)
# fruit["lime"] = "great with tequila"
# print(fruit)
# del fruit['lemon']
# print(fruit)
# #fruit.clear
# print(fruit['tomato'])

#print(fruit)

# while True:
#     dictKey = input("Please enter a fruit: ")
#     if dictKey == 'quit':
#         break
#     if dictKey in fruit:
#     ##Python2 in fruit.has_key(dictKey)
#         description = fruit.get(dictKey)
#         print(description)
#     else:
#         print("we do not have a " + dictKey)

    # description = fruit.get(dictKey,"We do not have a " + dictKey)
    #
    # print(description)

# for snack in fruit:
#     print(fruit[snack])
#

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

# to sort the dictionary as there is no inbuilt method
# orderedkeys = list(fruit.keys())
# orderedkeys.sort()

# orderedKeys = sorted(list(fruit.keys()))
#
# for f in orderedKeys:
#     print(f + "-" + fruit[f])

# for f in sorted(fruit.keys()):
#     print(f + " - " + fruit[f])

# #Not as good effecient as the folowing method
# for val in fruit.values():
#     print(val)
#
# print('-' * 40)
#
# for key in fruit:
#     print(fruit[key])
# fruitKeys = fruit.keys()
# print(fruitKeys)
#
# fruit['tomato'] = 'not nice with icecream'
# print(fruitKeys)

#print(fruit.values())

#print(fruit.items())

#fTuple = tuple(fruit.items())
#print(fTuple)

# for snack in fTuple:
#     item,description = snack
#     print(item + " is " + description)
#
#
# print(dict(fTuple))

# myList = ['a','b','c','d']
# letters = 'abcdefghijkl'
# numbers ='123456789'
#
# newString = ''
# #for c in myList:
# #     newString += c + ','
# #newString = ','.join(letters)
#
# newString =' mississippi '.join(numbers)
# print(newString)

