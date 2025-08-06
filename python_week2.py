my_list=[]    # create an empty list called my_list

for i in range(10, 50, 10):  # append the values 10, 20, 30, 40 to my list 
    my_list.append(i)
print(my_list)

my_list.insert(1, 15) #insert the value 15 at the second position in the list.
print(my_list)   

my_list.extend([50, 60, 70]) #extend the list with 50, 60, and 70
print(my_list)

my_list.pop()  # delete the last element in the list
print(my_list)

my_list.sort()  # sort the list in ascending order
print(my_list)

print(my_list.index(30))  # print the index of the value 30 in the list