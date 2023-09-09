# write a python program to find the factorial of given number

def factorial(num):
    result = 1 # to store factorial value
    if num < 0:
        print("Factorial of negative number is not defined.")
    elif num == 0 or num == 1:
        print(f"Factorial of {num} is 1.")
    else:
        for i in range(2, num+1): # 1 is skipped because any number multiplied by 1 is the number
            # and (num+1) is because we want to include the number
            result *= i
        print(f"Factorial of {num} is {result}.")

input_num = int(input("Enter the number: "))

factorial(num = input_num)