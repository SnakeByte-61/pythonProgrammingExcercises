#https://www.crowdcast.io/e/list-comprehensions

# If you are wrting an iterable into an iterable
# my_favorite_numbers = [1,1,2,3,5,8,13]
# doubled_numbers = []
#
# for n in my_favorite_numbers:
#     doubled_numbers.append(n* 2)
# print(doubled_numbers)
#
#
# #list Comprehension from for loop
#
# doubled_numbers = [n* 2 for n in my_favorite_numbers]
# print(doubled_numbers)
#


# doubled_numbers = [n*2 for n in my_favorite_numbers]
# print(doubled_numbers)

# import math
#
# numbers = range (101)
# #list(numbers)
#
# cubes_of_squares = []
#
# for n in numbers:
#     if math.sqrt(n).is_integer():
#         cubes_of_squares.append(n**3)
#
#
# cubes_of_squares = [
#     n**3
#     for n in numbers
#     if math.sqrt(n).is_integer()
# ]
# print(cubes_of_squares)
#
# names = ['Jeffery','Nicole','Wifred','Ashley','Dorothy','Cynthia','Jared','Eve']
#
# vowel_names = []
# for name in names:
#     if name[0].lower() in "aeiou":
#         vowel_names.append(name)
#
# vowel_names = [
#                name
#                for name in names
#                if name[0].lower() in "aeiou"
#                ]
# print(vowel_names)

# numbers = [1,2,3,4,5,6,7,8,9]
# # squares = []
# #sum_of_squares = 0
# #
# # for n in numbers:
# #     squares.append(n**2)
# #     sum_of_squares = sum(squares)
#
#
# sum_of_squares = sum(n**2 for n in numbers)
# print(sum_of_squares)

# words = ['hi','hiya','he','hello']
#
# def superstring_is_not_in_list(item,some_list):
#     return not any(item in x for x in some_list)
#
#
#
# # new_words =[]
# # w_in_x = False
# # for w in words:
# #     if superstring_is_not_in_list(w,words):
# #         new_words.append(w)
#
# new_words = [
#              w
#              for w in words
#              if superstring_is_not_in_list(w,words)]
#
# print(new_words)

#generators

# numbers = [1,2,3,4]
# # print(sum(numbers))
#
# g = (n ** 2 for n in numbers)
# print(sum(g))

#print(list(g))

# matrix = [
#     [row * 3 + i for i in range(1,4)]
#     for row in range (4)
# ]

#print(matrix)

# flatten = []
#
# for row in matrix:
#     for x in row:
#         flatten.append(x)

#print(flatten)

# flatten = [
#     x
#     for row in matrix
#     for x in row
#     ]
# print(flatten)


#dictionary comprehension

favorite_numbers = {
    'george': 58,
    'david' :983,
    'matt': 314,
    'margaret' : 48,
    'judith': 6
}

small_favorites = {}

for name, number in favorite_numbers.items():
    if number < 100:
        favorite_numbers[name] = number

small_favorites = {
    name : number
    for name, number in favorite_numbers.items()
    if number < 100

}
print(small_favorites)