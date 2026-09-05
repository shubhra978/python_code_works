def longest_consecutive(nums):
  nums.sort()
  new_list =[]
  element=nums[0]
  size = len(nums)
  for item in nums:
    if element == item:
      new_list.append(item)
      element+=1
    else:
      element+=0
  return(len(new_list))
 
my_list = [100,2,100,200,3,4,5]
result = longest_consecutive(my_list)
print(result)
