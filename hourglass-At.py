import math
x = int(input("enter your num:"))
y = []

while x % 2 == 0:
    x = int(input("plz enter an odd number: "))

num_of_rows = int((x+1)/2)

for i in range (num_of_rows):
    print(" "*i,end="")
    y.append(list((x - (i*2)) * "*"))
    
    #the equation the hourglass asterisks
    # x * "*" - (i * 2) * "*"
    # (x - (i*2)) * "*"

for i in range (num_of_rows-2, -1, -1):
    print(" "*i,end="")
    y.append(list((x - (i*2)) * "*"))
    
for i in (y):
    for j in (y):
        # at = i % 2 == 0
        if y[j] % 2 == 0:
            y[j] = '@'
        print(y[j],end="")
    print("")   
            
print(y)