a = b = c = d = 12

print(c)

a,b = 12,13

print(a,b)

a,b = b,a
#values are assigned on the right first
print("a is {}".format(a))
print("b is {}".format(b))