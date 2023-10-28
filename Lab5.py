
# user_input=input()      # 1 task
# print(tuple(user_input))


from collections import Counter
user_input=input()      # 2 task
tup_el=list(tuple(user_input))
print(tup_el)
symble_count=Counter(tup_el)
symbol_freq_list = list(symble_count.items())
print(symbol_freq_list)

