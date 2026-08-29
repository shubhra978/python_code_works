def factorial(num):
    if(num==1): #base case
        return 1
    else:
        return num * factorial(num-1) #recursion function call
    
def sum_of_numbers(num):
    if(num==1): #base case
        return 1
    else:
        return num + factorial(num-1) #recursion function call
    
number = 5
print(factorial(number))
print(sum_of_numbers(number))
