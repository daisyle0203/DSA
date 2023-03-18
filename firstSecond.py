#Given a list, write a function to get first, second best scores from the list.
#List may contain duplicates.

#Example

myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
# firstSecond(myList) # 90 87

def firstSecond(myList):
    # myList.sort()
    # first = myList[-1]
    # second = myList[-2]
    # return first, second
    a = myList   #make a copy
 
    a.sort(reverse=True)
 
    print(a)
 
    first = a[0]
 
    second = None
 
    for element in myList:
 
        if element != first:
 
            second = element
 
            return first, second

print(firstSecond(myList))