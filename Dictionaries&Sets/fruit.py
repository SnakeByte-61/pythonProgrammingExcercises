fruit = {'orange': 'a,sweet,citrus fruit',
         'apple': 'good for making cider',
         'lemon': 'a sour,yellow citrus fruit',
         'grape': 'a small, sweet fruit growing in bunches',
         'lime': 'a sour , green citrus fruit'}
print(fruit)

veg = {'cabbage' :"every child's favorite",
       'sprouts' : "mmm. , lovely",
       'spinach' : "can i have some more,please"}

#print(veg)
#to combine both the dictionaries. It doesnot return any object
veg.update(fruit)
#print(veg)
print(fruit.update(veg))
# to make a new dictonary object

niceAndNasty = fruit.copy()
niceAndNasty.update(veg)
print(niceAndNasty)

