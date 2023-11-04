
user_input=input()      # 1,1 task
print(tuple(user_input))






from collections import Counter
user_input=input()      # 1,2 task        Pulp Fiction
tup_el=list(tuple(user_input.lower()))
print(tup_el)
symble_count=Counter(tup_el)
symbol_freq_list = list((symble_count).items())
print(symbol_freq_list)







from collections import Counter        # 1.3 task
user_input=input()     
tup_el=list(tuple(user_input.lower()))
print(tup_el)
symble_count=Counter(tup_el)
symbol_freq_list = list((symble_count).items())
print(symbol_freq_list)
list_vow=[]
list_cons=[]
for item in symbol_freq_list:
    el,val=item
    if el.isalpha():
        if el=='a' or el=='e' or el=='i' or el=='o' or el=='u' or el=='y':
            list_vow.append((el,val))
        else :
            list_cons.append((el,val))
    else:
        list_sym=el,val


print('list_vow = ',list_vow)
print('list_cons = ',list_cons)
print('list_sym = ',list_sym)







try:                          #1.4 task
    user_input=input()      #1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4       
    list_A=list(map(int, user_input.split(', ')))       #1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4, 8
    list_A.sort()
    twenty_five=len(list_A)//4
    half_list=len(list_A)//2
    for el in list_A:
        if len(list_A)%4==0:
            q_one=list_A[:twenty_five]
            q_two=list_A[twenty_five:half_list]
            q_three=list_A[half_list:half_list+twenty_five]
            q_four=list_A[half_list+twenty_five:]
        elif len(list_A)%4==1:
            for i in range(3):
                list_A.insert(0,0)
            twenty_five=len(list_A)//4
            half_list=len(list_A)//2
            q_one=list_A[:twenty_five]
            q_two=list_A[twenty_five:half_list+1]
            q_three=list_A[half_list+1:half_list+twenty_five+1]
            q_four=list_A[half_list+twenty_five+1:]
    print(list_A)
    print('q1=',q_one,'\nq2=',q_two,'\nq3=',q_three,'\nq4=',q_four)
except ValueError:
    print('You dont write integers ')








user_name=input('Enter Name: ')         #Adam          task 2.1
assigment_of_student=input('Enter assignments: ')         #82, 56, 44, 30  
list_assigment=list(map(int, assigment_of_student.split(', ')))     

labs=input('Entere labs: ')                 #78.20, 77.20
list_labs=list(map(float,labs.split(', ')))

test=input('Enter test: ')                  #78, 77
list_test=list(map(int, test.split(', ')))

print(list_assigment)
print(list_labs)
print(list_test)

st_dict={}
students_keys=['name','assignment','test','lab']

for key,val in zip(students_keys,[user_name,list_assigment,list_labs,list_test]):
    st_dict[key]=val
print('student = ',st_dict)










user_name=input('Enter Name: ')         #Adam          task 2.2
assigment_of_student=input('Enter assignments: ')         #82, 56, 44, 30       2.12    max 4 point
list_assigment=list(map(int, assigment_of_student.split(', ')))     

labs=input('Entere labs: ')                 #78.20, 77.20   max 2p
list_labs=list(map(float,labs.split(', ')))

test=input('Enter test: ')                  #78, 77     max 2p
list_test=list(map(int, test.split(', ')))

print(list_assigment)
print(list_labs)
print(list_test)

st_dict={}
students_keys=['name','assignment','test','lab']
for key,val in zip(students_keys,[user_name,list_assigment,list_labs,list_test]):
    st_dict[key]=val
print('student = ',st_dict)


assigment=0
while assigment<len(list_assigment):
    assigment+=1

activity_test=0
while activity_test<len(list_test):
    activity_test+=1

activity_labs=0
while activity_labs<len(list_labs):
    activity_labs+=1

activites=assigment+activity_test+activity_labs
list_user_name=list(user_name.split(' '))
dict_activites=dict.fromkeys(list_user_name,activites)

