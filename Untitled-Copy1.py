#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Ex1 Convert radians into degrees
def rad_to_deg(rad):
    return rad*180/3.14
rad_to_deg(float(input('Enter radians')))


# In[23]:


#Ex2 Sort a list
def sort_list(list_num,order):
    if order == 'asc':
        return list_num.sort()
        print(list_num) 
    elif order == 'desc':
        return list_num.sort(reverse=True)
    else:
        return list_num
list = [5,7,4,8,1]
sort_list(list,input('Enter order'))
list


# In[31]:


#Ex3 Convert a decimal number into binary
dec_val = int(input('Enter digital number'))
string = ''
while dec_val > 0:
    string += '{}'.format(dec_val%2)
    dec_val = dec_val//2
print(string[::-1])


# In[39]:


#Ex4 Count the vowels in a string
def vowels_count(string):
    count_v = 0
    for x in string:
        if x in 'aeiou':
            count_v +=1
    return count_v
vowels_count(input('Enter string'))


# In[48]:


#Ex5 Hide the credit card number
def hide_id(id_number):
    index = 0
    for x in id_number:
        if index < len(id_number)- 4:
            id_number = id_number.replace(x,'#',1)
            index += 1
    return id_number

hide_id('1237698730')


# In[51]:


#Ex6 Are the Xs equal to the Os?
def x_eq_o(string):
    return string.count('O') == string.count('X')

x_eq_o('qwerty')
    


# In[55]:


#Ex7 Create a calculator function
def calc(a,b,sign):
    if sign == '+':
        return a+b
    elif sign == '-':
        return a-b
    elif sign == '/':
        return a/b
    elif sign == '*':
        return a*b
    else:
        print('Enter operator one of +,-,/,*')
       

calc(6,10,'d')
    


# In[63]:


#Ex8 Give me the discount
def disc(price,disc):
    return price*(1-disc/100)

disc(230,20)


# In[62]:


#Ex9 Just the numbers
def just_num(string):
    just_num = ''
    for x in string:
        if x.isdigit():
            just_num += x
    return just_num

just_num('1f3f2f4b')


# In[60]:


#Ex10 Repeat the characters
def repeat(string):
    new_string = ''
    for x in string:
        new_string += x*2
    return new_string

repeat('abc')
    


# In[ ]:




