'''
Write a function that returns a boolean to indicate whether or not any permutation of the
supplied string is a palindrome.
This means the following should apply:
"racecar" should return True
"acrearc" should return True*
"ratecat" should return False
"caretat" should return False
'''

'''
This solution adds every character to a set from the startinglist. If the character is already present in the set,
the character gets removed from the set. When the startingList has been fully traversed, this function checks
how big the checklist is. Based on the parity of the length of the startinglist, if the checklist only has zero or one
characters left over, returns True or False.
'''

def checkPalindrome(text):
    if len(text) <= 1:
        return False
    startingList = list(text.upper())
    checkList = set()

    # Iterate over the list and add or remove based on existence in checklist
    for item in startingList:
        if(item in checkList):
            checkList.remove(item)
        else:
            checkList.add(item)
        print(checkList)

    # check palindrome based on parity
    if len(checkList) == 1 and (len(startingList) % 2 == 1):
        return True
    elif(len(checkList) == 0):
        return True
    else:
        return False


print(checkPalindrome("retteketter"))
