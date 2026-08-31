
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
#Print the set of elements that are present in either set1 or set2 but not both.
set1.update(set2)
print(set1)

#Print all the keys of the dictionary given below.
myDict = {1:'One', 2:'Two', 3:'Three'}
print(myDict.keys())

#We have two sets given below. Print the elements common to both the sets.
set3 = {1, 2, 3, 4, 5}
set4 = {4, 5, 6, 7}
result = set3 & set4
print(result)

#We have a dictionary given below. 

color = {1:'Red', 2:'Orange', 3:'White', 4:'Brown', 5:'Yellow'}
#Delete the item with key '3,' and add an item with key '7' and value 'Black.
color.pop(3)
color.update({7:'Black'})
print(color)


#Merge the two dictionaries given below.
myDict2 = {1:'One', 2:'Two', 3:'Three'}
myDict3 = {4:'Four', 5:'Five', 6:'Six'}
myDict2.update(myDict3)
print(myDict2)

#Remove all the duplicate items from the tuple given below.
myTuple = ('Red', 'Blue', 'Green', 'Red', 'Orange', 'Green')
set5=set()
set5.update(myTuple)
print(set5)

#Print the number and the cube of that number in a dictionary from 0 to 5.
my_dict4={}
for i in range(0,5):
    my_dict4[i]=i**3
    print(my_dict4)
    
    
