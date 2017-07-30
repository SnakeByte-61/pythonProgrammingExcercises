# with open("binary", 'bw') as binFile:
#     for i in range(17):
#         binFile.write(bytes([i]))
#
#
# with open("binary","br") as binFile:
#     for b in binFile:
#         print(b)

# import pickle
#
# imelda = ("More Mayhem",
#           "imelda May",
#           '2011',
#           ((1,'Pulling the Rug'),
#            (2,'Psycho'),
#            (3,'Mayhem'),
#            (4,'Kentish Town Waltz')))
#
# even = list(range(0,10,2))
# odd = list(range(1,10,2))
#
# with open("imelda.pickle","wb") as pickleFile:
#     pickle.dump(imelda,pickleFile,protocol= pickle.HIGHEST_PROTOCOL)
#     pickle.dump(even,pickleFile,protocol= 0)
#     pickle.dump(odd,pickleFile,protocol= pickle.DEFAULT_PROTOCOL)
#     pickle.dump(29998308,pickleFile,protocol= pickle.DEFAULT_PROTOCOL)
#
#
#
# with open("imelda.pickle","rb") as pickleFile:
#     imelda2 = pickle.load(pickleFile)
#     evenList = pickle.load(pickleFile)
#     oddList = pickle.load(pickleFile)
#     number = pickle.load(pickleFile)
#
# print(imelda2)
#
# album,artist,year,trackList = imelda2
#
# print(album)
# print(artist)
# print(year)
# for track in trackList:
#     teackNumber, trackTitle = track
#     print(teackNumber,trackTitle)
#
#
# print("=" * 40)
#
# for i in evenList:
#     print(i)
# print("=" * 40)
#
# for i in oddList:
#     print(i)
#
# print("=" * 40)
#
# print(number)

import shelve

with shelve.open("Shelftest") as fruit:
    fruit['orange'] = "a sweet , orange, citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow citrus fruit"
    fruit['grape'] = "a small, sweet fruit growing in bunches"
    fruit['lime'] = "a sour , green citrus fruit"

    # print(fruit['lemon'])
    # print(fruit['grape'])
    #
    # fruit['lime'] = 'great with tequila'
    #
    # for snack in fruit:
    #     print(snack + ": " + fruit[snack])

    while True:
        shelfKey = input("Please enter a fruit: ")
        if(shelfKey == "quit"):
            break

        description = fruit.get(shelfKey)
        print(description)
#print(fruit)

