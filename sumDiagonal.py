#Given 2D list calculate the sum of diagonal elements.

# Example

myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
def sumDiagonal(myList2D):
    sum = 0
    for i in range(len(myList2D)):
        sum += myList2D[i][i] 
    return sum

print(sumDiagonal(myList2D))# 15