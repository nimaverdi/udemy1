#!/usr/bin/env python
# coding: utf-8

# In[2]:


#3 key words for exception handling:

#try: block of code to be attempted (may or may not lead to error)

#except: code that will execute in case there is an error in try block

#finally: block of code to be executed regardless of error


# In[3]:


def add(n1,n2):
    print(n1+n2)
    
add(10,20)


# In[4]:


number1=10
number2=input('Enter number')

add(number1,number2) #this will return error because input value is string


# In[ ]:


#try, except

try:
    #attempt this code, may have error
    result=10+v
except: #to be executed if error occurs in try
    print('add error')
else: #to be executed if no error
    print('Add went well')


# In[ ]:


try:
    f = open('testfile','r')
    f.write("Write a test file")
except TypeError:
    print('hey there was a TypeError')
except:
    print('all other errors')
#you can have except for specific kinds of errors

finally:
    print('i always run')


# In[ ]:


def ask_for_int():
    try:
        result=int(input('insert number'))
        
    except:
        print('thats not a number')
    
    finally:
        print('end of statement')
        
ask_for_int()


# In[13]:


#how to set up function that repeats until valid

def multiply():
    
    while True:
        pass


# In[ ]:




