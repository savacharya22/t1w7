def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            print("not a prime")
            break
    else:
        print("is prime")
 
is_prime(10)           