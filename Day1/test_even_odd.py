# Write a program to find the number is even or odd

def even_odd(x):  # defining function
    if x % 2 == 0: # condition for even numbers
        print(f"{x} is a even number.")
    else:
        print(f"{x} is a odd number.")

num = int(input("Enter a number to check if it a even or odd: ")) 
# taking input number from user

even_odd(num) # function calling