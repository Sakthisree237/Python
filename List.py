lst1 = [1,2,3,4]
lst2 = [110,435,5,6,7,8]
 #Accesing list element using index
print(lst1[0])

#---------list can be added-----------------
print(lst1+lst2)

#--------list can be multiplied like strings
print(lst2*3)

#---------Function or methods in list--------
#Adding element at end of list
lst1.append(8)

#counting a specific element in list
print(lst1.count(1))

#return the index of first accurance of element
print(lst1.index(8))

#Insert element at specific postion
lst1.insert(0,9)

#will remove first occurance
lst1.remove(1)

#remove at specific index
lst1.pop(3)

#funciton to return length if list
print(len(lst1))

#sort list element
print(sorted(lst2))

#return minimum element
print(min(lst1))

#return maximim element
print(max(lst1))

#---------------------List comrehension-------------------

lst_com =[i*2 for i in range(8)]
print(lst_com)

#Condtions may also applied
lst_com1=[i for i in range(30) if i%5 ==0 ]
print(lst_com1)

#-----------------List slicing----------------------------
print(lst_com[1:3])

print(lst_com[3:])

print(lst_com[:4])

print(lst_com[::-1])

print(lst_com[1:4:2])





