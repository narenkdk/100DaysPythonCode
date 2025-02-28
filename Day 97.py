#Day 97: Memory management and garbage collection


#Learn about Python's memory management and garbage collection.


import sys
import gc

# Function to check reference count
def check_ref_count(obj):
    print(f"Reference count of object: {sys.getrefcount(obj)}")

# Demonstrating reference counting
print("\n--- Reference Counting Example ---")
a = [1, 2, 3]
check_ref_count(a)  # Initial reference count

b = a  # Another reference to the same object
check_ref_count(a)  # Reference count increases

del a  # Deleting 'a' does not remove the object since 'b' still refers to it
check_ref_count(b)  # Object is still alive

del b  # Now the object is no longer referenced and will be garbage collected

# Demonstrating cyclic garbage collection
print("\n--- Cyclic Garbage Collection Example ---")
class Node:
    def __init__(self):
        self.reference = self  # Circular reference

def create_cycle():
    obj = Node()
    return obj  # Object goes out of scope but is still referenced by itself

cyclic_obj = create_cycle()
del cyclic_obj  # Object is not collected due to cyclic reference

# Manually trigger garbage collection
gc.collect()
print("Garbage collection executed.")

# Checking garbage collector status
print("\n--- GC Information ---")
print(f"Garbage Collector Enabled: {gc.isenabled()}")
print(f"Garbage Collector Stats: {gc.get_stats()}")

# Disabling and Enabling Garbage Collector
gc.disable()
print("Garbage Collector Disabled.")

gc.enable()
print("Garbage Collector Enabled Again.")
