x = int(input("enter your num:"))

while x % 2 == 0:
    x = int(input("plz enter an odd number: "))

num_of_rows = int((x+1)/2)

for i in range (num_of_rows):
    print(" "*i,end="")
    print((x - (i*2)) * "*")
    
    #the equation the hour glass asterisks
    # x * "*" - (i * 2) * "*"
    # (x - (i*2)) * "*"

for i in range (num_of_rows-2, -1, -1):
    print(" "*i,end="")
    print((x - (i*2)) * "*")