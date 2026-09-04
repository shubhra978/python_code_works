# Square numbers  
my_list=[1, 2, 3, 4]

def square(p_x):
    return p_x*p_x


result = list(map(square,my_list)) #map each element from list  and square it after calling square function
print(result)

#Convert strings to uppercase 

fruit_list = ["apple", "banana", "cherry"]

def to_upper(p_x):
    return p_x.upper()

upper_result = list(map(to_upper,fruit_list)) #map each element from list  and use upper function defined 
print(upper_result)


#Extract lengths of words  

words = ["python", "map", "reduce"]

def word_length(p_x):
    return len(p_x)

result_length = list(map(word_length,words)) #map each element from list  and use word_length function defined
print(result_length)


#Add tax to prices

capital = [100, 200, 300]

def tax_cal(p_x):
    p_x= round(((p_x*10)/100),0)
    return p_x
result_tax = list(map(tax_cal,capital)) #map each element from list and use word_length function defined
print(result_tax)
