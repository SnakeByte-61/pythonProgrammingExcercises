import shelve

#with shelve.open('ShelveTest') as fruit:
fruit = shelve.open('ShelveTest')
fruit['orange'] = "a sweet,orange citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "a sour , yellow citrus fruit"
fruit['grape'] = "a small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green itrus fruit"

print(fruit['lemon'])
print(fruit['grape'])

fruit.close()

print(fruit)