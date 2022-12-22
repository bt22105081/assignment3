#print the fibonacci series and find its average


def fibbo(x,y,n):
    #l = []
    #summ = 0
    print(x)
    print(y)
    summ = x+y
    #l.append(x)
    #l.append(y)
    for i in range(0,n):
        z = x+y
        print(z)
        summ = summ + z
        #l.append(z)
        x = y
        y = z
    #for j in l:
    #    summ = summ+j
    print("The average of the series = ",summ/(n+2))    
    
    
    
        

nterms = int(input("Enter the  number of terms"))
a = int(input("Enter the  first term"))
b = int(input("Enter the  second term"))

fibbo(a,b,nterms)

        
