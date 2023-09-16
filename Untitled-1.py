print ("hello world")

num=9
float_num=9.1
print(num, float_num,sep='\t')
a=19
b=19.00
print('a= '+str(a))
print('b= '+str(b))

var_int=42
var_flt=42.0
print(var_int,'\n')
print(var_flt,'\n')

name = input('Enter your name plese: ')
print('The name is ' + name,'\n')

name = 'C3PO'
age = 112
print(f"Salem, My name is {name} and I'm {age} years old.")



try:
    num = int(input("Enter a number: "))
    result = 10 / num   
    print("Result:", result,'\n')
except:
    print("Division by zero is not allowed.",'\n')

try:
    num2 = int(input("Enter a number: "))
    result2 = 10 / num2
    print("Result:", result2,'\n')
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.",'\n')