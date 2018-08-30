from random import choice
from math import pow
import os
import time

# Not Repeat Characters
def is_repeat_char(str_rp):
    _str=str_rp
    b_rp=False
    for s in _str:
        c=_str.count(s)
        if c>1:
            b_rp=True
            break
    return b_rp
# Create Password List Function
def Create_Passwords(c_loop,c_char_pss,lst_indexs,lst_chars,path):
    lst_pss = []
    str_pss = ""
    count_created=1

    while len(lst_pss) < c_loop:
        for s in range(0, c_char_pss):
            i = choice(lst_indexs)
            str_pss += lst_chars[i]
        if str_pss not in lst_pss:
            with open(path, 'a') as f:
                f.write(str_pss + "\n")
                print(count_created,' from ',c_loop)
                count_created+=1
                lst_pss.append(str_pss)
        str_pss = ''
    #return lst_pss

input_Char_Pass= ""
input_Number_Pass= ""
input_Path= ""

print("<<for Exit press 'q'>>")
# Insert Characters
b_rp_char=True
while b_rp_char:
    input_Char_Pass= input("Enter the password list characters: ")
    if input_Char_Pass=='q':
        exit()
    if is_repeat_char(input_Char_Pass):
        print("Error!!\tThe input has a duplicate character")
    else:
        b_rp_char = False
        break

# Number of password characters
b_cnt=True
while b_cnt:
    input_Number_Pass=input("Enter the length of the passwords: ")
    if input_Number_Pass=='q':
        exit()
    if not input_Number_Pass.isdigit():
        print("Error!!\tInput is not number")
    else:
        input_Number_Pass=int(input_Number_Pass)
        b_cnt=False
        break

# Insert Path
b_dir=True
while b_dir:
    input_Path=input("Enter Path for Save Passwords List: ")
    if input_Path=='q':
        exit()
    if os.path.isdir(input_Path):
        b_dir=False
        break
    else:
        print("Error!!\tInvalid Path")

list_for_Index=[]
list_Char_Pass=[]
temp_index=0
for c in input_Char_Pass:
    list_for_Index.append(temp_index)
    temp_index+=1
    list_Char_Pass.append(c)

count_Pass=int(pow(len(list_Char_Pass), input_Number_Pass))
input_Path+= "\PassList(" + input_Char_Pass + ")" + str(input_Number_Pass) + "char.txt"

Create_Passwords(count_Pass, input_Number_Pass, list_for_Index, list_Char_Pass,input_Path)

print("Password list was successfully created!")


