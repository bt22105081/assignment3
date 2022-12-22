# Take input of sid and name in a dictonary and display name

ch="Y"
dic={}
dic2={}
#List containing Y or N
liste=["Y","y","n","N"]
while ch=="Y" or ch=="y":
    
    name = str(input("Enter student name:"))
    sid = int(input("Enter student SID:"))
    if sid<0:
        print("\nError\nSID can't be negative\n")
    else:
       
        dic.update({sid: name})
        
        dic2.update({name:sid})
       
        ch = str(input("Enter Y to continue or N to end:"))
    if ch=="N" or ch=="n":
        break
    elif (not (ch in liste)):
        print("\nError\nPlease enter valid input['Y' or 'N']")
        repeat=str(input("\nEnter Y to continue or N to end:"))


#printing the dictionary
print("The Dictionary containing {'SID':'Name'} is shown below")
print(dic)

#sorting according to name
list_k=sorted(dic2)
dic3={}
for ele in list_k:
    dic3.update({dic2.get(ele):ele})
print("The Dictionary after sorting according to name:")
print(dic3)


sort_dic = sorted(dic)
dic4 = {}
for va in sort_dic:
    dic4.update({va: dic.get(va)})
print("The Dictionary after sorting according to SID:")
print(dic4)
# Taking input SID to be searched
enter_sid = int(input("Enter SID to get name of student:"))
# Searching for sid as key in dic
output_name = str(dic.get(enter_sid))
# printing name with key sid
print(f"Name of student with SID {enter_sid} is {output_name}.")
