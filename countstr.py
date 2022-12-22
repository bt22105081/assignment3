# count the number of occurence of a word or character

s = input("enter the string : ")
ch = input("Enter the word or character :")

if(ch.find(' ') != -1):
    print("enter a single word or letter")
else:
    if(len(ch) == 1):
        print("Number of times letter",ch,"comes = ",s.count(ch))
    elif(len(ch) > 1):
        print("Number of times word ",ch," comes = ",s.count(' '+ch))
    else:
        print("Enter a word or letter")
        
        




