from array import *

arr = array('i', [])

n = int(input("Enter the length of the array"))

for i in range(n):
    x = int(input("Enter the next value"))
    arr.append(x)

print(arr)
# every time a user enters a value we can append it to the array


val = int(input("Enter the value for search"))

k = 0
for e in arr:
    if e == val:
        print(k)
        break

print(arr.index(val))
