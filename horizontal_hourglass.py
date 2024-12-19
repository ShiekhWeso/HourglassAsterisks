# import math
x = int(input("enter your num:"))

while x % 2 == 0:
    x = int(input("plz enter an odd number: "))
    
for i in range (int(x/2)):
    print((1+i)*"*"+(x-2-2*i)*" "+(1+i)*"*")

print("*"*x)

for i in range (int(x/2)-1,-1,-1):
    print((1+i)*"*"+(x-2-2*i)*" "+(1+i)*"*")