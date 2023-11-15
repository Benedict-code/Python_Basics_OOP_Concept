"""CONCATENATION
============="""
print(10+10)
print(1.1+2.4)
print(1.2+1)
print("welcome"+"python")  #invalid
# print("welcome"+2)  #invalid
# print("add"+2.5)
print(True+5)
print(False+2)
# print(True+"welcome")  #invalid statement

"""#swapping of variables
======================="""
a,b=b,a
print("After swapping:", a,b)
"""#re-decalare varaibles: variables can be re-declared multiple times. this is unlike in java
======================="""
n=10;
print(n)
n=30;
print(n)
"""#deleting a variable
====================="""
m=30;
print(m)
del m
print(m) #throws a name error

"""#input function: input() & raw_input(), this is different in python 2.x and 3.x
===============
#python 2.x, input() takes any type of data while raw_input() takes only strings data types
#python 3.x, we only have input() which takes only strings data types just like the raw_input()"""

num1=input("enter your age:")
num2=input("enter your number:")
print(num1+num2)
"""#type casting in python: this helps to use input() for number calculations
========================"""
num1=int(input("enter your age:"))
num2=int(input("enter your number:"))
print(num1+num2)
num1=float(input("enter your age:"))
num2=float(input("enter your number:"))
print(num1+num2)
#float can hold integer value while integer cannot hold float values
num1=int(input("enter integer value:"))
num2=int(input("enter float value:"))
print(num1+num2)

"""#formating output: this can be done by using % and {}
==================
# ---%d is used for int type
# ---%s is used for strings type
# ---%f & %g is used for float """

sal=20.2
name="scoot"
age=20
print("sal is:",sal)
print("name is:",name)
print("age is:",age)
print("name:%s age:%d sal:%g" %(name,age,sal)) #data type is not important
print("name:{} age:{} sal:{}".format(name,age,sal)) #value is important
print("name:{0} age:{1} sal:{2}".format(name,age,sal)) #by passing index value and value 
print("name:{} age:{} sal:{}".format(name,name,sal)) #accepts any value format



"""FOMATING IN PYTHON CAN ALSO BE DONE:
msg = f'From: {sender}\r\nTo: {receiver}\r\nConten-Type: text/plan; charset="utf-8"\r\nSubject: {theme}\r\n\r\n'


So, basically we have three different statements in python:
========================================================
1). Conditional statements--->If, Else & Elif statements

2). Loop statement--->While and For statements. While True means the while condition is true, go into the loop and perform the action.
 For loop is used when u know the range you want to iterate but while loop is used when u are not sure of the range u want to iterate. In addition regarding using For Loop, Two different cases of For loop are used, (1)==> Using IN RANGE, which expects 2 arguments/pamaraters i.e. initial, end, increment. (2)==>Using only IN, which specifies all the range from the first value to the last value. ALSO, EXIT FOR LOOP in RF is similar to break statement in python.
While creating a list in RF, U do not need to add equal sign to the @{...} to the create list keyword. While using the FOR LOOP in RF, the variable ${i} represents the INDEX and its value always starts from zero otherwise stated.
Example:Using while loop in date-picker
while month_year.text != 'december 2022': month and year selection
	next_click_calender.click()
	calender_date=driver.find_element.by....#date selection

3). JUMPING STATEMENTS:
   >>Break Jumping statement--->when you have a set of loop condition within a range and wishes to come out at a specific value
   >>Continous Jumping statement"""

#conditional statements examples:
#if, else and elif statments

a=10

if a>20:
    print("This statement is true")
else:
    print("This statment is false")

if True:
    print("This statement is true")
else:
    print("This statment is false")

if 0:
    print("This statement is true")
else:
    print("This statment is false")


#even and odd number
b=10
if b%2==0:
    print("Number is even number")
else:
    print("Number is odd number")

#multiple statements under if and else blocks and in a single lines
if True:
    print("welcome")
    print("enter")
    print("close")
else:
    print("not welcome")
    print("not enter")
    print("open")
if False:
    print("welcome")
    print("enter")
    print("close")
else:
    print("not welcome")
    print("not enter")
    print("open")
print("welcome") if True else print("not welcome")
print("welcome") if False else print("not welcome")
{print("welcome"),print("sit")} if True else {print("not welcome"),print("not sit")}

#u make use of elif statement when u have more of conditions to validate
u=10
if u==20:
    print("Two")
elif u==30:
    print("Three")
elif u==40:
    print("Four")
else:
    print("no valid value")


#loop statements/iterative statements: U must understand a range() for u to understand loop statement
print(list(range(10))) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(2,7))) #[2, 3, 4, 5, 6]

print(list(range(1,10,2)))  #[1, 3, 5, 7, 9] odd numbers
print(list(range(0,10,2)))  #[0, 2, 4, 6, 8] even numbers
print(list(range(10,1,-1)))  #[10, 9, 8, 7, 6, 5, 4, 3, 2]

