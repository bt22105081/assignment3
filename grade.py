# print grade and respective remark to it

def grade(p):
    if(p ==4):
        g ='D'
        r = "poor"
    elif(p==5):
            g = 'C'
            r = "Below average"
    elif(p==6):
            g = "C+"
            r = "Average"
    elif(p==7):
            g = 'B'
            r = "Good"
    elif(p==8):
            g = "B+"
            r = "Very Good"
    elif(p==9):
            g = 'A'
            r = "Excellent"
    elif(p==10):
            g = "A+"
            r = "Outstanding"
    else:
            print("*")
    print("Your Grade is ",g," and ",r,"Performance")
                
            
        

pts = int(input("Enter your Grade points: "))
if(not(pts>=4 and pts<=10)):
    print("Invalid input/points")
else:
    grade(pts)
    
