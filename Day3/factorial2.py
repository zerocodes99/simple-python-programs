# write a python program to find the factorial of given number using recursive function

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
input_num = int(input("Enter the number: "))

if input_num < 0:
    print("Factorial of negative number is not defined.")
else:
    result = factorial(num = input_num)
    print(f"Factorial of {input_num} is {result}.")