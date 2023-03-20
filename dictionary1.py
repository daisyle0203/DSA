#  Update / add an element to the dictionary O(1)
myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'
print(myDict)

#  Traverse through a dictionary O(n)
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

#  Searching a dictionary 0(n)
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(myDict, 26))

#  Delete or remove a dictionary element O(1)
myDict.pop('name')

# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}

print(sorted(myDict, key=len))
