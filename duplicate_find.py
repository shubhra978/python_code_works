def contains_duplicate(input)-> bool:
  has_set = set()
  for i in input:
    has_set.add(i)
  
  set_length = len(has_set)
  if set_length != len(input):
    return True
  return False
