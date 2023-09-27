

print(4,8,15,16,23,42,sep=' ',end='\n') #1,1 exercise



print(4,8,15,16,23,42,sep='\n')#1,2 exercise



try:        #1,3 exercise
    m=int(input())

    print(m,m+1,m+2,sep=' ')
except ValueError : 
    print('please try again')




try:        #1,4 exercise
    m1=int(input())
    m2=int(input())
    m3=int(input())
    print(m1+m2+m3)
except ValueError : 
    print('please try again')



try:      #1,5 exercise
    num=int(input())   
    print("Volume = ",num*num*num)
    print('Volume = ',num*num*6)
except ValueError :
    print('please try again')



try:        #2,1 exercise
    N = int(input("Enter the number of schoolchildren: "))  
    K = int(input("Enter the number of tangerines: "))

    whole_tangerines_per_student = K // N
    remainder_tangerines = K % N
    print("Each student will get", whole_tangerines_per_student, "whole tangerines.")
    print("There will be", remainder_tangerines, "whole tangerines remaining in the basket.")
except ValueError :
    print('please try again')




try: #2,2 exercise
    number = int(input("Enter a four-digit number: ")) 

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
except ValueError :
    print('please try again')




try:        #2,3 exercise
    total_peop=int(input('total nimber is '))   
    survive=total_peop/2
    print(int(round(survive)),' people survive')
except ValueError :
    print('please try again')




try:                   #2,4 exercise
    num = int(input("Enter a number: "))
    result = num << 1
    if result == 0:
        print("Warning: The result of << is zero.")
    else:
        print("The result of << is ", result)
except ValueError:
    print("Invalid input. Please enter a valid number.")



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
