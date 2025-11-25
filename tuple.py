# Q1: Print all elements of a tuple
t1 = (10, 20, 30, 40)
for x in t1:
    print(x)
# q2: print all elements of a tuple using while loop
t1 = (5, 10, 15, 20)
i = 0
while i < len(t1):
    print(t1[i])
    i += 1
 #Q3: Print first 3 elements using slicing
t1 = (1, 2, 3, 4, 5)
print(t1[:3])
 #Q4: Print last 3 elements using slicing
t1 = (10, 20, 30, 40, 50, 60)
print(t1[-3:])
#Q5: Check if an element exists in tuple
t1 = (10, 20, 30, 40)
if 20 in t1:
    print("Present")
else:
    print("Not Present")
#Q6: Count how many times a value appears
t1 = (1, 2, 2, 3, 2, 4)
print(t1.count(2))

#Q7: Find the index of an element
t1 = (5, 10, 15, 20)
print(t1.index(15))
 #Q8: Reverse the tuple using slicing
t1 = (1, 2, 3, 4)
print(t1[::-1])
#Q9: Print only even elements
t1 = (1, 2, 3, 4, 5, 6)

for x in t1:
    if x % 2 == 0:
        print(x)
 #Q10: Create a new tuple of first 4 elements
t1 = (10, 20, 30, 40, 50, 60)
t2 = t1[:4]
print(t2)
