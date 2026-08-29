#We have a set given below. Find out whether 10 and 7 are present in the given set or not.


set_a={1,8,6,7,2,11,2}
count = 0
for element in set_a:
    if (element == 7) or (element == 10):
        count +=1

if( count > 1 ):
    print(True)
else:
    print(False)


# We have the name and seat numbers of a student given below as two tuples. With this given data, print the students' names and their assigned seat numbers in a single line using the appropriate data type.


student_list = ['Shaun', 'Ron', 'Michael']
roll_no_list = [101, 102, 103]


for item_a,item_b in zip(student_list,roll_no_list):
    print(item_a,":",item_b)
