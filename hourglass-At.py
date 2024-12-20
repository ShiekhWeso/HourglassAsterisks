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
    
for i in (y):
    for j in (y):
        # at = i % 2 == 0
        if y[j] % 2 == 0:
            y[j] = '@'
        print(y[j],end="")
    print("")   
            
print(y)