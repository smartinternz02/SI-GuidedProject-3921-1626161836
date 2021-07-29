n = int(input("Enter number of elements")) 
listl = [] 
for i in range(0,n) : listl.append(int(input("enter element"))) 
print("ACCESSING THE ELEMENTS IS:") 
 
for i in listl: print(i) 
 
print("Maximum:",max(listl))
print("Minimum:",min(listl)) 
print("Size of the list:",n)
list1.sort() 
print(list1)