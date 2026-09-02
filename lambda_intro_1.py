result = lambda my_num : my_num*my_num 

print(result(7))

new_result = lambda a, b: a * b

print(new_result(7,8))



names = ["alice", "bob", "charlie"]
Upper_list =  list(map(lambda n : n.upper(),names))

print(Upper_list)


sorted_list = sorted(names,key=lambda sizecheck: len(sizecheck))
print(sorted_list)
