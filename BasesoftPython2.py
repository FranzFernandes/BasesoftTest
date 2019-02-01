'''
Your company uses drones to deliver goods to your clients. Every time a drone goes out for
delivery it is given a unique ID. The ID is a positive int. This ID gets added to a list. When the
drone returns to base the it's ID is added to the same list.
There are 50 drones, and one day only 49 are reported back. We need to find which drone (ID)
is missing.
Your function will be provided with the list of IDs. These IDs aren't in a specific order. We
expect the function to return the ID of the missing drone.
Hint, use bitwise operators; can be done in one loop.
'''

import random

def createRandomArray():
  #creates a random list of size 50 of unique numbers ranging van 0 to 99 
  randomList = random.sample(range(0,100), 50)
  for drone in range(0,49):
    #doubles all unique numbers except 1
    randomList.append(randomList[drone])

  # to check if the unique number is the actual unique number
  print("Unique number is: " + str(randomList[49]))
  #just to make this more "realistic"
  #random.shuffle(randomList)
  return randomList

def findMissingId(randomArray):
  result = 0
  for ID in randomArray:
    result = result ^ ID
  return result



print(findMissingId(createRandomArray()))