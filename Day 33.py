#Day 33 - File operations: Write

#Write data to a text file.

# Data to write
data = """This is the first line of the text file.
This is the second line.
And this is the third."""

# File path and name
file_name = "example.txt"

# Writing to the file
with open(file_name, "w") as file:
    file.write(data)

print(f"Data successfully written to {file_name}")
