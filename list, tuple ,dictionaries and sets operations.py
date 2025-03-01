a = [10, 20, "GfG", 40, True]
print(a)
print(a[0])  
print(a[1]) 
a = []

# Adding 10 to end of list
a.append(10)  
print("After append(10):", a)  

# Inserting 5 at index 0
a.insert(0, 5)
print("After insert(0, 5):", a) 

# Adding multiple elements  [15, 20, 25] at the end
a.extend([15, 20, 25])  
print("After extend([15, 20, 25]):", a) 

a = ['apple', 'banana', 'cherry']

# Iterating over the list
for item in a:
    print(item)
    
    
t = (1, 2, 3, 4, 5)

# tuples are indexed
print(t[1])
print(t[4])

# tuples contain duplicate elements
t = (1, 2, 3, 4, 2, 3)
print(t)

# updating an element
t[1] = 100
print(t)


t = (10, 5, 20)

print("Value in t[-1] = ", t[-1])
print("Value in t[-2] = ", t[-2])
print("Value in t[-3] = ", t[-3])




d = { "name": "Alice", 1: "Python", (1, 2): [1,2,4] }

# Access using key
print(d["name"])

# Access using get()
print(d.get("name"))  




d = {1: 'Geeks', 2: 'For', 3: 'Geeks', 'age':22}

# Using del to remove an item
del d["age"]
print(d)

# Using pop() to remove an item and return the value
val = d.pop(1)
print(val)

# Using popitem to removes and returns
# the last key-value pair.
key, val = d.popitem()
print(f"Key: {key}, Value: {val}")

# Clear all items from the dictionary
d.clear()
print(d)






A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '|' operator
res1 = A | B
print("using '|':", res1)

# Using union() method
res2 = A.union(B)
print("using union():",res2)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '&' operator
res1 = A & B
print("using '&':",res1)

# Using intersection() method
res2 = A.intersection(B)
print("using intersection():",res2)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Using '^' operator
res1 = A ^ B
print("using '^':", res1)

# Using symmetric_difference() method
res2 = A.symmetric_difference(B)
print("using symmetric_difference():", res2)