def sum_divisors(n):
  sum = 0
  i=1
  # Return the sum of all divisors of n, not including n

  while n%i==0:
    sum = sum + i
    i+=1
    if n%i!=0:
      i+=1
  return sum


print(sum_divisors(6)) # Should be 6 (sum of 1+2+3)
print(sum_divisors(12)) # Should be 16 (sum of 1+2+3+4+6)

def sum_div(number):
    divisors = [0]
    for i in range(1, number):
        if (number%i)==0:
            divisors.append(i)
    return sum(divisors)
print(sum_div(6))
print(sum_div(12))
print(sum_div(0))
