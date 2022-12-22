# python program to make list of tuple

l = []
while True:
    n = int(input("Enter number : "))
    l.append(n)
    ch = input("Do you want to continue press enter for yes and n for no ")
    if(ch == ''):
        continue
    elif(ch =='n'or ch =='N'):
        break
    else:
        print("Wrong choice")

l1 = []


for a in l:
    l1.append((a,a**2))

print(l1)    