print(list(range(-10,-2)))  #[-10, -9, -8, -7, -6, -5, -4, -3]
print(list(range(-10,-2,2)))  #[-10, -8, -6, -4]

#for loop: cares for range
#print 1 to 10 numbers
for i in range(10):
    print(i)
print("next command:")
for i in range(2,10,2):
    print(i)
print("next command:")
for i in range(10,1,-1):
    print(i)
print("next command:")

#while loop: does not care for range values, u must declare 3 things; initialization, condition, and increamentation
i=1
while i<=10:
    print(i)
    i=i+1
print("next command:")
i=10
while i>=1:
    print(i)
    i=i-1
print("next command:")

#jumping statements or transfer statements: here we have break and continue commands
for i in range(10):
    if i==5:
        break
    print(i)
print("next command")
for i in range(10):
    if i==5:
        continue
    print(i)

#number types:
x=10
y=10.5
print(type(x))
print(type(y))

#type casting:
print(float(x)) #float () converts integer to float
print(int(y)) #int() converts floats to integer

#buit-in functions on number types: max() and min() on numbers
print(max(10,20,30))
small=min(10,20,30)
print(small)

#Strings and string() in python: string is a collection of characters
name="john"
name1=str("scott")
print(name,name1)
#strings are immutable in python
name="john"
name1="john"
print(id(name))   #2536547356976  memory location
print(id(name1))  #2536547356976  memory location

name1=name1+"more names"
print(id(name1))   #2536547040688 different memory location
#operations on strings
str1="name"
str2=str1+"age"
print(str2)
str3=str1*10
print(str3)
#slicing [] operations on strings in python
str1="welcome"
print(str1[1:3]) # "el" the last values is always considered as n-1 operator
print(str1[:5]) #welcom
print(str1[2:]) #lcome
#ord() and chr(): ord() returns the ASCII code of the character while chr() returns character represented by a ASCII number
print(ord("z"))
print(chr(80))
#String() in python
#len() = returns the length of the string
#max() = returns character having the highest ASCII value
#min() = returns character having the lowest ASCII value
print(len("coding"))
print(max("coding"))
print(min("coding"))
#in and not in operators: used to check existence of string in another string, also known as membership operator
str1="programming"
print("gram" in str1) #it returns a boolean value
print("gram" not in str1)
#string comparism/using math operators in strings(>,<,<=,>=,==,!=) answers based on ASCII values
print('sim' == 'sim')
print("sim" != "simn")
print('arrow' > 'arow')
print('go' >= 'go')
print('went' < 'have')
print('meet' <= 'meat')
#iterating string using for loop
s='loop'
for i in s:
    print(i)
for i in s:
    print(s)
print('next command:')
#testing strings
s='welcome to python'
print(s.isalnum()) #isalnum()
print('welcome'.isalpha()) #isalpha()
print(s.isdigit()) #isdigit()
print('2020'.isidentifier()) #isidentifier()
print(s.islower()) #islower()
print(s.isupper()) #isupper()
print(s.isspace()) #isspace()
print('next command:')
#searching for strings
s='welcome to python'
print(s.endswith('thon'))
print(s.startswith('weli'))
print(s.find('come'))
print(s.find('become'))
print(s.rfind('o'))
print(s.count('p'))
print('next command:')
#converting strings
s='welcome to coding'
print(s.capitalize())
print(s.title())
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.replace('in','on'))
print('next command:')
#creating list in python:similar to arrays
list1=list()
print(list1)
print(list([22,31,61]))
print(list(['cod', 'code', 'coding']))
print(list('coding'))
print('next command:')
#accessing elements from a list
l=[1,3,5,7,9]
print(l[1])
print(l[3])
print('next command:')
#list common operators
l=[1,2,3,4,5,6,7,8,]
print(2 in l)
print(10 not in l)
print(len(l))
print(max(l))
print(min(l))
print(sum(l))
print('next command:')

# + and * operators in list:
list1=[1,2,3]
list2=[4,5]
print(list1+list2)
print(list2*3)
print('next command:')
list=[1,2,3,4,5]
for i in list:
    print(i)
    #print(i, end=" ") #using end="" prints the values in a single line otherwise that will be printed in multiple lines

print('next command:')
#common methods in list:
list3=[1,2,3,4,5,6,7]
list3.append(9) #returns None
print(list3)
print(list3.count(2)) #counts the index number from the list value
list4=[12,13]
list3.extend(list4)
print(list3)
#print(list3.extend(list4)) returns None
print(list3.index(12))
list3.insert(9,20)
print(list3)
list3.remove(20)
print(list3)
list3.reverse()
print(list3)
list3.sort()
print(list3)
print(list3.pop(5)) #5 is the index value
print('next command:')

#list comprehension:
#list5=[1,2,3,4,5,6,7,8,9]
list5=[x for x in range(10)] #this command stores values in the list
print(list5)
list5=[x+1 for x in range(10)]
print(list5)
list5=[x for x in range(10) if x%2 ==0]
print(list5)


