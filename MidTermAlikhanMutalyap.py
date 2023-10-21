try:        #User input, code output 
    user_name=input('Enter your name please: ')
    salary=input('Enter your desired salary level: ')
    level=int(salary)
    tax=int(level*0.2)
    print(f'{user_name}, the tax level you will pay with the salary {level} is {tax}')
except ValueError:
    print('You wrong write your salary ')    













def addition(num1, num2):      # Using arithmetic, bitwise and logic ops 
    return int(num1 + num2)

def multiplication(num1, num2):
    return int(num1 * num2)

b='please write anither second number'
# c=0
def square (num1, num2):
  
   try:
       #c=lambda x: num1**num2
       return num1 ** (1/num2)
       #return c
   except ZeroDivisionError:
       
       return b


# Function to perform division
def division(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2
result= None

try:
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))

    operation = input("Please chose the task you want to perform:'\n' 1.Addition'\n' 2.Multiplication '\n' 3.Division '\n' 4.Exponentiation '\n' Number 1 is subcortical number and Number 2 is root indicator: ")

    if operation == '1':
        result = addition(num1, num2)
    elif operation == '2':
        result = multiplication(num1, num2)
    elif operation == '3':
        result = division(num1, num2)
    elif operation == '4':
        result = square(num1,num2)  
    else:
        result = "Invalid operation choice"

    print("Result: ", result)

except ValueError:
    print("Invalid input. Please enter valid numbers.")










try:        #  Loops and iterations 
        N = int(input("Enter a positive integer (N): "))
        fibonacci_sequence = []
        a, b = 1, 1
        while N > 0:
                fibonacci_sequence.append(a)
                a, b = b, a + b
                N -= 1
        print("Fibonacci Sequence: " + ", ".join(map(str, fibonacci_sequence)))
except ValueError:
        print('You dont write integer so, this program doesn\'t work \n')










from itertools import groupby
def main():
    unique_items = set()
    non_unique_items = {}
    x=[]
    while True:
        print("Please choose the task you want to perform:")
        print("1. Enter items")
        print("2. Exit")
        
        choice = input()
        
        if choice == '1':
            items_input = input("Please enter items separated by comma: ").lower()
            items = [item.strip() for item in items_input.split(',')]
            x=items_input.split(',')
            new_x = [el for el, _ in groupby(x)]
            for item in items:
                if item in unique_items:
                    non_unique_items[item] = non_unique_items.get(item, 0) + 2
                    
                else:
                    unique_items.add(item)
            

            unique_items = "{" + ", ".join(unique_items) + "}"
            non_unique_items = tuple((key, value) for key, value in non_unique_items.items())
            print(new_x)
            print("Unique items:", unique_items)
            print("Not unique items:", non_unique_items)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please choose again.")
    
main()






def main():
    todo_list = []
    completed_tasks = set()

    while True:
        print("Please choose the task you want to perform:")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. Mark Task as Completed")
        print("4. View All Completed Tasks")
        print("5. Exit")

        choice = input()

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.append(task)
            print(f'The task "{task}" was added to the todo list.')

        elif choice == '2':
            print("All Tasks:")
            for i, task in enumerate(todo_list, 1):
                print(f"{i}. {task}")

        elif choice == '3':
            task = input("Enter the name of the task: ")
            if task in todo_list:
                todo_list.remove(task)
                completed_tasks.add(task)
                print(f'The task "{task}" is marked as completed.')
            else:
                print(f'The task "{task}" was not found in the todo list.')

        elif choice == '4':
            print("Completed Tasks:")
            for i, task in enumerate(completed_tasks, 1):
                print(f"{i}. {task}")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please choose again.")


main()
