
# coding: utf-8

# # WWC - Regular Expresions in Python
# 
# Facilitator: Diana Amador
# 
# From Automate the Boring Stuff with Python

# **Regular Expressions** allow you to specify a pattern of text to search for. 
# 
# **Search** and **Replace** functions in MS-Word or OpenOffice are examples of regular expression processing.
# 
# For instance, to search for a phone number. 
# 
# A phone number in the US is a text structure with a 3-digit Area Code followed by hyphen, a group of three digits, another hyphen and a group of four digits.
# 

# ### TASK 1
# 
# Write a Python Program to find text patterns without using regular expressions. We will be matching regular expressions.

# In[1]:

def isPhoneNumber(text):
    if len(text)!= 12: # 1
        return False
    for i in range(0,3): 
        if not text[i].isdecimal(): # 2
            return False
    if text[3] != '-': # 3
        return False
    for i in range(4,7):
        if not text[i].isdecimal(): # 4
            return False
    if text[7] != '-': # 5
        return False
    for i in range(8,12): 
        if not text[i].isdecimal(): # 6
            return False
    return True


# In[2]:

print('409-223-8952 is a phone number:')
print(isPhoneNumber('409-223-8952'))


# In[3]:

print('Shala lala is a phone number:')
print(isPhoneNumber('Shala lala'))


# **HOW IT WORKS**
# 
# The **isPhoneNumber( )** function has code that validates the string structure to match a phone number structure.
# 
# 
# 1. Check the string length to be 12-character long
# 2. Check the first group of characters are all digits
# 3. Check for the first hyphen
# 4. Check the second group of characters are all digits
# 5. Check for the second hyphen
# 6. Check the third group of characters are all digits
# 

# ### TASK 2
# 
# Add code to the previous one to find the phone pattern inside a larger string.

# In[4]:

message = 'Call me at 409-223-8952 tomorrow. 409-888-8498 is my office'


# In[6]:

for i in range (len(message)):
    chunk = message[i:i+12] #1
    if isPhoneNumber(chunk): #2
        print('Phone number found:'+ chunk)
print('Done')


# In the new code:
# 
# 
# 1. on each iteration of the *for* loop, a new 12-character long chunk is cut from the *message* and assigned to the variable chunk.
# 2. The chunk is passed to the isPhoneNumber( ) to see if it matches the phone number pattern, and if so, print the chunk (the phone number).
# 
# The loop goes through the entire string, testing each 12-character piece and printing any chunk it finds that satisfies isPhoneNumber( ).
# 

# ### TASK 3
# 
# #### Create **Regex Objects** using **re** module
# 
# The previous code will not match different valid phone number structure such as 409.223.8952 or (409) 223-8952.
# 
# In order to make things easier you can use **Regular Expressions** which are also called **regexes** for short. **Regexes** are descriptions for a pattern of text.
# 
# For example, a *\d* in a regex stands for a digit character. The regex \d\d\d-\d\d\d-\d\d\d\d is used in Python to match the same text the previous isPhoneNumber( ) function did.
# 
# Another way to create the phone number pattern with repeated characters would be: \d{3}-\d{3}-\d{4}
# 
# 

# In[7]:

import re


# To create a Regex Object pass a string value representing your regular expression to **re.compile()**. It will return a Regex pattern object.

# In[9]:

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')


# #### Passing Raw Strings
# 
# By putting a 'r' character before the first quote of the string value, you can mark the string as a *raw string*, which does not escape characters and don't need to type extra backlashes (I.e. '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d.)

# #### Matching Regex Objects
# 
# A *Regex* object's *search ( )* method searches the string that is passed for any matches of the regex.
# 
# **HOW IT WORKS**
# 
# The *search( )* method will return None if the regex pattern is not found in the string. If the pattern is found, the *search( )* method will return a *Match* object.
# 
# *Match* objects have a *group( )* method that will return the actual matched text from the searched string.

# In[19]:

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchObject = phoneNumRegex.search('My number is 409-223-8952')
print(matchObject)


# In[20]:

print('Phone number found: ', matchObject.group())


# #### GROUPING PATTERNS WITH PARENTHESES
# 
# Adding parentheses will create groups in the *regex*: (\d-\d-\d)-(\d\d\d-\d\d\d\d). Then you can use the group() match object method to grab the matching text from just one group.
# 
# **HOW IT WORKS**
# 
# The first group of parentheses in a regex string will be group 1. The second will be group 2. 
# 
# By passing the integer 1 or 2 to the group() match object method, you can grab different sections of the matched text.
# 
# Passing 0 or nothing to the group( ) method will return the entire text.
# 
# To retrieve all the groups at once, use the groups(  ) method.