#DICTIONARY IN PYTHON:
# It is very similar to HashMap in Java. is a datatype that helps to store, retrieve, add, remove, modify,
# values by using a key. They are mutable

#create a dictionary
dic1={'foods':'rice, beans, eggs', 'jobs':'QA Enginner'}
print(dic1)
#Other operations in dictionary
print(dic1['foods']) #retrieve
dic1['vacation'] = 'Dubai' #add
print(dic1)
dic1['foods'] = 'egg sauce' #modify
print(dic1)
del dic1['vacation'] #delete
print(dic1)
print('next command:')
#using for loop in a dictionary
dic2 = {'foods':'rice, beans, eggs', 'jobs':'QA Enginner', 'vacation':'Dubai'}
print('next command:')
#dic3 = {'a':'rice', 'b':'QA Enginner', 'c':'Dubai'}
for x in dic2:
    print(x, ":", dic2[x])
print('next command:')
#using len() in dictionary
print(len(dic2))
print('next command:')
#using comparism/math operators
dic2 = {'foods':'rice, beans, eggs', 'jobs':'QA Enginner', 'vacation':'Dubai'}
dic3 = {'a':'rice', 'b':'QA Enginner', 'c':'Dubai'}
print(dic2==dic3)
print(dic2!=dic3)
print('next command:')
#common methods in dictionary
dic2 = {'foods':'rice, beans, eggs', 'jobs':'QA Enginner', 'vacation':'Dubai'}
dic3 = {'a':'rice', 'b':'QA Enginner', 'c':'Dubai'}
print(dic2.popitem()) #returns the key and value and remove it from the dictionary
print(dic2)
print(dic3.keys()) #returns in form of tuples
print(dic3.values()) #returns in form of tuples
print(dic3.get('a'))
print(dic3.pop('c')) #it return the key value and removes the item from the dictionary
print(dic3)
print(dic3.clear()) #delete all from dictionary and returns None
print('next command:')

#Tuples in python: They are very similar to list, but once created, cannot be modified. They are immutable
#create a tuple
t=1,2,3,4,5
t1=() #empty tuple
t2=(1,2,3,4,5)
t3=([6,7,8,9])
t4=tuple('abc') #tuple keyword returns each item as a key
print(t1)
print(t2)
print(t3)
print(t4)
print(t)
print('next command:')
#tuple fuctions: function is not different from methods, u pass the variable inside of a fuction but u use the variable to call methods by using dot'.'
print(max(t2))
print(min(t2))
print(len(t2))
print(sum(t2))
print('next command:')
#using for loop in tuple
for x in t2:
    #print(x, end=" ")
    print(x)
print('next command:')
#slicing operation in tuples: this is based on values not index
t2=(1,2,3,4,5)
print(t2[:3])
print(t2[2:])
print(t2[1:3])
print('next command:')
#in and not in operators in tuples
print(2 in t2)
print(6 in t2)
print(7 not in t2)
print('next command:')


#FUNCTIONS:
#Functions are re-usable pieces of code and they help to run a set of statements multiple times. Wheneva u create a function,
#u expect a value from the return

