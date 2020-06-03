#!/usr/bin/env python
# coding: utf-8

# ## Question 1

# 5              integer
# -------------------------------------------------------------------
# 5.0            float
# -------------------------------------------------------------------
# 5 > 1          boolean expression
# -------------------------------------------------------------------
# '5'            string
# -------------------------------------------------------------------
# 5 * 2          integer multiplication
# -------------------------------------------------------------------
# '5' * 2        string concatenation of 2 copies of string '5'
# -------------------------------------------------------------------
# '5' + '2'      string concatenation of '5' and '2'
# -------------------------------------------------------------------
# 5 / 2          integer division resulting in float value
# -------------------------------------------------------------------
# 5 // 2         integer division giving only quotient
# -------------------------------------------------------------------
# [5, 2, 1]      list
# -------------------------------------------------------------------
# 5 in [1, 4, 6] boolean expression
# -------------------------------------------------------------------
# math.pi        standard python library module
# -------------------------------------------------------------------
# 

# ## Question 2

# In[ ]:


#2.a
string1 =  "Supercalifragilisticexpialidocious"
len(string1)


# In[ ]:


#2.b
subString1 = 'ice'
subString1 in string1


# In[ ]:


#2.c
##adding the strings into the list
stringList = ['Supercalifragilisticexpialidocious', 'Honorificabilitudinitatibus', 'Bababadalgharaghtakamminarronnkonn']
## creating a container empty string
longestString = ''
##looping around the stringList, checking the legnth of the elements of the list and assigning to the empty string
for string in stringList:
    if len(string) > len(longestString):
        longestString = string
print(longestString)


# In[ ]:


#2.d
#adding the composers' names into the list
composerList = [ 'Berlioz', 'Borodin', 'Brian','Bartok', 'Bellini', 'Buxtehude', 'Bernstein']
#using library sort function that alphabetizes the list 
composerList.sort()
#printing the first and last element of the list
print('The first composer in the dictionary is ' + composerList[0] + 'and the last is '
     + composerList[-1])


#  ## Question 3

# In[ ]:


#3.a
#simple maths checking the point co ordinates provided against the lower and upper points
def inside(x, y, x1, y1, x2, y2):
    print( x > x1 and x < x2  and y > y1 and y < y2)
        
inside (-1, - 1, 0, 0, 2, 3)


# In[ ]:


#3.b
#using and boolean expressions so that both conditions must be true 
inside (1, 1, 0.3, 0.5, 1.1, 0.7) and inside (1, 1, 0.5, 0.2, 1.1, 2)


# ## Question 4 

# In[ ]:


#asking user for the word and saving into words string
words = input('Enter the word you wish to change into pig-Latin: ')

# calling our pig func
pig(words)

def pig(word):
#     checking whether the first letter of the word is a vowel or consonant
    if word[0] in ['a', 'e', 'i', 'o', 'u']:
        word += 'way'
        print ('The pig-Latin word is ' + word)
    else:
#         remvoing the first letter, concatenating that letter at the end with 'ay'
        word = word[1:] + word[0] + 'ay'
        print ('The pig-Latin word is ' + word)


# ## Question 5
# 

# In[ ]:


# importing Counter function from collections library
from collections import Counter 

#open the file with absolute path
bloodTypeFile = open(r"C:\\Users\\prav3\\Documents\\bloodtype1.txt")

#read the file and split in to multiple lines and assign it to content
content = bloodTypeFile.read().split()

#close the cursor
bloodTypeFile.close()

#using collections library and importing Counter function
counts = Counter(content)
for key, value in counts.items():
    print ('There are ' + str(value) + ' patient(s) of blood type ' + key + '.')
    


# ## Question 6
# 

# In[ ]:


# importing Counter function from collections library
from collections import Counter 

# providing absolute path the open it in r mode
currenciesFile = open(r"C:\\Users\\prav3\\Documents\\currencies.txt")

# reading the file per line
content = currenciesFile.readlines()

#close the cursor
currenciesFile.close()

# multiplier is for the conversion value
multiplier = 0.0

def curconversion(name, value):
    for a in content:
        if name in a:
#           we are trying to extract the currency rate from the content list by splitting the first 4 characters and going upto last
#           digit of the rate and changing it to float value
            multiplier = float(a[4:13])
    
#            value is supplied by the user along the currency code (name)
            print('The value of 100 '+ name + ' in US dollars is ' + str(multiplier * value))
            return
    print("Error")

curconversion('EUR', 100)


# ## Question 7

# Trying to add incompatible variables, as in
# adding 6 + ‘a’:  `TypeError`
# 
# Referring to the 12th item of a list that has only 10
# items:   `IndexError`
# 
# Using a value that is out of range for a function’s
# input, such as calling math.sqrt(-1.0)  `ValueError`
# 
# Using an undeclared variable, such as print(x)
# when x has not been defined `NameError`
# 
# Trying to open a file that does not exist, such as
# mistyping the file name or looking in the wrong
# directory.  `IOError`

# ## Question 8

# In[ ]:


from collections import Counter 

# we are using counter function which takes a string and counts each characters and returns it in key value pair
def frequencies(cryptoText):
        print (Counter(cryptoText.lower()))

frequencies('The quick red fox got bored and went home.')

frequencies('apple')


# ## Question 9

# In[2]:


## This was the most time consuming question for me tbh

# creating two empty intital lists
L = []
primeL = []

# asking the user for the max range upto which we want the prime numbers
maxRange = int(input('Enter the number: '))

# using maxrange to add the values into the first List
for i in range(2, maxRange): 
    L.append(i) 

# this function first checks the length of first list
# if the list is not empty, we take the 1st element of the 1st list to the primeL list
# assigning the 1st element of L to fEL because we dont want it to change inside the  iteration in the if condition
# inside the for loop, we check the multiples of 1st element and remove them.
# after the removal, we have a new list and we repeat the same process, so using recurssion we call the siev() again
# when everything is removed and list is empty we simply print the primeL list with all the prime numbers inside it
def siev(): 
    if len(L) > 0:
        primeL.append(L[0])
        fEl = L[0]
        for i in L:
            if i%fEl == 0:
                L.remove(i)
        siev()
    else:
        print(primeL)
        return

#     we call this function which prints the prime numbers
siev()


# ## Question 10

# In[ ]:


import math
s = 0.0
# nothing special just using sqrt function found within math library to do the calculation
def calculateArea(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s-a) * (s - b) * (s-c))

calculateArea(2,2,2)

