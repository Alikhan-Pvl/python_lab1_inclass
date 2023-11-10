
def get_keys_with_value_true(dictator):    #task 1
    answers=[]
    # dict.dictator
    for key, val in dictator.items():
        if val==True:
            answers.append(key)

    return answers


user_input = {} 

while True:
    try:
        key = input("Enter key: ")
        if key=='stop':
            break
        value = input("user : ")
        bool_val= True if value.lower()=='t' else False
        user_input[key]= bool_val
        

    except ValueError:
       print("error!")
       break

print(user_input)
a=get_keys_with_value_true(user_input)
print(a)










from collections import Counter       #task 2

def get_unique_elements(list):
    el_counter=Counter(list)
    dict_el_counter=dict(el_counter)
    new=[]
    for key,val in dict_el_counter.items():
        if dict_el_counter[key]==1:
            new.append(key)

    return new


user_input=input("Enter numbers throw , :") #1, 2, 3, 1, 2, 4
list_user=list(map(int,user_input.split(',')))

print(list_user)
a=get_unique_elements(list_user)
print(a)












def get_date_in_format(date):        #task 3

    if date:
        first_el=date[0]
        end_el=date[-1]
        date[0]=end_el
        date[-1]=first_el
        result='.'.join(date)

    return result


user_input=input('Enter date: ')        #2023.10.23
list_user=list(user_input.split('.'))

print(list_user)
a=get_date_in_format(list_user)

print(a)











from collections import Counter       #task 4
def get_elements_with_no_more_than_two_occurrences(list):
    el_counter=Counter(list)
    dict_el_counter=dict(el_counter)
    new=[]
    for key,val in dict_el_counter.items():
        if dict_el_counter[key]>1:
            new.append(key)

    return new


user_input=input("Enter numbers throw , :") #1, 2, 3, 1, 2, 4
list_user=list(map(int,user_input.split(',')))

print(list_user)
a=get_elements_with_no_more_than_two_occurrences(list_user)
print(a)













def get_words_from_string(string):            #task 5
    list_user_word=list(string.split(' '))

    return list_user_word


user_input=input('Enter words: ')       #This a string with a several words.
a=get_words_from_string(user_input)
print (a)













from collections import Counter 
def get_unique_elements_with_count(list):            #task 6
    el_counter=Counter(list)
    dict_el_counter=dict(el_counter)

    return dict_el_counter



user_input=input('Enter numbers: ')     #1, 2, 3, 1, 2, 4, 1, 2
list_user=list(map(int,user_input.split(', ')))
a=get_unique_elements_with_count(list_user)
print(a)












def get_prime_numbers(n):           #7 task
    list_numbers=[]

    for i in range(2,int(n)+1):
        k=0
        for j in range(1,i+1):
            if i%j==0:
                k+=1
        if k==2:
            list_numbers.append(i)              

    return list_numbers


try:
    user_input=int(input('Enter integers: '))      #100
    a=get_prime_numbers(user_input)
    print(a)         #2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97

except ValueError:
    print('you dont write integers so i dont work')











def get_prime_numbers_in_list(list):          # 8 task
    new_list=[]

    for i in list:
        k=0
        for j in range(1,i+1):
            if i%j==0:
                k+=1
        if k==2:
            new_list.append(i)   
    return new_list

try:
    user_input=input('Enter numbers throw commas: ')        #1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99
    list_of_input=list(map(int, user_input.split(', ')))
    answers=get_prime_numbers_in_list(list_of_input)
    print(answers)

except ValueError:
    print('you dont write integers')











from datetime import datetime
try:
    def get_difference_between_dates(date1, date2):         #9 task
        date1 = datetime.strptime(date1, "%Y.%m.%d")
        date2 = datetime.strptime(date2, "%Y.%m.%d")
        diff=date2-date1
        diff=diff.days
        return diff
except ValueError:
    print('you dont write corect format to date ')


user_input_date1=input('Enter 1 date: ')        #2023.10.23
user_input_date2=input('Enter 2 date: ')        #2023.10.24
answer=get_difference_between_dates(user_input_date1,user_input_date2)
print(answer)
















def get_decimal_number_from_binary_string(binary_string):       #10 task
    decimal=int(binary_string,2)
    return  decimal


user_input_num=input('Enter numbers: ')     #10110011   2**7+2**5+2**4+3=128+32+16+3=179
print(get_decimal_number_from_binary_string(user_input_num))











import math
def is_expression_true(expression):                     #11 task 
    k=0
    num_of_list=list(map(int,expression.split(', ')))
    print(num_of_list)
    for el in num_of_list:
        el=math.isqrt(el) 
        print (el)
        if isinstance(el, int):
            k+=1
    
    if k==len(num_of_list):
        return True
    else:
        return False


try:
    user_input_num=input('Enter numbers throw comma: ')     #4, 16, 25

    print(is_expression_true(user_input_num))
except ValueError:
    print('you dont write integers!!!!')












def sort_key(item):
    return item['price']

def sort_by_price(shopping_list):                           #12 task
    sorted_list=sorted(shopping_list, key=sort_key)

    return sorted_list


general_list=[]
for i in range(3):
    user_input_name=input(f"Enter {i+1} name: ")
    general_list.append(user_input_name)
    try:
        user_orice=int(input(f"Enter {i+1} price: "))
    except ValueError:
        print('you dont write integer')
    general_list.append(user_orice)

a=int(len(general_list)/3)
b=2*a
first_list=general_list[:a]
second_list=general_list[a:b]
third_list=general_list[b:]

insignificant_list=['name', 'price']
first_dict={}
second_dict={}
third_dict={}

for key,val in zip(insignificant_list,first_list):
    first_dict[key]=val

for key,val in zip(insignificant_list,second_list):
    second_dict[key]=val

for key,val in zip(insignificant_list,third_list):
    third_dict[key]=val   

list_of_dict=[first_dict, second_dict, third_dict]


print(first_dict)           # {"name": "Apple", "price": 100},
print(second_dict)          # {"name": "Banana", "price": 50},
print(third_dict)           # {"name": "Orange", "price": 20}
print(sort_by_price(list_of_dict))














def get_words_starting_with_vowel(words):
    vowels_of_letters = set("aeiouAEIOU")       #13 task
    if words[0] in vowels_of_letters:
        return True



user_input_words=input('Enter words: ')         # apple, banana, orange, bear, cat
list_of_user=list(user_input_words.split(', '))
new_list=[]
i=0
for i in range(len(list_of_user)):
    if get_words_starting_with_vowel(list_of_user[i]):
        new_list.append(list_of_user[i])
    i+=1

print(new_list)     # ['apple', 'orange']

