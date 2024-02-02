from array import *

# You van use various import functions:
# import array as arr
# from array import *

# you can use array.array() or arr.array
vals = array('i', [5, 9, 8, 4, 2])
vals.reverse()
print(vals.buffer_info())
print(vals[0])

# loop
for i in range(5):
    print(vals[i])

for i in range(len(vals)):
    print(vals[i])

for e in vals:
    print(e)

# to create a new array with same values
newArr = array(vals.typecode, (a for a in vals))

for e in newArr:
    print(e)

#to assign square root, type a*a in the brackets above.