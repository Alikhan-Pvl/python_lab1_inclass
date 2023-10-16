

word=tuple(input('Enter word: ')   )   #1.1 task
print(word)

word=input('Enter word: ')      #1.2 task
a = tuple(word)
print(a)
a=''.join(a)
print(a)



try:                      #1.3 task
    list_elem=[]        # for tuple A
    while True:
        element=input('Enter numbers for tuple A: ')
        if element=='q':
            break
        int_ele=int(element)
        list_elem.append(int_ele)
    tpl=tuple(list_elem)
    print(tpl,'tuple A')               #there finished tuple A


    list_elem2=[]           #for tuple B 
    while True:
        element2=input('Enter numbers for tuple B: ')
        if element2=='q':
            break
        int_ele2=int(element2)
        list_elem2.append(int_ele2)

    tpl2=tuple(list_elem2)
    print(tpl2,'tuple B' )            #there finished tuple B 

    half_list_elem=round(len(list_elem)/2)
    result_list=list_elem[:half_list_elem]+list_elem2[half_list_elem:]
    tpl_res=tuple(result_list)
    print(tpl_res)

except ValueError:
    print('You dont write integers')



def count_occurrences(input_tuple):     #1.4 task
    element_counts = {}
    print(element_counts,'heeeeee')
    for item in input_tuple:
        print(item)
        if item in element_counts:
            element_counts[item] += 1
        else:
            element_counts[item] = 1
    print(element_counts,'dddddddddddd')
    result_tuple = tuple((key, value) for key, value in element_counts.items())
    return result_tuple

user_input = input("Введите элементы кортежа через запятую: ")
user_input = eval(user_input)  # Преобразуем строку в кортеж, предполагая, что пользователь введет корректный кортеж

result = count_occurrences(user_input)
print("Elements and their occurrences:")
print(result)


integers = ()           #1.5 task
floats = ()
strings = ()

# Просим пользователя вводить элементы
user_input = input("Введите элементы через запятую: ")
elements = user_input.split(", ")

for element in elements:
    if element.isdigit():
        integers += (int(element),)
    elif "." in element and all(part.isdigit() for part in element.split(".")): # for float
        floats += (float(element),)
    else:
        strings += (element,)

print("Кортеж целых чисел:", integers)
print("Кортеж чисел с плавающей запятой:", floats)
print("Кортеж строк:", strings)


user_input = input("Enter a string without whitespaces: ")        #2.1

result_set = {char for char in user_input}

print("Created set is:")
print(result_set)




try:        #2.2 task
    input_A = input("Enter element A throw comma: ")
    input_B = input("Enter element B throw comma: ")

    set_A = set(map(int, input_A.split(',')))
    set_B = set(map(int, input_B.split(',')))

    difference_set_A = set_A - set_B
    difference_set_B = set_B - set_A

    result_set = difference_set_A.union(difference_set_B)

    print("Different between A and B:")
    print(result_set)
except ValueError:
    print('you dont write integers')



try:            #2.3 task
    input_A = input("Enter element A throw comma: ")
    input_B = input("Enter element B throw comma: ")

    set_A = set(map(int, input_A.split(',')))
    set_B = set(map(int, input_B.split(',')))


    set_A = set_B-set_A

    print("The result after removing elements from A that are also in B:")
    print(sorted(set_A))
except ValueError:
    print('you dont write integers')




try:        #2.4
    input_A = input("Enter element A throw comma: ")
    input_B = input("Enter element B throw comma: ")
    input_C = input("Enter element C throw comma: ")


    set_A = set(map(int, input_A.split(',')))
    set_B = set(map(int, input_B.split(',')))
    set_C = set(map(int, input_C.split(',')))

# Найдите элементы, которые присутствуют и в set_A, и в set_C
    common_elements = set_A.intersection(set_C)

# Удалите эти элементы из set_A и добавьте их в set_B
    set_A -= common_elements
    set_B |= common_elements


    updated_set_C = set_C | set_A  # union set_C и set_A
    print("update set_C:")
    print(updated_set_C)
except ValueError:
    print('you dont write integers')




from itertools import combinations      #2.5 task
try:
    input_A = input("Enter element A throw comma: ")
    n = int(input("Enter lenth n: "))
    m = int(input("Enter lenth m: "))

    A = set(map(int,input_A.split(',')))

    if m > len(A):      # check about m noy bigger generation A size n 
        print("Error: m cannot be greater than the number of combinations of A of size n")
    else:

        combinations_list = list(combinations(A, n))    # generation combination 
        result_list = [set(combination) for combination in combinations_list[:m]]


    print(result_list)
except ValueError:
    print('you dont write integers')




from itertools import groupby       #3 task

cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'),
             ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

# Sort the list by manufacturer (the first element of each tuple)
sorted_cars = sorted(cars_list, key=lambda car: car[0])

# Group the cars by manufacturer
grouped_cars = groupby(sorted_cars, key=lambda car: car[0])

# Iterate through the grouped data and print the table output
for manufacturer, models in grouped_cars:
    models_list = list(models)
    count = len(models_list)
    print(models_list)
    print(f"{manufacturer} {count}")
    

    for model in models_list:
        print(f"- {model[1]}")

