#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','u','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['@','#','$','%','(',')']
print("WECLOME TO PASSWORD GENERATOR!")
l = int(input("How many 'Letters' do you want in your password?\n")) #Letters
n = int(input("How many 'Numbers' do you want in your password?\n")) #numbers
s = int(input("How many 'symbols' do you want in your password?\n"))  #symbols
password = []
for i in range(1,l+1):
    char = random.choice(letters)
    password += char
for i in range(1,n+1):
    num = random.choice(numbers)
    password += num
for i in range(1,s+1):
    sym = random.choice(symbols)
    password += sym
random.shuffle(password) # for shuffle the generator password
password_list = ""
for i in password:
    password_list+=i
print(password_list)    



# In[ ]:




