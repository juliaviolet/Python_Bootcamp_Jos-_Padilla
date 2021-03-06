def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  if n==0:
    return False
  while n != 1:
    if n%2 !=0:
      return False
    n=n/2
  return True
  # If after dividing by two the number is 1, it's a power of two



print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False
