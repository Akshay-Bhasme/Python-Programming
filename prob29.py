#Problem: Write a program to print out a set containing all the colors from list1 which
# are not present in list2.
list1=['White','Black','Red']
list2=['Red','Green']
lst=[]
for i in list1:
    for j in range(len(list2)):
        if i== list2[j]:
            break
    else:
        lst.append(i)
print(set(lst))

#Or
list3=set(list1)
list4=set(list2)
print(list3.difference(list4))

