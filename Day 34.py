#Day 34 - File operations: Append

#Append data to an existing text file.

# Open the file in append mode
with open('example.txt', 'a') as file:
    # Write new data to the file
    file.write('This is the new data being appended.\n')
    file.write('You can add as many lines as needed.\n')

print("Data has been appended to the file.")
