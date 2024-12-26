import math
x = int(input("enter your num:"))
lines = []

while x % 2 == 0:
    x = int(input("plz enter an odd number: "))
    
for i in range (int(x/2)):
    lines.append(list((1+i)*"*"+(x-2-2*i)*" "+(1+i)*"*"))

lines.append(list("*"*x))

for i in range (int(x/2)-1,-1,-1):
    lines.append(list((1+i)*"*"+(x-2-2*i)*" "+(1+i)*"*"))
    
for (i,line) in enumerate(lines):
    for j in range (x):
        at = (j+i) % 2 == 1
        if line[j] == '*':
            if at:
                line[j] = '@'
        print(line[j],end="")
    print("")