print(dict_activites)












while True:
    user_name=input('Enter Name: ')         #Adam          task 2.3     2student is Kevin
    if user_name=='stop':
        break
    else:
        assigment_of_student=input('Enter assignments: ')         #82, 56, 44, 30      max 4p     2student 82, 30
        list_assigment=list(map(int, assigment_of_student.split(', ')))     

        labs=input('Entere labs: ')                 #78.20, 77.20   max 2p      Kevin 78.2
        list_labs=list(map(float,labs.split(', ')))

        test=input('Enter test: ')                  #78, 77     max 2p      Kevin  0
        list_test=list(map(int, test.split(', ')))

        print(list_assigment)
        print(list_labs)
        print(list_test)

        st_dict={}
        students_keys=['name','assignment','test','lab']
        for key,val in zip(students_keys,[user_name,list_assigment,list_labs,list_test]):
            st_dict[key]=val
        i=1
        print(f'student{i} = ',st_dict)


        assigment=0
        if sum(list_assigment) !=0:
            while assigment<len(list_assigment):
                assigment+=1
        else:
            list_assigment.clear()

        activity_test=0
        if sum(list_test) !=0:
            while activity_test<len(list_test):
                activity_test+=1
        else:
            list_test.clear()

        activity_labs=0
        if sum(list_labs) !=0:
            while activity_labs<len(list_labs):
                activity_labs+=1
        else:
            list_labs.clear()

        activites=assigment+activity_test+activity_labs     #activites 4p for assigment 2p for labs and 2p for test
        list_user_name=list(user_name.split(' '))
        dict_activites=dict.fromkeys(list_user_name,activites)
        print('submission_rate = ',dict_activites)


        if sum(list_assigment)==0:
            final_assig=0
        else:
            final_assig=0.3*sum(list_assigment)/len(list_assigment)
        if sum(list_labs)==0:
            final_labs=0
        else:
            final_labs=0.5*sum(list_labs)/len(list_labs)
        if sum(list_test)==0:
            final_test=0
        else:
            final_test=0.2*sum(list_test)/len(list_test)
            
        if final_assig ==0 or final_labs==0 or final_test==0:
            final_grade=0
        else:
            final_grade=final_assig+final_labs+final_test
        
        st_dict2={}
        students_keys=['name','assignment','test','lab','final_grade']
        for key,val in zip(students_keys,[user_name,list_assigment,list_labs,list_test,final_grade]):
            st_dict2[key]=val
        print(f'student{i} = ',st_dict2)
        i+=1















def function_students(student_name,assigment_of_students,lab_students,test_students):
    list_assigment=list(map(int, assigment_of_students.split(', '))) 
    list_labs=list(map(float,lab_students.split(', ')))
    list_test=list(map(int, test_students.split(', ')))
    print(list_assigment)
    print(list_labs)
    print(list_test)

    st_dict={}
    students_keys=['name','assignment','test','lab']
    for key,val in zip(students_keys,[student_name,list_assigment,list_labs,list_test]):        # i need output
        st_dict[key]=val


    assigment=0
    if sum(list_assigment) !=0:
        while assigment<len(list_assigment):
            assigment+=1
    else:
        list_assigment.clear()

    activity_test=0
    if sum(list_test) !=0:
        while activity_test<len(list_test):
            activity_test+=1
    else:
        list_test.clear()

    activity_labs=0
    if sum(list_labs) !=0:
        while activity_labs<len(list_labs):
            activity_labs+=1
    else:
        list_labs.clear()


    activites=assigment+activity_test+activity_labs     #activites 4p for assigment 2p for labs and 2p for test
    list_user_name=list(student_name.split(' '))
    dict_activites=dict.fromkeys(list_user_name,activites)           # i need output

    if sum(list_assigment)==0:
        final_assig=0
    else:
        final_assig=0.3*sum(list_assigment)/len(list_assigment)
    if sum(list_labs)==0:
        final_labs=0
    else:
        final_labs=0.5*sum(list_labs)/len(list_labs)
    if sum(list_test)==0:
        final_test=0
    else:
        final_test=0.2*sum(list_test)/len(list_test)
            
    if final_assig ==0 or final_labs==0 or final_test==0:
        final_grade=0
    else:
        final_grade=final_assig+final_labs+final_test
        
    st_dict2={}
    students_keys=['name','assignment','test','lab','final_grade']
    for key,val in zip(students_keys,[student_name,list_assigment,list_labs,list_test,final_grade]):           # i need output
        st_dict2[key]=val

    return st_dict, dict_activites, st_dict2







