#Day 53 - Set Operations


#Perform various operations on sets (union, intersection, etc.).

# Define sets
A = {1, 2, 3}
B = {3, 4, 5}
C = {1, 2}
D = {6, 7}

# 1. Union
union = A | B  # or A.union(B)
print("Union of A and B:", union)

# 2. Intersection
intersection = A & B  # or A.intersection(B)
print("Intersection of A and B:", intersection)

# 3. Difference
difference = A - B  # or A.difference(B)
print("Difference (A - B):", difference)

difference_reverse = B - A
print("Difference (B - A):", difference_reverse)

# 4. Symmetric Difference
symmetric_difference = A ^ B  # or A.symmetric_difference(B)
print("Symmetric Difference of A and B:", symmetric_difference)

# 5. Subset and Superset Checks
print("C is a subset of A:", C <= A)  # or C.issubset(A)
print("A is a superset of C:", A >= C)  # or A.issuperset(C)

# 6. Disjoint Sets
print("A and D are disjoint:", A.isdisjoint(D))

# 7. Add and Remove Elements
A.add(6)
print("A after adding 6:", A)

A.remove(3)
print("A after removing 3:", A)

# Safely removing an element
A.discard(10)  # Does nothing if the element doesn't exist
print("A after discarding 10:", A)

# 8. Set Comprehensions
E = {x for x in range(10) if x % 2 == 0}
print("Set of even numbers (0-9):", E)




