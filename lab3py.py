def even_number():          #1 task||only even number before N 
    try:
        n=input('write integer: ')
        num=int(n)
        i=1
        while i<=num:
            if i%2!=0:
                print(i,'\n')
            i=i+1
    except ValueError :
        print('please try again or write "stop" to exit this programm','\n')
        if n=='stop':
            exit()
        return even_number()
    
even_number()


def factorial():        # 2 task ||   math factorial example 4!=24     
    try:
        n=input('write integer: ')
        num=int(n)
        i=1
        fact=1
        while i<=num:
            fact=i*fact
            i+=1
        print ('factorial number is: ',fact)

    except ValueError :
        print('please try again or write "stop" to exit this programm','\n')
        if n=='stop':
            exit()
        return factorial()

factorial()




def search(): #there i need search 42 "3 task"
    try:

        while True:
            n=input('write integer: ')
            num=int(n)
            if num==42:
                break
            else:
                continue
    except ValueError :
        print('please try again or write "stop" to exit this programm','\n')
        if n=='stop':
            exit()
        return search()

search()

     

#4 task||     character counting a letter

def count_a():          
    try:
        word=input('write world: ')
       # check(word)
        num=word.count('a') + word.count('A')
        
        if word.startswith("a")==False:
                print('please try again or write "stop" to exit this programm','\n')
                if word=='stop':
                    exit()
                return count_a()

        print('number "a" letters: ',num)

    except ValueError:
        print("heeeeeee")

count_a()


        # 5 task                              tens + ones
number_str = input("Enter a number: ")
sum_of_digits = 0
for digit_char in number_str:
    if digit_char.isdigit():
        sum_of_digits += int(digit_char)

if digit_char.isdigit():
        print("Sum of digits:", sum_of_digits,'\n')
else:
        print('So you dont write number because of this I dont work :(','\n')



                # 6 task         Fibonacci numbers where print first N numbers
try:
        N = int(input("Enter a positive integer (N): "))
        fibonacci_sequence = []
        a, b = 0, 1

        while N > 0:
                fibonacci_sequence.append(a)
                a, b = b, a + b
                N -= 1

        print("Fibonacci Sequence: " + ", ".join(map(str, fibonacci_sequence)))
except ValueError:
        print('You dont write integer so, this program doesn\'t work \n')



                # 7 task                     reverse word
w=input('Enter word: ')
rev=w[::-1]
print(rev)

# 8 task                         sum of odd numbers 
sum_of_odd=0
while True:
    try:
        a=int(input("Enter numbers: "))
        if a==0:
                break
        if a%2==0:
                continue

        sum_of_odd+=a

    except ValueError:
                break
print("sum od add numbers: ", sum_of_odd)

        # 9 task         guess numbers 
import random
n=random.randint(1,100)
while True:
        try:
                user=input('Try to guess my number ')
                int_user=int(user)
                if n>int_user:
                        print('Too large \n')
                elif n<int_user:
                        print('Too small \n')
                else:
                        print('Right ')
                        break
        except ValueError:
                print('you dont write number because so i dont work :( ')
                if user=='stop':
                        break


                # 10 task polindrom example: civic, radar, level, rotor, kayak, madam, refer
w=input('write words: ')
rev1=w.lower()
print(rev1)
if rev1==rev1[::-1]:
    print('It\'s polindrom word or number \n')
else:
    print('It isn\'t polindrom word or number \n')


                        # 11 task number of power example 2^3=8
try:
    x=input("Enter number x: ")
    y=input("Enter number of power: ")
    x_int=int(x)
    y_int=int(y)
    i=1
    res=x_int
    
    while i<y_int:
            res=res*x_int

            i+=1
    print('Number to the power is: ',res)
except ValueError:
    print("you don't write integer in power so i don't work :( \n")


                # 12 task count prime number             
def is_prime(num):
    if num <=1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes_in_range(N):
    prime_list = []
    num = 1
    while num <= N:
        if is_prime(num):
            prime_list.append(num)
        num += 1
    return prime_list

try:
    N = int(input("Enter positive integer : "))
    if N < 1:
        print("You dont write a positive integer.")
    else:
        prime_numbers = find_primes_in_range(N)
        print(f"Prime numbers from 1 to {N}:")
        for prime in prime_numbers:
            print(prime, end=" ")
except ValueError:
    print("You dont write integer so i dont work :(")


                # 13 task reverse number
try:
        w=input('Enter integer: ')
        rev=w[::-1]
        print(rev)
except ValueError:
        print('You dont write integer')

                # 14 taask output next prime nummber 
def is_prime(num):
    if num <=1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primes(num):
    num += 1
    while True:
        if is_prime(num):
            return num
        num += 1


while True:
        try:
                user= int(input("Enter a number: "))
                if is_prime(user):
                        print(f"{user} is a prime number.")
                        break
                else:
                        next_prime = find_primes(user)
                print(f"{user} is not prime. The next prime number is {next_prime}.")
                break
        except ValueError:
                print("You dont write integer so i dont work :(")

                # 15 task           Caesar Cipher 
def encrypt(text,s):
    result = ""
 
    # traverse text
    for i in range(len(text)):
        char = text[i]
 
        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
 
        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
 
    return result
 
#example  hello with 3 move is khoor
try:
        text = input('Enter word: ')
        s = int(input('Enter number which move: '))
        print ("Text  : " + text)
        print ("Shift : " + str(s))
        print ("Cipher: " + encrypt(text,s))
except ValueError:
     print('You dont follow the instruction ')
