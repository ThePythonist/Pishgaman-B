def is_prime(n):
    # divisors = []
    # for i in range(1,n+1):
    #     if n%i == 0 :
    #         divisors.append(i)
    #
    # print(divisors)

    # if len(divisors) == 2 :
    #     return True
    # else :
    #     return False
    #
    divisors = [ i for i in range(1,n+1) if n%i == 0 ]
    return True if len(divisors) == 2 else False

print(is_prime(int(input("Enter any number : "))))
