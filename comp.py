largest = None
print ("Before!!!")

for value in [9,5,41,74,9,84,3]:
    if largest is None:
        largest = value
    elif largest<value:
        largest = value
print("Largest value",largest)
     
