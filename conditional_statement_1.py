#!/usr/bin/env python
# coding: utf-8

# ## Even or Odd

# In[1]:


A=int(input("Enter number "))
if A%2==0:
    print("Number is Even")
else:
    print("Number is Odd")


# ## Vowel or Consonent

# In[36]:


alpha=(input("Enter Alphabet  "))
if (alpha=='A' or alpha=='E' or alpha=='I' or alpha=='O' or alpha=='U' or alpha=='a' or alpha=='e' or alpha=='i' or alpha=='o' or alpha=='u'):
    print("Alphabet" ,alpha, "is Vowel")
else:
    print("Alphabet" ,alpha, "is Consonent")


# ## Persons eligibility to vote

# In[41]:


Person_age=int(input("Enter Person Age- "))
if Person_age>=18:
    print("Person is eligible to vote ")
else:
    print("Person is not eligible to vote ")


# ## Given number is positive ,negative or zero

# In[44]:


a=int(input(" Enter Number "))
if a==0:
    print(" Number is zero")
elif a>0:
     print(" Number is Positive")
else:
     print(" Number is Negative")


# ## leap year

# In[5]:


a=int(input(" Enter Year "))
if a%100==0: #century year
    if a%400==0:
        print (" Year is leap year")
    else:
        print (" Year is not leap year")
else:
    if a%4==0:
        print(" Year is leap year")
    else:
        print(" Year is not leap year")


# ## Triangle is Equilateral, Isosceles or Scalene

# In[15]:


a=int(input("enter side "))
b=int(input("enter side "))
c=int(input("enter side "))
if a==b==c:
    print("Triangle is Equilateral")
elif (a==b and b!=c or  b==c and b!=a or c==b and c!=a):
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalene")


# ## convert celsius into fahrenheit

# In[4]:


n=float(input("Enter celcius value "))
F= 9/5*n+32
print("Celsius to fahrenheit ",F)


# ## Profit and loss after selling a product

# In[4]:


cp=int(input("Enter cost price "))
sp=int(input("Enter selling price "))
if sp-cp>0:
    profit=sp-cp
    print("Porfit after selling product - ",profit)
else:
    loss=cp-sp
    print("Loss after selling product - ",loss)


# ## Greatest number
# 

# In[7]:


First_number= int(input("Enter 1st number "))
Second_number= int(input("Enter 2nd number "))
if First_number > Second_number:
    print("1st number is greatest")
else:
    print("2nd number is greatest")


# In[11]:


First_number= int(input("Enter 1st number "))
Second_number= int(input("Enter 2nd number "))
Third_number= int(input("Enter 3rd number "))

if First_number > Second_number and First_number > Third_number:
    print("1st number is greatest")
    
elif Second_number > First_number and Second_number > Third_number:
    print("2nd number is greatest")
else:
    print("3rd number is greatest")


# ## smallest number

# In[12]:


First_number= int(input("Enter 1st number "))
Second_number= int(input("Enter 2nd number "))
if First_number < Second_number:
    print("1st number is smallest")
else:
    print("2nd number is smallest")


# In[13]:


First_number= int(input("Enter 1st number "))
Second_number= int(input("Enter 2nd number "))
Third_number= int(input("Enter 3rd number "))

if First_number < Second_number and First_number < Third_number:
    print("1st number is smallest")
elif Second_number < First_number and Second_number < Third_number:
    print("2nd number is smallest")
else:
    print("3rd number is smallest")


# ## Finding roots of a quadratic equation

# In[6]:


a=int(input("Enter a "))          ##ax2+bx+c
b=int(input("Enter b "))
c=int(input("Enter c "))

d = (b**2) - (4*a*c)

if d > 0: 
    print(" Real and Different roots ") 
    print("x = ",(-b + d**0.5)/(2 * a)) 
    print("x = ",(-b - d**0.5)/(2 * a))
    
elif d == 0: 
    print(" Real and Same roots") 
    print("x = ", -b / (2 * a)) 
    
else:
    print("Complex Roots") 
        


# ## print week days

# In[7]:


a=int(input(" enter value between 1 to 7=  "))
if a==1:
    print("Monday")
elif a==2:
    print("Tuesday")
elif a==3:
    print("Wednsday")
elif a==4:
    print("Thursday")
elif a==5:
    print("Friday")
elif a==6:
    print("Saturday")
elif a==7:
    print("Sunday")
else:
    print("A week has 7 days only")


# ## Print all month of a year

# In[9]:


a=int(input(" enter value between 1 to 12=  "))
if a==1:
    print("January")
elif a==2:
    print("February")
elif a==3:
    print("March")
elif a==4:
    print("April")
elif a==5:
    print("May")
elif a==6:
    print("June")
elif a==7:
    print("July")
elif a==8:
    print("August")
elif a==9:
    print("September")
elif a==10:
    print("October")
elif a==11:
    print("November")
elif a==12:
    print("December")
else:
    print("A year has 12 months only")


# ## Input 2 numbers and perform Addition, Subtraction, Multiplication and Division

# In[3]:


F= int(input("Enter 1st number "))
S= int(input("Enter 2nd number "))
Z=input("enter function name (add,sub,mul,div) - ")

if Z == 'add':
    result = F + S
    print("The result is:", result)
elif Z == 'sub':
    result = F - S
    print("The result is:", result)
elif Z == 'mul':
    result = F * S
    print("The result is:", result)
elif Z == 'div':
    result = F / S
    print("The result is:", result)
else:
    pass


# ## convert celsius into fahrenheit

# In[9]:


c=float(input("Enter celcius value "))
F= 9/5*c+32
print("Celsius to fahrenheit - ",F)


# ## convert fahrenheit into celsius

# In[10]:


F=float(input("Enter fahrenheit value "))
C=(F-32)*5/9
print("fahrenheit to Celsius - ",C)


# ## 5% bonus if Year of service is more than 5 year and print net bonus of employyee

# In[1]:


S= int(input("Enter Your Salary "))
E= int(input("Enter Years of Service "))
if E>5:
    Bonus=S*0.05
    print("Net Bonus Amount= ",Bonus)
else:
    print("Not eligible for Bonus")


# ## Program to know its square or rectangle

# In[15]:


l=int(input("Enter length "))          
b=int(input("Enter breath "))
if l==b:
    print("It is square")
else:
     print("It is rectangle")


# ## oldest and youngest person 

# In[17]:


a=int(input("Enter age of 1st person "))          
b=int(input("Enter age of 2nd person "))
c=int(input("Enter age of 3rd person "))

if a>b and a>c:
    print("1st person is Oldest")
elif b>c and b>a:
    print("2nd person is Oldest")
else:
    print("3rd person is Oldest")
    
if a<b and a<c:
    print("1st person is Youngest")
elif b<c and b<a:
    print("2nd person is Youngest")    
else:
    print("3rd person is Youngest")


# ## Students marks and grades

# In[19]:


marks=int(input("Enter marks between 0 to 100 = "))
if marks>80:
    print("A grade")
elif marks>=60 and marks<=80:
    print("B grade")
elif marks>=50 and marks<60:
    print("C grade")
elif marks>=45 and marks<50:
    print("D grade")
elif marks>=25 and marks<45:
    print("E grade")
else:
    print("F grade")


# In[ ]:




