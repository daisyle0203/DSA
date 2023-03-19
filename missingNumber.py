# Write a function to find the missing number in a given integer array of 1 to 100.

# Example

# missingNumber([1, 2, 3, 4, 6], 6) # 5

def missingNumber(myList, totalCount):
    for i in myList:
        if myList[i + 1] - myList[i] != 1:
            return myList[i] + 1


print(missingNumber([1, 2, 3, 4, 6], 6))
