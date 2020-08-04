#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Problem 1

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('invalid calculation')
    


# In[7]:


#Problem 2

try:
    x = 5
    y = 0

    z=x/y

except ZeroDivisionError:
    print('cannot divide by 0')

except:
    print('Other error')
    
finally:
    print('All done')


# In[25]:


#Problem 3

def ask():
    
    while True:
        try: #run this code
            number = int(input('Please enter a number'))
            return number**2
        except: #if it returns an error run this code and repeat the block
            print("That's not a valid. Try again.")
            
        else: #if there is no error, break the while
            break


ask()


# In[ ]:





# In[ ]:




