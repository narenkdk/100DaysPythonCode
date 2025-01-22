#Day 60: Tower of Hanoi


#Solve the Tower of Hanoi problem.

def tower_of_hanoi(n, source, destinatio, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destinatio}")
        return
    
    tower_of_hanoi(n-1, source, auxiliary, destinatio)#step 1
    print(f"Move disk {n} from {source} to {destinatio}")#step 2    
    tower_of_hanoi(n-1, auxiliary, destinatio, source)#step 3   


# Example usage
n = 3 #number of disks
tower_of_hanoi(n, 'A', 'C', 'B') #A is the source, C is the destination, B is the auxiliary

#Output:
#Move disk 1 from A to C
#Move disk 2 from A to B
#Move disk 1 from C to B
#Move disk 3 from A to C
#Move disk 1 from B to A
#Move disk 2 from B to C
#Move disk 1 from A to C