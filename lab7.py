

file=open('text1.txt')      #1 task
# print(file.read())          #output content in text files 







import random
file=open('text1.txt')            #2 task
lines=file.readlines()
random_line = random.choice(lines)        #output random lines in text files
print(random_line)







def uper_letters(str):                    #3 task
    lines=str.readlines()
    k=0
    for i in lines:
        for j in i:
            if j.isupper():
                k+=1                #counter uper letter 
    return k


file=open('text1.txt')           
ans=uper_letters(file)
print(f'in text file it will be {ans} uppercase letter')






def line_letter_D(str):
    for line_number, line_content in enumerate(str, 1):     
        if line_content.startswith('D'):                   #where i search letter d in lines 
            k=line_number                 #write this lines
    return k


file=open('text1.txt')                                        #4 task
ans=line_letter_D(file)
print(ans)






def word_counter_end_f(word):       #5 task

    file=open(word)
    content=file.read()                 
    words=content.split()

    count = sum(1 for i in words if i.endswith(('F','f' )))    # there i count end of word letteral "F"
    return count


name='text1.txt'
ans=word_counter_end_f(name)
print(ans)








def word_counter_all_or_nine(name_word):          #6 task
    file=open(name_word)    
    content=file.read() 
    words=content.split()

    
    count_all = words.count('all')
    count_no = words.count('none')

    return count_all, count_no



name='text1.txt'
ans_all,ans_no=word_counter_all_or_nine(name)
print(ans_all)
print(ans_no)









file=open('text1.txt')   #7 task
content=file.read() 
words=content.split()

word_frequency = {}     #create dic for write freq

for word in words:

    cleaned_word = word.strip('.,!?()[]{}":;')    
    cleaned_word = cleaned_word.lower()

    if cleaned_word:
        word_frequency[cleaned_word] = word_frequency.get(cleaned_word, 0) + 1


for word, frequency in word_frequency.items():
    print(f"{word}: {frequency}")









file=open('text1.txt')   #8 task
content=file.read() 
words=content.split()

word_frequency = {}     #create dic for write freq
list_of_word=[]

for word in words:

    cleaned_word = word.strip('.,!?()[]{}":;')    
    cleaned_word = cleaned_word.lower()

    list_of_word.append(cleaned_word)

sorted_word_list = sorted(list_of_word, key=len)

print(sorted_word_list[-1])








def core_version(name_text):

    file=open(name_text)              #9 task
    lines = file.readlines()

    for line in lines:
        core=line.replace('B','J')

        if line!=core:
            print(f"Content of the file: {repr(line)}\n          Output: {repr(core)}")
            a=core
            

    corrected_content = ''.join(a)
    return corrected_content


name='text1.txt'
ans=core_version(name)
print(ans)








def core_version(name_text):

    file=open(name_text)              #10 task
    lines = file.readlines()
    a=0
    b=0
    for line in lines:
        for letter in line:

            if letter=='a' or letter=='A':
                a+=1
            if letter =='b' or letter=='B':
                b+=1

    return a,b


name='text1.txt'
ans_a,ans_b=core_version(name)
print('a = ',ans_a)
print('b = ',ans_b)
