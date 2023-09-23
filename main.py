# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print(4,8,15,16,23,42,sep=' ',end='\n') #1,1 exercise

print(4,8,15,16,23,42,sep='\n')#1,2 exercise
m=int(input())

print(m,m+1,m+2,sep=' ')#1,3 exercise
try:
    m1=int(input())#1,4 exercise
    m2=int(input())
    m3=int(input())
    print(m1+m2+m3)
exeption:ValueError:    print('please try again)
try:     num=int(input())    #1,5 exercise
print("Volume = ",num*num*num)
print('Volume = ',num*num*6)
exeption:ValueError
N = int(input("Enter the number of schoolchildren: "))  #2,1 exercise
K = int(input("Enter the number of tangerines: "))

whole_tangerines_per_student = K // N
remainder_tangerines = K % N
print("Each student will get", whole_tangerines_per_student, "whole tangerines.")
print("There will be", remainder_tangerines, "whole tangerines remaining in the basket.")


number = int(input("Enter a four-digit number: ")) #2,2 exercise


if 1000 <= number <= 9999:
    # Extract individual digits
    thousands_digit = number // 1000
    hundreds_digit = (number // 100) % 10
    tens_digit = (number // 10) % 10
    ones_digit = number % 10


    print("Thousands digit:", thousands_digit)
    print("Hundreds digit:", hundreds_digit)
    print("Tens digit:", tens_digit)
    print("Ones digit:", ones_digit)
else:
    print("Please enter a valid four-digit number.")

total_peop=int(input('total nimber is '))   #2,3 exercise
survive=total_peop/2
print(int(round(survive)),' people survive')

try:                                         #2,4 exercise
    num = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()


result = num << 1


if result == 0:
    print("Warning: The result of << is zero.")
else:
    print("The result of << is ", result)





#2,5 exercise
def addition(num1, num2):
    return num1 + num2

# Function to perform subtraction
def subtraction(num1, num2):
    return num1 - num2

# Function to perform multiplication
def multiplication(num1, num2):
    return num1 * num2

# Function to perform division
def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

try:
    # Prompt the user to enter two numbers
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    # Prompt the user to choose an operation
    operation = input("Please choose the operation (+, -, *, /): ")

    # Perform the selected operation based on user input
    if operation == '+':
        result = addition(num1, num2)
    elif operation == '-':
        result = subtraction(num1, num2)
    elif operation == '*':
        result = multiplication(num1, num2)
    elif operation == '/':
        result = division(num1, num2)
    else:
        result = "Invalid operation choice"

    # Display the result or an error message
    print("Result: ", round(result,3))

except ValueError:
    print("Invalid input. Please enter valid numbers.")