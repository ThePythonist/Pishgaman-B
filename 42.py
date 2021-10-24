# n = int(input("Enter any number : "))
# prime_status = False
# divisors = [ i for i in range(1,n+1) if n % i == 0 ]
#
# if len(divisors) == 2 :
#     print("Prime")
# else :
#     print("Not Prime")

n = int(input("Enter any number : "))
prime_status = False
divisors = [ i for i in range(1,n+1) if n % i == 0 ]

if len(divisors) == 2 :
    prime_status = True

print(prime_status)
