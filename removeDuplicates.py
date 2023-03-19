#Write a function to find the duplicate number on given integer array/list.

#Example

#removeDuplicates([1, 1, 2, 2, 3, 4, 5])

#Output : [1, 2, 3, 4, 5]

def removeDuplicates(myList):
    result = []
    for i in myList:
        if i not in result:
            result.append(i)
    return result

print(removeDuplicates([1, 1, 2, 2, 3, 4, 5]))