from numpy import *

arr1 = array([[1, 2], [4, 5]])
arr2 = array([[1, 2], [3, 4]])

arr1shape = array(arr1.shape)
arr2shape = array(arr2.shape)

print(arr1)
print("+")
print(arr2)
print("=")


ansrow = arr2shape[0]
anscol = arr1shape[1]

ansarr = ones((ansrow, anscol))

for i in range(ansrow):
    for j in range(anscol):
        ans = 0
        for q in range(ansrow):
            ans += arr1[i][q] * arr2[q][j]

        ansarr[i][j] = ans


print(ansarr)

