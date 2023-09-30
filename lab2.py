

def four_digit():            #1 exercise 
    
    try:           
        num=input('please write 4 digit number where 1 + 4 numbers  = difference between the second and third digits: ')
        n=int(num)
        if 1000 <= n <= 9999:
    # Extract individual digits
            thousands_digit = n // 1000
            hundreds_digit = (n // 100) % 10
            tens_digit = (n // 10) % 10
            ones_digit = n % 10
            if hundreds_digit - tens_digit < 0:
                difference=(hundreds_digit - tens_digit)*-1
            else :
                difference = hundreds_digit - tens_digit


            if thousands_digit + ones_digit ==difference:
                print("Yes",'\n')
            else: 
                print ("No",'\n')
        else:
            print('please write 4 digit number or write "stop" to exit this programm ','\n')
            return four_digit()
    except :
        print('please try again or write "stop" to exit this programm ','\n')  
        if str(num) == 'stop':
            return  
        else:  
            return four_digit()

try:            #there i call four_digit function 
    a=four_digit()
except:
    print()



def Roskomnadzor():      #2 exercise 
    try:            
        age=input("please take your age: ")
        numAge=int(age)
        if numAge<0:
              print('dont play this programm','\n')
        elif numAge>=18:
            print("Access is allowed",'\n')
        else:
            print("Access denied",'\n')
    except ValueError :
        print('please try again or write "stop" to exit this programm ','\n')
        if age=='stop':
            exit()
        return Roskomnadzor()


try:            #there i call Roskomnadzor function about age
    a=Roskomnadzor()
except:
    print()




def ArithmeticProgress():            #3 exercise
    try:                 
        num1=input("please take your number: ")
        first=int(num1)
        num2=int(input("please take your number: "))

        num3=int(input("please take your number: "))

       
        if num2-first == num3-num2:
            print("YES",'\n')
        else:
            print("NO",'\n')
    except ValueError :
        print('please try again or write "stop" to exit this programm ','\n')
        if num1=='stop':
            exit() 
        return ArithmeticProgress()

try:            #there i call ArithmeticProgress function 
    a=ArithmeticProgress()
except:
    print()




def Rook():              #4 exercise 
    try:            

        row=input("write where stay rook row: ")
        rowINT=int(row)
        column=int(input("write where stay rook column: "))

        if rowINT>=8 and column>=8:
            print('please write real coordinates and try again or write "stop" to exit this programm','\n' )
            return Rook()
        else:
            num1=int(input("write where rook go in row: "))
            num2=int(input("write where rook go in column: "))
            if num1<=8 and num2<=8:
                if num1==rowINT or num2==column:
                    print("YES",'\n')
                else:
                    print("NO",'\n')
            else:
                print('please write real coordinates and try again or write "stop" to exit this programm','\n' ) 
                return Rook()

    except ValueError :
        print('please try again or write "stop" to exit this programm ','\n')
        if row=='stop':
            exit() 
        return Rook()

try:            #there i call Rook function 
    a=Rook()
except:
    print()



def King():          #5 exercise
    try:       

        row=input("write where stay king row: ")
        rowINT=int(row)
        column=int(input("write where stay king column: "))

        if rowINT>=8 and column>=8:
            print('please write real coordinates and try again or write "stop" to exit this programm','\n' )
            return King()
        else:
            num1=int(input("write where king go in row: "))
            num2=int(input("write where king go in column: "))

            if num1>rowINT+1 or num2>column+1:
                print('NO','\n')
            else:
                print('YES','\n')

    except ValueError :
        print('please try again or write "stop" to exit this programm','\n')
        if row=='stop':
            exit()
        return King()

try:            #there i call King function 
    a=King()
except:
    print()



def avarage():      #avarage number in sort     6 exercise
    try:
        num1=input('write first number:')
        numInt=int(num1)
        num2=int(input('write second number:'))
        num3=int(input('write third number: '))
        
        num_sort=[numInt,num2,num3]
        num_sort.sort()

        print(num_sort[1])

    except:
        print('Please write numbers and try again or write "stop" to exit this programm','\n')
        if num1=='stop':
            exit()
        return avarage()

try:            #there i call King function 
    a=avarage()
except:
    print()



def Number_of_days():       #7 exercise
    try:
        a=input('write numbers of mounth: ')
        mounth=int(a)

        if mounth > 12:
            print ('in year have 12 mounth, please write around 1 to 12 and try again or write "stop" to exit this programm' ,'\n')
            return Number_of_days()
        elif mounth==1 or mounth==3 or mounth==5 or mounth==7 or mounth==8 or mounth==10 or mounth==12 :
            print('days in this mounth is 31' ,'\n')
        elif mounth==2:
            print('days in this mounth is 28','\n')
        elif mounth == 4 or mounth==6 or mounth==9 or mounth==11:
            print('days in this mounth is 30','\n')

    except:
        print('Please write numbers of mounth and try again or write "stop" to exit this programm','\n')
        if a=='stop':
            exit()
        return Number_of_days()
    

try:            #there i call Number_of_days function 
    a1=Number_of_days()
except:
    print()



def Weigh():              #8 exercise
    try :
        a=input('Weigh of boxer is: ')
        boxer=int(a)
        if boxer <= 60 :
            print('Light weight','\n')
        elif boxer <= 64:
            print('First welterweight ','\n')
        elif boxer <= 69:
            print('Welterweight ','\n')
        elif boxer <100 :
            print("It's so a lot for boxer, this boxer isn't allowed in the tournament ",'\n')
        else :
            print ("don't play with the program",'\n') 
            return 

    except:
        print('Please write person weigh and try again or write "stop" to exit this programm','\n')
        if a=='stop':
            exit()
        return Weigh()

try:            #there i call Weigh function about age
    a=Weigh()
except:
    print()



def  passord():         #9 exercise
    try:
        first_attempt=str(input("first passord is: "))
        second_attempt=str(input("second passord is: "))

        if first_attempt==second_attempt:
            print("Password accepted",'\n')
        else:
            print("Password not accepted",'\n')

    except:
        print()


try:            #there i call passord function 
    a=passord()
except:
    print()


def even_or_odd():          # 10 exercise 
    try:
        n=input("your number is: ")
        num=int(n)
        if (num%2)==0:
            print('Even value','\n')
        else:
            print('Odd number','\n')

    except:
        print('please write only integers and try again or write "stop" to exit this programm','\n')
        if n=='stop':
            exit()
        return even_or_odd()

try:            #there i call even_or_odd function 
    a=even_or_odd()
except:
    print()



def easy_task():        # 11 exercise 
    try:
        n=input('write your first number: ')
        num1=int(n)
        num2=int(input('write your second number: '))

        if num1>num2:
            print('the smaller number is ',num2,'\n' )
        else:
            print('the smaller number is ',num1,'\n' )

    except:
        print('please write only integers and try again or write "stop" to exit this programm','\n')
        if n=='stop':
            exit()
        return easy_task()

try:            #there i call easy_task function 
    a=easy_task()
except:
    print()


def age_group():            # 12 exercise 
    try:
        n=input('write your age: ')
        age=int(n)
        if age <0:
            print ('dont play this program and try again or write "stop" to exit this programm','\n')
            return age_group()
        elif age<14:
            print('childhood','\n')
        elif age <25:
            print('youth','\n')
        elif age <60:
            print('maturity','\n')
        else:
            print('old age','\n')
    except:
        print('please write your age and try again or write "stop" to exit this programm','\n')
        if n=='stop':
            exit()
        return age_group()
    

try:             #there i call age_group function about age
    a=age_group()
except:
    print()


def Triangle():             # 13 exercise 
    try:
        n=input('first side length: ')
        AB=int(n)
        BC=int(input('second side length: '))
        AC=int(input('third side length: '))
        if AB<0 or BC<0 or AC<0:
            print('Triangle can\'t negative length and try again or write "stop" to exit this programm','\n')
            return Triangle()
        elif AB==BC or BC==AC or AC==AB:
            print ('Isosceles','\n')
        elif AB==BC==AC:
            print ('Equilateral','\n')
        else:
            print ('Versatile','\n')
    except:
        print('please write Triangle lengths and try again or write "stop" to exit this programm','\n')
        if n=='stop':
            exit()
        return Triangle()
    
try:             #there i call Triangle function 
    a=Triangle()
except:
    print()