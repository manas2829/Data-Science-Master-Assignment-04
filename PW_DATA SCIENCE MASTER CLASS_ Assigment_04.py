#!/usr/bin/env python
# coding: utf-8

# # Assignment_03-02-2023

# ## 1. Which Keyword is used to create a Function? Create a Function to return a list of odd numbers in the rahge 1 to 25.
# 
# ### Ans:-
#            In Python, the keyword used to create a function is "def". 
#            
#            

# In[1]:


def odd_num():
    odd_list = []
    for i in range(1,26):
        if i%2 != 0:
            odd_list.append(i)
    return odd_list
          


# In[2]:


odd_num()


# ## 2. Why *args and ** Kwaegs is used in some functions? Create a function each for *args and Kwargs to demonstrate their use.
# 
# ### Ans:-
#            *args and **kwargs are special syntax in Python for passing a variable number of arguments to a function.
#            
#            1. *args is used to send a non-keyworded variable length argument list to the function. The syntax 
#            is to use the * before the parameter name in the function definition.Outcome data store in a tuples.

# In[3]:


def my_fun(*args):
    for arg in args:
        print(arg)
        


# In[4]:


my_fun(1,2,3,"Manas")


# ##  
#          2.**kwargs is used to send a keyworded variable length argument list to the function. The syntax 
#          is to use two asterisks ** before the parameter name in the function definition.Outcome data store in Dictionary.

# In[5]:


def my_fun1(**kwargs):
    return (kwargs)


# In[6]:


my_fun1()


# In[7]:


my_fun1(a=34,b=23,c=[1,2,3,4],d=("Manas","Priyanka"))


# ## 3. what is an iterator in python?Name the method used to initialise the iterator object and the method used for iteration. Use these methods to point the first five elements given list [2,4,6,8,10,12,14,16,18,20].
# 
# ### Ans.
#        An iterator in Python is an object that implements the iterator protocol. 
#        The iterator protocol consists of two methods: __iter__ and __next__. 
#        The __iter__ method returns the iterator object, and the __next__ method returns the next item in the iteration.
# 

# In[8]:


Number=[2,4,6,8,10,12,14,16,18,20]
n=iter(Number)
for i in range (5):
    print(next(n),end=",")


# ## 4. What are the generator function in Python? Why yield key word is used ? Give an example of a generator function.
# 
# ### Ans.
# 
#            A generator function in Python is a special type of function that allows you to generate a sequence of values 
#            one at a time, instead of generating them all at once and returning them as a list or tuple. 
#            A generator function is defined like a normal function, but instead of using the return keyword, 
#            it uses the yield keyword.
#            
#            The yield keyword allows the generator function to return a value to the caller, but 
#            it also saves the state of the function, so that when the function is called again, 
#            it resumes from the point where it left off, instead of starting over from the beginning. 
#            This allows the generator function to produce an unlimited number of values, one at a time,
#            without having to store them all in memory.
# 

# In[9]:


# Example of a generator function that generates the Fibonacci sequence:

def num_fib(n):
    a,b=0,1
    for i in range (n):
        yield a
        a,b = b,a+b
        
#fib = num_fib()
for i in num_fib(20):
    print(i,end=",")


# ## 5. Create a generator function for prime numbers less than 1000.Use the next() method to print first 20 prime number.
# 
# ### Ans:-
# 

# In[10]:


def prime_numbers_generator():
    primes = []
    for num in range(2, 1000):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
            yield num


# In[11]:


generator = prime_numbers_generator()
for i in range(20):
    print(next(generator),end=",")
    


# In[12]:


def num():
    prime_nums = []
    for i in range (2,1000):  ## Prime number is a number that is divisable by 1 or itself.
        for j in range (2,i):
            if i % j == 0:
                break
        else:
            prime_nums.append(i)
            yield i


# In[13]:


prime_list = num()
for i in range (20):
    print(next(prime_list),end=",")


# In[14]:


for num in range(1,1001):
    if num>1:
        for i in range(2,num):
            if num % i== 0:
                break
        else:
            print(num,end=",")

