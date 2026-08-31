s="IV"

my_string =str(s.split())

my_dict={'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

size = len(my_dict)-1

result =0

for items in my_dict: #iterating through items in dictionary
    for roman_alphabet in my_string:  #iterating through defined string in dictionary
        if roman_alphabet == items: 
           result = result + my_dict[items]
print(result)     
