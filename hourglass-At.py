x = int(input("Enter your num:"))
y = []

while x % 2 == 0:
    x = int(input("Please enter an odd number: "))

num_of_rows = int((x+1)/2)

# Construct the top half of the hourglass
for i in range (num_of_rows):
    line = " " * i + (x - (i * 2)) * "*"
    y.append(line)
    print(line)
    
# Construct the bottom half of the hourglass
for i in range(num_of_rows - 2, -1, -1):
    line = " " * i + (x - (i * 2)) * "*"
    y.append(line)
    print(line)
    
    #the equation the hourglass asterisks
    # x * "*" - (i * 2) * "*"
    # (x - (i*2)) * "*"
    
# Modify the asterisks
for i in range(len(y)):
    line_list = list(y[i])  # Convert the string to a list
    for j in range(len(line_list)):
        at = (j + i) % 2 == 1
        if line_list[j] == '*':
            if at:
                line_list[j] = '@'
    y[i] = ''.join(line_list)  # Convert the list back to a string
            
# Print the result
print("\nFinal Pattern:")
for line in y:
    print(line)