# In[21]:

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('My number is 409-223-8952')
matchObject.group(1)


# In[22]:

matchObject.group(2)


# In[23]:

matchObject.group()


# In[24]:

matchObject.groups()


# In[25]:

areaCode, mainNumber = matchObject.groups()


# In[26]:

print(areaCode)


# In[27]:

print(mainNumber)


# **CONSIDERATIONS**
# 
# Parentheses have a special meaning in regular expressions, so if you have to match a parentheses in your text, you have to escape them with backslashes.

# In[28]:

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
matchObject = phoneNumRegex.search('My phone number is (415) 555-4242.')
matchObject.group(1)


# In[30]:

matchObject.group(2)


# #### MATCHING SEVERAL GROUPS
# 
# The | (pipe) character can be used to match one of many expresions. It works like an OR. 
# 
# The first occurence of the matching text will be returned as the Match Object.
# 
# The | can also be used to match one of several patterns as part of your Regex. For example "Bat" in Batman, Batmobile, Batcopter and Batbat.

# In[31]:

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
mo1.group()


# In[32]:

mo2 = heroRegex.search('Tina Fey and Batman.')
mo2.group()


# In[33]:

batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()


# In[34]:

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()


# The (wo)? part of the regular expression means that the pattern wo is an optional group.
# 
# The regex will match text that has zero instances or one instance of wo in it.

# In[40]:

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
mo.group()


# In[41]:

mo.group(1)


# #### PUT IT INTO PRACTICE
# 
# Use (wo)? to make the regex look for phone numbers that do or do not have an area code.

# In[36]:

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 409-223-895242')
mo1.group()


# In[37]:

mo2 = phoneRegex.search('My number is 223-8952')
mo2.group()


# #### MATCHING ZERO OR MORE WITH STAR
# 
# The * character means "match zero or more".
# The group that precedes the star can occur any number of times in the text. It can be absent or repeated.

# In[44]:

batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
mo1.group()


# In[45]:

mo2 = batRegex.search('The Adventures of Batwoman')
mo2.group()


# In[46]:

mo3 = batRegex.search('The Adventures of Batwowowowowoman')
mo3.group()


# #### MATCHING ONE OR MORE WITH THE PLUS
# 
# The + character means "match one or more".
# The group must appear at least once. It is not optional.

# In[54]:

batRegex = re.compile(r'Bat(wo)+man')
mo1 = batRegex.search('The Adventures of Batwoman')
mo1.group()


# In[55]:

mo2 = batRegex.search('The Adventures of Batwowowowowoman')
mo2.group()


# In[60]:

mo3 = batRegex.search('The Adventures of Batman')
mo3 == None


# #### MATCHING SPECIFIC REPETITIONS
# 
# Same patterns:
# 
# (Ha){3}
# (Ha)(Ha)(Ha)
# 
# or:
# 
# (Ha){3,5}
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))

# In[61]:

haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
mo1.group()


# In[62]:

mo2 = haRegex.search('Ha')
mo2 == None


# #### GREEDY AND NON GREEDY MATCHING
# 
# Python's regular expressions are *greedy* by default, which means thatin ambiguous situations they will match the longest string possible.
# 
# The *non-greedy* version of the curly brackets, which matches the shortest string possible, has the closing bracket followed by a question mark. 

# In[63]:

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
mo1.group()


# In[65]:

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
mo2.group()


# #### THE FINDALL(  ) METHOD
# 
# While search(  ) method will return a **Match** object of the first matched text in the searched string, the findall( ) method will return every match in the searched string.
# 
# Findall(  ) has no groups. If there are groups in the regular expression, then findall(  ) will return a list of tuples.

# In[67]:

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
mo.group()


# In[69]:

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')


# In[70]:

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')


# #### SHORTHAND CODES FOR COMMON CHARACTER CLASSES
# 
# - \d    Any numeric digit from 0 to 9
# - \D    Any character that it is not a numeric digit
# - \w    Any letter, numeric digit, or the underscore character ("word" characters
# - \W    Any character that is not a letter, numeric digit, or underscore character.
# - \s    Any space, tab, or newline character ("space" characters)
# - \S    Any character that is not a space, tab or newline

# In[72]:

xmasRegex = re.compile(r'\d+\s\w+')
xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')


# #### MINIPROJECT
# 
# Download any of the sample text files.
# Find all the occurrences of a pattern using regular expresions. You may use Excel File 911_short available at the Git repo: github.com/damchilly/WWC-Regular-Expressions

# In[ ]:



