def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      factor+=1
      # If it's not, increment the factor by one
      ___
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5