#when a function prints a value
def fun1(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i
    print(result)
fun1(20,30)

#when a function returns a value
def fun2(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i
    return result
call1=fun2(10,25)
print(call1)
#if u don't specify a return value, always None is return
def fun3(start, end):
    if (start>end):
        print('start value is greater')
        return
    result=0
    for i in range(start,end+1):
        result=result+i
    print(result)
r=fun3(20,10)
print(r)
# and also without specifying return keyword, the function default return is None(we also have pass keyword)
def func5():
    v=200
    #return
print(func5())


#Global and Local variables
varg=100
def fun():
    varl=200
    print("this is a global variable:", varg)
    print("this is a local variable:", varl)
fun()
#using global keyword inside of a function
def fun2():
    global var
    var=300
    print(var)
fun2()
#how to pass arguments/values to a function
#arguments with default values(positional arguments)
def fun(i,j=5):
    print(i,j)
fun(2)
fun(3,6)
#passing a keywords arguments
def names(ename,eadd):
    print(eadd+" "+ename)
names('scott','street') #positional argument
names(ename='john', eadd='street2') #keyword argument
def fun(a,b,c):
    print(a,b,c)
fun(10,b=30,c=40)
fun(1,2,c=1) #positional arguments must appear before keyword arguments
#using return keyword on ariables within a function
def param(a,b):
    if a>b:
        return a,b
    else:
        return b,a
r=param(10,20)
print(r) #the results are treated as a tuple

#file handing: open and close a file and write 'w'
# file1=open('C:\Users\bened\PythonProgramming\file_handling', 'w')
# file1.write('This is line one\n')
# file1.write('This is line two\n')
# file1.close()

#Reading data from a file: Read 
# file1=open('C:\Users\bened\PythonProgramming\file_handling', 'r')
# print(file1.read()) #read all the content from the file
# print(filw1.read(12) #read only 12 index characters
# file1.close()

#Readlines: readlines shows in array format
# file1=open('C:\Users\bened\PythonProgramming\file_handling', 'r')
# print(file1.readlines()) #read all the content from the file
# print(filw1.readlines(12) #read only 12 index characters
# file1.close()

#Readline: Read only one line
# file1=open('C:\Users\bened\PythonProgramming\file_handling', 'r')
# file1.write('This is line three\n')
# file1.write('This is line four\n')
# file1.close()

#Append data to a file
# file1=open('C:\Users\bened\PythonProgramming\file_handling', 'a')
# print(file1.read()) #read all the content from the file
# print(filw1.read(12) #read only 12 index characters
# file1.close()

#using for loop in reading lines in a file
#file1=open('C:\Users\bened\PythonProgramming\file_handling', 'r')
# for l in file1:
#     print(l)
# file1.close()

#Class and Methods:
#creating basic class and object which includes methods
class MyClass():
    def fun(self):
        pass
    def func(self,name):
        print('The name is:', name)
obj=MyClass()
obj.fun()
obj.func('scott')
#creating instance method and static method NB: In Java, we have both static methods and static variables but in
# in python, we only have static method
class MyClass:
    def fun(self):
        print('instance method') #must call with an object
    @staticmethod
    def func(): #static method doesnt take any parameter
        print('static method') #called/invoke while calling a class/object creation
    @staticmethod  #static methos with parameters
    def fun1(name,add):
        print('The name is:' ,name, 'The address is:' ,add)
obj=MyClass()
obj.fun()
MyClass.func()
MyClass.fun1('smith','street')

#Declaring variables inside a class
class MyClass:
    x,y=100,200
    def fun(self):
        print(self.x +self.y)
    def fun1(self):
        print(self.x *self.y)
obj=MyClass()
obj.fun()
obj.fun1()
#Local/Global/Class variables
a,b=2,4
class MyClass:
    m,n=5,6
    def fun(self,e,d):
        print(e+d)
        print(self.m+self.n)
        print(a+b)
obj=MyClass()
obj.fun(7,8)
#same values of local/global and class variables
a,b=3,4
class MyClass:
    a,b=5,6
    def fun(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(globals()['a'] +globals()['b'])
obj=MyClass()
obj.fun(7,8)
#creating multiple objects for a single class
class MyClass:
    def show(self):
        print('welcome')
obj=MyClass()
obj.show() #occupies different memory location
obj2=MyClass()
obj2.show() #occupies different memory location
#named object and nameless object
class MyClass:
    def show(self):
        print('welcome')
obj=MyClass() #Named object
obj.show()
MyClass().show() #Nameless object
#How to check memory locations of the objects
class MyClass:
    def fun(self):
        pass
obj=MyClass()
obj2=MyClass()
obj3=MyClass()
obj4=obj
print(id(obj))
print(id(obj2))
print(id(obj3))
print(id(obj4))
print(obj is obj2)
print(obj is obj4)
print(obj2 is not obj3)
print(obj is not obj4)

#Constructor, object, and class
#How to create and use a constructor in python
class MyClass:
    def fun(self):
        print('good morning')

    def __init__(self):  #called/invoked at the time of object creation
        print('this is a constructor')
obj=MyClass()
obj.fun()
#Converting local variables into class variables
# NB: we define local variables within a method and access it also within that method
class MyClass:
    def fun(self,val1,val2):
        print(val1)
        print(val2)
        self.val1=val1
        self.val2=val2
    # def __int__(self,val3,val4):
    #     print(val3+val4)
    #     self.val3=val3
    #     self.val4=val4
    # def fun3(self):
    #     print(self.val3+self.val4)
    def fun2(self):
        print(self.val1+self.val2)
# obj1=MyClass(4,5)
obj=MyClass()
obj.fun(2,3)
obj.fun2()
# obj1.fun3()

class MyClass:
    def __init__(self,val1,val2):
        print(val1)
        print(val2)
        self.val1=val1
        self.val2=val2
    def fun2(self):
        print(self.val1+self.val2)
obj=MyClass(5,6)  #u can only pass values here with only constructors.
obj.fun2()
#how to call current class method in another method
class MyClass:
    def fun(self):
        print('this is method 1')
        self.fun1(5)
    def fun1(self,a):
        print('this is method 2:',a)
obj=MyClass()
obj.fun()
#constructor with arguments
class MyClass:
    var1='smith'
    def __init__(self,name):
        print(name)
        print(self.var1)
obj=MyClass('scott')
#create a class name Emp, constructor that accepts eid,ename,esal and displays method
class Emp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eid,self.ename,self.esal)
        print('eid:{} ename:{} esal:{}'.format(self.eid,self.ename,self.esal))
        print('eid:%d ename:%s esal:%d' %(self.eid,self.ename,self.esal))
obj=Emp(102,'smith',2000)
obj.display()
#String constructor(__str__) is invoke when you print reference varaible of the object, so no need to call with object
class MyClass:
    pass
obj=MyClass()   #obj is the reference variable
print(obj)  # <__main__.MyClass object at 0x000002B1FDC8D400>
#But when u specify the string, it returns a value. it can only return strings and not numbers or anything else
class MyClass:
    def __str__(self):
        return 'welcome'
obj=MyClass()
print(obj)
#When u print the reference variable, __str__ is invoke and it will be executed and it only returns a value and not print
class Emp:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def __str__(self):
        #print(self.eid,self.ename,self.esal)
        return('eid:{} ename:{} esal:{}'.format(self.eid,self.ename,self.esal))
        #print('eid:%d ename:%s esal:%d' %(self.eid,self.ename,self.esal))
obj=Emp(102,'smith',2000)
print(obj)
#Using __del__ is authomatically be invoke whenever you destroy the object
class MyClass:
    def __del__(self):
        print('Destroyed')
obj1=MyClass()
obj2=MyClass()
del obj1

# Inheritance
#single inheritance
class A:
    def m1(self):
        print('this is method 1 from class A')
class B(A):
    def m2(self):
        print('this is method 2 from class B')
c1=B()
c1.m2()
c1.m1()
print('next command:')
class A:
    a,b=2,3
    def m1(self):
        print(self.a+self.b)
class B(A):
    x,y=4,5
    def m2(self):
        print(self.x+self.y)
c=B()
c.m1()
c.m2()
print('next command')
#multi-level inheritance: multple parents and  multiple childs
class A:
    a,b=2,3
    def m1(self):
        print(self.a+self.b)
class B(A):
    x,y=4,5
    def m2(self):
        print(self.x+self.y)
class C(B):
    s,r=6,7
    def m3(self):
        print(self.s+self.r)
c=C()
c.m1()
c.m2()
c.m3()
print('nect command:')
#Hierarchy inheritance: one parent multiple child classes
class A:
    a,b=2,3
    def m1(self):
        print(self.a+self.b)
class B(A):
    x,y=4,5
    def m2(self):
        print(self.x+self.y)
class C(A):
    s,r=6,7
    def m3(self):
        print(self.s+self.r)
c=B()
c.m1()
c.m2()
c1=C()
c1.m1()
c1.m3()
print('next command:')
#Multiple inheritance: Multiple parents with one child
class A:
    a,b=2,3
    def m1(self):
        print(self.a+self.b)
class B:
    x,y=4,5
    def m2(self):
        print(self.x+self.y)
class C(A,B):
    s,r=6,7
    def m3(self):
        print(self.s+self.r)
c=C()
c.m1()
c.m2()
c.m3()
print('next command:')
#Using super() keyword in inheritance: used to invoke parent class methods, to invoke parent class variables and
# to invoke parent class constructor
# used to invoke parent class methods:
class A:
    def m1(self):
        print('This is the parent class method m1:')
class B(A):
    def m2(self):
        print('This is the child class method m2:')
        super().m1()
o=B()
o.m2()
print('Next command:')
# To invoke parent class variables:
class A:
    a,b=1,2
class B(A):
    x,y=3,4
    def m1(self,m,n):
        print(m+n)
        print(self.x+self.y)
        print(self.a+self.b)
o=B()
o.m1(5,6)
print('Next command:')
a,b=7,8
class A:
    a,b=1,2
class B(A):
    a,b=3,4
    def m1(self,a,b):
        print(a+b)
        print(self.a+self.b)
        print(super().a+super().b)
        print(globals()['a']+globals()['b'])
o=B()
o.m1(5,6)
print('next command:')
# To invoke a parent constructor
class A:
    def __init__(self):
        print('This is a constructor')
class B(A):
    pass

o=B()
print('next command:')
class A:
    def __init__(self):
        print('This is a constructor')
class B(A):
    def __init__(self):
        print('This is a constructor for child class')
        super().__init__()
o=B()
print('next command:')
class A:
    def __init__(self):
        print('This is the first constructor')
class B(A):
    def __init__(self):
        print('This is a constructor for child class')
        A.__init__(self)  #another method of invoking without using a super keyword but with class name
o=B()
print('next command:')

#POLYMORPHISM: we can use polymorphism to achieve same task for multiple scenarios sya by clicking on a button that
# comes in various forms and shapes but still achieve same purpose for same task. we regard this as an objects that
# comes in many types or forms. This means same thing can have multiple behaviours. This polymorphism concept can be
# by using overiding and overloading.
# OVERRIDING: means having two methods with the same name but doing different tasks. It means that one method overides
# the other. so if there is a superclass/parent class and subclass/child class with same methods, by executing one method,
# the other method will be executed and they both perform their respective task. This is also applicable to variables.
#Oveririding Variable:
class A:
    name='Scott'
class B(A):
    name='Smith'
o=B()
print(o.name)
print('next command:')
class A:
    name='Scott'
class B(A):
    pass
o=B()
print(o.name)
print('next command:')
#Overriding methods:
class OpBank:
    def rateofinterest(self):
        return 0
class SBank(OpBank):
    def rateofinterest(self):
        return 2.5
        #super().rateofinterest()
o=SBank()
print(o.rateofinterest())
o1=OpBank()
print(o1.rateofinterest())
print('next command:')
# Same method but behaves differently: Overloading method of polymorphism
class Human:
    def sayHello(self,name=None):
        if name is not None:
            print('Hello' + name)
        else:
            print('Hello')
o=Human()
o.sayHello()
print('next command:')
class Human:
    def sayHello(self,name=None):
        if name is not None:
            print('Hello' + name)
        else:
            print('Hello')
o=Human()
o.sayHello('Scott')
print('next command:')
class Bird:
    def fly(self,name=None):
        if name=='parot':
            print('can fly')
        if name=='fowl':
                 print('cannot fly')
        if name is None:
               print('No input')
o=Bird()
o.fly()
#Encapsulation: This is by resisting access to methods and variables and making them private by putting (__) infront of them
# U can only access them within the class and within the method but public methods and variables can be access from anywhere
class A:
    __x=1
    def private(self):
        print(self.__x)
o=A()
o.private()
#print(A.__x) : cannot be accessed outside of the class
print('next command:')
class A:
    def __m1(self):
        print('This is a private method m1')
    def m2(self):
        print('This is a public method m2')
        self.__m1()
o=A()
o.m2()
print('next command:')
#o.m1() : cannot be accessed outside of the class
#We can access private variables outside of the class indirectly using methods
class A:
    __a=3
    def m1(self,b):
        self.__a=b
    def m2(self):
        print('The value of the private variable', self.__a)
o=A()
o.m1(4)
o.m2()
print('Next command:')

#Abtract Class: They are classes that conatains one or more abstract methods. iT requires a subclass for their implementation.
#Is like a mock up class used to design a prject without implementing coz of minimal knowledge we have for the project.
#we use them when we dont know how to design/implement based on the requirement, so we can then create abstract class with multiple abstract methods
# and once we understand how to implement the design, then we can create multiple classes and methods and implement them.
#abstractclass is also important for security reasons.

from abc import ABC, abstractmethod
class A(ABC): #ABC is a pre-defined abstract class
    @abstractmethod
    def m(self):
        None
class B(A):
    def m(self):
        print('This is a method used to implement the abtract method')
o=B()
o.m()
print('next command:')
class Food(ABC):
    @abstractmethod
    def eat(self):
        pass
class Beans(Food):
    def eat(self):
        print('He eats beans')
class Rice(Food):
    def eat(self):
        print('He eats rice')
o=Beans()
o.eat()
o1=Rice()
o1.eat()
print('next command:')
class A(ABC):
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
class B(A):
    def m1(self):
        print('This is m1')
        #self.m2()
class C(B):
    def m2(self):
        print('This is m2')
o=C()
o.m2()
o.m1()
print('next command:')
#Create a constructor in abstractclass
class A(ABC):
    #@abstractmethod
    def __init__(self,a):
        self.a=a
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):
        pass
class B(A):
    def m1(self):
        print(self.a+2)
    def m2(self):
        print(self.a-4)
o=B(6)
o.m1()
o.m2()
print('next command:')

#MODULES: A module is a python file which contains sets of functions you want to include in your application.
# The content of a module can be accessed with the import statement
#Module 1:
def add(num1,num2):
    print(num1+num2)

def sub(num1,num2):
    print(num1-num2)

# add(10,20)
# sub(100,50)
#This two functions are exactly same in module2
def school1():
    print("Primary school 1")
def school2():
    print("High school 1")


#Importing class with same method from module2
class Veg:
     def display(self):
         print("This is spinach")

#Finding how many classes are in a module
class A:
    def pas(self):
        pass
class B:
    def display1(self):
        print('display1')
    def display2(self):
        print('display2')

#Using package file/folder for module1
def m1():
    print('This is from m1')

#Module 2:
#This two functions are exactly same in module1
def school1():
    print("Primary school 2")
def school2():
    print("High school 2")

#Importing class that has same method from module1
class Fruits:
     def display(self):
         print("This is mango")

#Finding how many functions are in a module
def display1(self):
    print('display1')
def display2(self):
    print('display2')
#Using package file/folder for module2
def m2():
    print('This is from m2')

#ModuleCall:
#IMPORTING A MODULE FUNCTION
#Approach1
import module1
module1.add(5,10)
module1.sub(5,3)
print('next comand:')

#Approach2
from module1 import add,sub
add(5,5)
sub(5,3)
print('next command:')

#Approach3
from module1 import *
add(4,5)
sub(7,3)
print('next command:')
#Importing same functions from two different modules: Only when the methods has same name
from module1 import * #This import is only applicable to functions in module1
school1()
school2()
from module2 import *  #This import is only applicable to functions in module2
school1()
school2()
print('next command:')
#Importing same functions from two different modules:
import module1
import module2
module1.school1()
module1.school2()
module2.school1()
module2.school2()
print('next command:')
#IMPORTING A CLASS
import module1
import module2
o1=module1.Veg()
o1.display()
o2=module2.Fruits()
o2.display()
print('next command:')
from module1 import *
from module2 import *
o1=Veg()
o1.display()
o2=Fruits()
o2.display()
print('next command:')
#Finding how many classes are in a module1
from module1 import *
print(dir(module1))
print('next command:')
#Finding how many functions are in a module2
from module2 import *
print(dir(module2))
print('next command:')

"""#PackageModule:
===============
Client Program:
===============
#For more than one package, please import all the package paths and directories."""

import sys
sys.path.append("C:/Users/bened/PycharmProjects/pythonPractice/BasicCommands") #change directory to farward slash
import module1
import module2
module1.m1()
module2.m2()
# from module1 import *
# from module2 import *
# m1()
# m2()

#EXCEPTIONS: They are programes that restrict the codes from running. In python, they are considered as errors.
#Errors is of two types; Syntax error and Programming error.
#For one try block, we can have multiple except blocks
#CASE1: Thrown exception: handled: except-->finally, block will be executed
#CASE2: Thrown exception: not handled-->finally block will be executed
#CASE3: Not thrown exception: else -->finally block will be executed

print('The program has started executing')

try:
    print(10/0) #ZeroDivisionError:
except ZeroDivisionError: #This will only execute only when exception error occurs
    print('Entered into except block - Handled exception')
except TypeError:
    print('Entered into except block - Handled exception')
except SyntaxError:
    print('Entered into block - Handled exception')
else:  #This does not handle any exception error
    print('Entered into else block ...')
finally:
    print('Entered into finally block...')
print('The program has finnished executing ')

print('next command:')

#RAISE EXCEPTION: This is when we raise create our own exception
def enterage(age):
    if age < 0:
        raise ValueError('Only positive integers are allowed')
    if age % 2==0:
        print('Age is an even number')
    else:
        print('Age is an odd number')
try:
    num=-3
    enterage(num)
except ValueError:
    print('Only positive integers are allowed')
except:
    print('Something went wrong')
print('next command:')

#Handling exception using exception objects
try:
    number=one
    print('The number is', number)
except NameError as ex:  #ex is the exception object which returns an inbuilt expression
    print('Exception:', ex)

#LAMBDA FUNCTION:
# They are regarded as an anonymous function that take any number as an arguments, but can only return one expression
# lambda arguments:expression
x= lambda a : a+10
print(x(5))  #Passing single variable
x=lambda a,b:a*b
print(x(2,3))  #Passing multiple variables
x=lambda a,b,c:a+b+c
print(x(2,4,6))  #Passing multiple variables
#Lambda function helps to simplify and reduce our code lines
print('next command:')
def add(x):
    x=x+10
    return x
print(add(10))
print('next command:')

#Python *args(arguments) and **kwargs(key arguments):
#Used to define function and methods and pass number of parameters
# *args is just a convention and u can use anything that is valid identifier e.g: *myargs is perfectly valid

def sum(*args):
    a=0
    for i in args:
        a+=i #a=a+i
    print('The sum is', a)
sum(1,2,3,4)  #Can take as many paramters as possible
print('next command:')
#By using with list
def my_list(a,b,c): #This takes excatly same argumemts specified
    print(a,b,c)
args=[1,2,3]
my_list(*args)
print('next command:')
#Using **kwargs
# Syntax: func_name(name='tim',team='school')
def my_args(a,b,c):
    print(a,b,c)
dic={'a':'one','b':'two','c':'three'}
my_args(**dic)
print('next command:')
def my_kwargs(**kargs):  # ** represents key and value
    for i,j in kargs.items():
        print(i,j)
my_kwargs(Name='Scott', Age='20', Grade='A')
print('next command:')



"""COLLECTION LIBRARY :
====================
list[]...mutable
tuple()-immutable
set-->is unordered or unset. rep. by {}..mutable
dictionary...mutable..{keys,values}

Function in python is usually denoted with () while keyword is denoted separately
Tuple is immutable while list is mutable(we can make changes on the data)
Index: Elements we can accessed only through index

LIST..Mutable..Ordered..Index
------------------------------------------------------------------------------
TUPLE..Immutable..Ordered..Indexed
-------------------------------------------------------------------------------
SET ..Mutable..Unordered..Unindexed
--------------------------------------------------------------------------------
DICTIONARY..Mutable..Unordered..Unindexed(keys and value based datas)
----------------------------------------------------------------------------------

FUNCTION: A set of statements which will perform a task. 
1. Function declaration/creation
2. Calling the function/invoking fuction.
These are user defined fuctions ie. we defined these sets of functions. 
Other type of fucntion is built-in function. they are different from built in functions. 
User-defined functions must start with def.

1. Positional arguments in a function 
2. Keyword arguments in a function

NB: Positional arguments must appear before a keyword arguments
You can call a function multiple times within a function

PYTHON supports structured + object oriented programming concept this is why we can execute our programe 
without having a class or object programming concept.
This is different with JAVA and C++. They only support Object oriented programming concept
oops: Object Oriented Programming Concept
OOPS supports:
1. Class
2. Object
3. Inheritance
4. Polymorphism

CLASS:Is a category. Class is a logical entity while Objects are physical entity.
Technically, class is a collection of variables(attributes) and methods(behaviors)
You can create multiple objects from a class. the object basically depends on the class.
it takes all its values from the class. Class is a blue print. Class does not occupy any space in the memory while
Objects occupies a space in the memory because they are of the a physical quantity. Objects are independent.
Function and Methods are very similar but different in various aspects.
Function we can create without a class in python(structured+object oriented concept) while,
Method is only created in side of a class.
U must create an object within a class to access the class cos the class is a logical entity 
while an object is a physical entity
A function/method inside a class must have a 'self' inside to verify that it is a function/method class.
A 'Pass' is like a None within a function inside of a class.


two types of methods:
1. Instance methods(we can only call through objects)--->self is rep. a class and not a parameter.
2. Static methods(we can directly call using class)---> self is considered as a parameter in a staticmethod. you need to pass a paramter to self.
NB: It is possible to call static method by objects but it is advisable as it is always better to call static method through the class.
@staticmethod--->Annotation

CLASS VARIABLE:This is diff from the global and local variables.

METHOD:
=========
give any name
return the values
method cantake arguments and parameters
we use an object to invoke the method

CONSTRUCTOR: A constructor name is fixed:
=============
def __init__(self):
constructor will not return any value. but there is an exception for another type of constructor(__str__) constructor which accepts only a string value
constructor can also take arguments/parameters
constructor will be called at the time of object creation itself.

def....means a default
 you can also create a class variable inside a method or a constructor only by using self.varaible=...keyword.
if the values belongs to the constructor or even the method. they cannot be accessed by other methods but only by their method or constructor.

INHERITANCE:
============
Inheritance supports only Object Oriented Programming concepts and does not support Object based Programming concepts just like class and object
Inheritance is basically acquiring all the attributes(variables) and behaviours(methods) from one class to another class.
E.g: From parent to child, all attributes and behaviours are transfered to the each other.
class A --->a,b,c m1() m2() --->A is parent of B class (Based/Super class)
class B(A)--->x,y,z m3() --->B is a child of A class (Sub/derived class)
The main purpose/objective of inheritance is for code reusability and avoid code duplication.

4types of inheritance in python:
==================================
1). Single (One parent, one child inheritance)
2). Multi level(a parent/class to multiple parents/class)
3). Heirarchy(one parent,multiple class and class contents varies)
4). Multiple(multiple parents and one child)
In coding standard: Wheneva you create a class, pls always start with a capital letter. Unlike creating variables that always starts with small letters.


We can also have an overriding scenario/method in an inheritance oops method: we can see this both in methods and also in variables.
This is when a method is repeated single or multiple times in a different class, also same with variables.
In this second case of overriding the variables, when we call the object, we can with the variable name but only that we need to print as well cos we do not have any method.
To further print the varaible from the parent class, we need to create a new method so as to access this variable from the parent class.

POLYMORPHISM:
This is when something has mutiple values e.g: shape;circle,rectangle, square etc.  we can see this in methods. It is not fully integrated in python but rather in Java.

MODULES AND PACKAGES IN PYTHON:
Modules is a collection of functions and classes(variables, methods)
NB: When a function is created inside a class, self is required for passing value or any other inputs but when a function is created without a class, self is not required for passing any value.
You can import a module with either:
1). Import "MODULENAME"--->You must use module name to invoke or call the function eg. module.uni
2). from "modulename" import "spefic function name"--->You only need to call the function or method by name. No need to invoke the module name.
3). from "modulename" import *(imports all files from the module)

When defining a class, we use () if the class is extending from a parent class, otherwise not applicable. 

PACKAGE: This is a collection of modules. it is of higher scale than the module.
Package --->Modules---->Class(methods&Variables)
NB: We cannot directly import a package inside a 'callModule' bcoz they are in a package and not directly in module file.

EXCEPTION HANDLING: This is an event which will cause program termination.(Use try,except and else) to handle exceptions.
ERROR:(Syntax error and Programming error)
In python, all exceptions are considered as an error. This is not applicable in other languages like Java, C++, etc.

try:
{
statements
}
except-->executes only when exception occured.
{
statements
}
else--->executes only when exception does not occur.
{
statements
}
finally--->always executes
{

}

SCROLL IN PYTHON SELENIUM
=========================
1). Scroll down the page by pixel:
	driver.execute_script("window.scrollBy(0,500)","")
2). Scroll to an element
	driver.execute_script("arguments[0].scrollIntoView();",Element)
3). Scroll to the end of the page
	driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")"""
