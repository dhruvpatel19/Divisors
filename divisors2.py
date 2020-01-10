import math 
  
def primeFactors(n): 
    z = []
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        z.append("2") 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            z.append(i) 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        z.append(n)

    cnt = 1
    set_1 = set(z)
    for element in set_1:
        value = z.count(element)
        cnt = cnt * (value + 1)
    print(cnt)
n = int(input(""))
primeFactors(n)
