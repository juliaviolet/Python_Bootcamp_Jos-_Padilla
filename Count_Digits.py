def digits(n):
    count = 0
    if n==0:
        count = 1
        break
    while(n>0):
        count+=1
    return count
print(digits(25))
