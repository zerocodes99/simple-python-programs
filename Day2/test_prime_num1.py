# program to check the number is prime or not.

def prime_checker(num):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False

    if is_prime == False:
        print(f"{num} is not a prime number.")
    else:
        print(f"{num} is a prime number.")

input_num = int(input("Enter a number to check: "))

prime_checker(num = input_num)