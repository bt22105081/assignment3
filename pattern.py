# print the pattern

s = input("Enter the string ")



for a in range(len(s),0,-2):
    print("")
    for b in range(len(s),a,-2):
        print('',end=' ')
    for c in range(0,a):
        print(s[c],end='')
        
