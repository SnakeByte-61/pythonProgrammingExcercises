# cities = ['Adelaide','Alice Springs','Darwin','Melbourne','Sydney']
#
# with open("cities.txt",'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)


# cities = []
# with open('cities.txt','r') as cityFile:
#     for city in cityFile:
#         cities.append(city.strip('\n'))
#
# print(cities)
#
# for c in cities:
#     print(c)

# imelda = 'more Mayhem','Imelda May','2011',(
#     (1,'Pulling the rug'),(2,'Psycho'),(3,'Mayhem'),(4,'Kentish Town Waltz'))
#
# with open('imelda.txt','w') as imeldaFiles:
#     print(imelda, file=imeldaFiles)

# with open('imelda.txt', 'r') as imeldaFile:
#     contents = imeldaFile.readline()
#
# imelda = eval(contents)
# print(imelda)
#
# title,artist,year, tracks = imelda
#
# print(title)
# print(artist)
# print(year)
# #print(tracks)

with open('sample.txt','a') as tables:
    for i in range(2,13):
        for j in range(1,13):
            print("{1:>2} times {0} is {2} ".format(i,j,i*j),file = tables)
        print("-" * 20,file=tables)

