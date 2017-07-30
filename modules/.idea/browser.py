# import webbrowser
#
# webbrowser.open("https://www.python.org")
#
# help(webbrowser)

import time
# print(time.gmtime(0))
# print(time.localtime())
# print(time.time())

# timeHere = time.localtime()
# print(timeHere)
# print("Year: ",timeHere[0],timeHere.tm_year)
# print("Month: ",timeHere[1],timeHere.tm_mon)
# print("Day: ",timeHere[2],timeHere.tm_mday)

# from time import perf_counter as myTimer
# import random
# input("Press enter to start ")
# waitTime = random.randint(1,6)
# time.sleep(waitTime)
# startTime = myTimer()
# input("Please enter to stop")
#
# endTime = myTimer()
#
# print("Started at " + time.strftime("%X", time.localtime(startTime)))
#
#
# print("Ended at " + time.strftime("%X", time.localtime(endTime)))
#
# print("Your reaction time was {} seconds".format(endTime - startTime))

print("time(): \t\t\t",time.get_clock_info('time'))
print("perf_counter(): \t",time.get_clock_info('perf_counter'))
print("monotonic(): \t\t",time.get_clock_info('monotonic'))
print("process_time(): \t",time.get_clock_info('process_time'))