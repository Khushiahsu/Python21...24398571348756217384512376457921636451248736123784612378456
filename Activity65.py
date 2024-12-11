#Write a program to perform the following operations: 1. Create a tuple with different datatypes 2. Create another tuple of integers 3. Create a new tuple by adding 9 to the previous tuple 4. Count the occurrences of an element in the tuple 5. Perform slicing on the tuple?

tuple1 = (3.5,'apple',55,True) 
print(tuple1)

tuple2 = (3)
print(tuple2)
tuple2 = tuple2 + (9)
print(tuple2)
tuple4 = (2,1,3,4,5,6,6,5)
print(tuple4.count(5))
tuple5 = (8,3,7,5,4,29)
print((tuple5[0:5]))