user_name=input('Enter Name: ')         #Adam          task 2.4     

assigment_of_student=input('Enter assignments: ')         #82, 56, 44, 30      max 4p    

labs=input('Entere labs: ')                 #78.20, 77.20   max 2p      

test=input('Enter test: ')                  #78, 77     max 2p     


result=function_students(user_name,assigment_of_student,labs,test)
student_dict, dict_activites_stud, student_dict2=result
print('student = ',student_dict)
print('submission_rate = ',dict_activites_stud)
print('student = ',student_dict2)




user_name2=input('Enter Name: ')        #Kevin

assigment_of_student2=input('Enter assignments: ')      #82, 30

labs2=input('Entere labs: ')                    # 78.2

test2=input('Enter test: ')                     # 0


result2=function_students(user_name2,assigment_of_student2,labs2,test2)
student_dict3, dict_activites_stud2, student_dict4=result2     #unpacking tuples
print('student = ',student_dict3)
print('submission_rate = ',dict_activites_stud2)
print('student2 = ',student_dict4)



finish_dict={}
list_user_name1=list(user_name.split(' '))
list_user_name2=list(user_name2.split(' '))
key_list=list_user_name1+list_user_name2        #we do for new key


if student_dict2:
    first_key=next(iter(student_dict2))
    first_val=student_dict2[first_key]
    del student_dict2[first_key]

if student_dict4:
    first_key=next(iter(student_dict4))
    first_val=student_dict4[first_key]
    del student_dict4[first_key]

for key,val in zip(key_list,[student_dict2,student_dict4]):
    finish_dict[key]=val
print('students = ',finish_dict)














# [(1001, 2), (1001, 1), (1003, 2), (1005,2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003,2), (1001, 1)]       1 - comment, 2 - like, 3 - share
# (1001, 2), (1001, 1) (1001, 3)(1001, 1)
# (1003, 2) (1003,2)
# (1005,2)
# (1007, 1) (1007, 2)
# (1100, 2)



# user_input = []  

# while True:
#    try:
 #       key = int(input("Enter key: "))
  #      value = int(input("user transaction(chose 1 - comment, 2 - like, 3 - share): "))
   #     user_input.append((key, value))
        

    #    if value >=4:
     #       print('Error, your chose incorect')
      #      break
    #except ValueError:
     #   print("error!")
      #  break
        
user_input=[(1001, 2), (1001, 1), (1003, 2), (1005,2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003,2), (1001, 1)]

print(user_input)
user_keys=list(set([item[0] for item in user_input]))
print(user_keys)
print(len(user_input))




stats = {}  

for user_id, transaction_type in user_input:
    user_id = str(user_id)  # Преобразуем user_id в строку, чтобы использовать его как ключ

    if user_id not in stats:
        stats[user_id] = {2: 0, 1: 0, 3: 0, 'mft': 0, 'lft': 0}

    stats[user_id][transaction_type] += 1  # Увеличиваем счетчик для данного типа транзакции

# Вычисляем mft (самую частую транзакцию) и lft (самую редкую транзакцию) для каждого пользователя
for user_id, user_data in stats.items():
    max_transaction = max(user_data, key=user_data.get)
    min_transaction = min(user_data, key=user_data.get)
    user_data['mft'] = max_transaction
    user_data['lft'] = min_transaction

print(stats)








