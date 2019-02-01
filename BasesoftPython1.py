'''
Write a function which accepts a list of integers and returns a list of the products of those
numbers except the one at its own index.
Example, the following:
[9, 3, 6, 2]
should return:
[36, 108, 54, 162]
because:
[3*6*2, 9*6*2, 9*3*2, 9*3*6]
'''

# Array that we want the product of all the other integers
arr = [9, 3, 6, 2]

# function that returns the product of all the other integers per index.
# takes a list of integers as argument


def productOfList(arr):
    # result list
    result = []
    # loops over each item in the list. Removes that item in a temporary list to return the product of all other integers on that location.
    for item in arr:
        tempArr = arr[:]
        tempArr.remove(item)
        result.insert(0 + len(result), calcProduct(tempArr))

    return result

# function that calculates the product of all the integers in a list
# expects an array of all integers


def calcProduct(array):
    result = 1
    for x in array:
        result *= x
    return result


print productOfList(arr)
