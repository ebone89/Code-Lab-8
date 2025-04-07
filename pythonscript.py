# Open the file in read mode
filename = "data.txt"
with open(filename, "r") as file:
    # Read all lines from the file
    lines = file.readlines()


#Use strip() to remove any extra lines or whitespace from text file.
name = lines[0].strip()
age = lines[1].strip()
id_number = lines[2].strip()

# Output the variables to the screen.
print("Name:", name)
print("Age:", age)
print("ID#:", id_number)
