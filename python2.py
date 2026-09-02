"""  print("Hello world")
age = 10
print(age)
print(type(age))
a,b,c = 10, 20, 30
print(a,b,c)
a=b=c=10
print(a,b,c)
 a=20 
print("first assigned value:",a)
a=40
print("variable is re-intialised,now value is:",a)
print(type(a))
 g= 0.12e-3
print(g)
a= 2e2
b = 2E2
c = 2e3
print(a)
print(b)
print(c)
print(type(a))
a = 3+5j
b = 2-5.5j
c = 3+10.5j
print(a)
print(b)
print(c)
print(a+b)
print(b+c)
print(c+a)
 a = True 
b = False 
print(a)
print(b)
print(a+a)
print(a+b)
 print("hi")
a = "Amit"
a = bool(a)
print(type(a))
print(a)
a = 5
a = bool(a)
print(type(a))


print(a*102)
 str1 = "hello" 
str2 = "world"
str3 = this
is
a
string
print(str1)
print(str2)
print(str3)
 x = [10, 20, 30, 100, 0, 15]
y = bytes(x)
print(type(y))
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])
print(y[5])
 x = [10, 20, 30, 40, 50, 60, 15]
y = bytes(x)
for  a in y:
    print(a)
 x = [10, 20, 30, 40, 50, 800, 0, 56, 90]
y = bytes(x)
y[0] = 30 
a = range(5)
print(a)
for x in a:
    print(x)
 Range(7)
Range(2.10) 
Range(2,10,3) 
Range(10,2, -2) 
Range(10,2)
print(range(7)) 


 a = 89 #any number is True except 0 or none
a = "Amit"  #string us True except empty string
print(bool(a)+3)
a = 5
print("123"+str(a))
print(a+int("123"))


 a = 10
n = float(a)
print(n)
print(type(n)) 


 a = 10 
b = 20 
c = (a if a<b else b)+20
print(c) 

 age1 = 24 
age2 = 16
eligibility1 = "eligible" if age1 >= 18 else "not eligible"
eligibility2 = "eligible" if age2 >= 18 else "not eligible"
print(f"Age 1: {age1}, Eligibility: {eligibility1}")
print(f"Age 2: {age2}, Eligibility: {eligibility2}")


a = 10
b = 20
c = -5 
d = (a if a<c else c)  if a<b else (b if b<c else c)
print(d)


a = 10
b = 20
c = -5 
d = (a if a>c else c)  if a>b else (b if b>c else c)
print(d)   
 """


"""for and"""

""" a = 10 
b = 3
c = a+b    # +,-,*,/,%,**,//
print(c) """



""" c = (12 and 5) + 9
print(c) """



"""for or"""

""" c = (-34 or 5)+9
print(c)


c = ("abcd" or "1234")+ "rest"
print(c)

c = ("" or "1234")+ "rest"
print(c)


c = ("" or 12)+ 12
print(c)

c = (5 or 7)+ 3
print(c) """


""" a = 10 
b = 20 
c = (a<b)+23*(34 and 0)- (5 or 4)
print(c) """

"""assignment operators in python"""
"""operator - "=" """
""" a = 5
b = 6
x = a+b
print(x) """


""" a = 10
print(a)
print(-a)
 """

""" text = "Welcome to python programming"
print("Welcome" in text)
print("welcome" in text)
print("nireekshan" in text)
print("Hari" not in text)
 """


""" a = 15
b = 15
print(id(a))
print(id(b)) """

""" a = 25
b = 25
print(a is b)
print(id(a))
print(id(b))


a = 30
b = 25
print(a is b)
print(id(a))
print(id(b))
 """


""" not in ; is not """

""" input("Enter the name")
print("You entered name as:","saloni")


a = (input("Enter Num1"))
b = (input("Enter Num2"))
c = a+b
print(c)


a = int(input("Enter Num1"))
b = int(input("Enter Num2"))
c = a+b
print(c)


a = float(input("Enter Num1"))
b = float(input("Enter Num2"))
c = a+b
print(c) """


""" a = int(input("principal amount"))
b = int(input("rate"))
c = int(input("time"))
d = (a*b*c)/100
print(d)


a = float(input("principal amount"))
b = float(input("rate"))
c = float(input("time"))
d = (a*b*c)/100
print(d) """



""" a = eval(input("Enter any value"))
b = eval(input("Enter any value"))
print(a)
print(type(a))  """


""" from sys import argv 

a = eval(argv[1])
b = eval(argv[2])
c = a+b
print(c) """


#print("hi")


""" print("hi")

from sys import argv 
num1 = eval(argv[1])
num2 = eval(argv[2])
num3 = eval(argv[3])
c = num1+ num2 + num3 
print(c)

print(argv[1])
print(argv[2])
print(argv[3]) """

""" from sys import argv


print("The length of values:", len(argv))
 """


""" str1 = "Rajeev's Dairy"
str2 = 'Rajeev said  "I am a good boy" '
print(str1)
print(str2) """



""" c = "" + 34-4
print(c)      #it is a error """

#c = bool("") +34-4
#print(c)

#c = bool("ihkh") + 34-4
#print(c)     # the output well be 30 

""" 
str1 = "python"
print(str1[0])
print(str1[len(str1)-1])
print(str1[-1])
print(str1[-len(str1)])  

for x in range(len(str1)): 
    print(str1[x])

for x in range(-len(str1), 0):
    print(str1[x])

for s in str1:
    print(s) 

for x in range(-len(str1), 0, 1):
    print(str1[x])
 """



""" str1 = "Python in GLA CL2"
print(str1)
print(str1[ : :])
print(str1[2:6:2]) 
print(str1[10:13:])
print(str1[10:12:2])
print(str1[13:9:-1])
print(str1[-50:90:]) """


""" name = "Balayya"
print(name)
print(name[0])
name[0] = "X"   #str' object does not support item assignment """



""" a = "Python"
b = "Programming"
print(a+b)


a = "Python"
b = 4 
print(a+b)


a = "Python" 
b = 3
print(a*b) 


a = "Python"
b = 3.5
print(a*b)


print("Python" + "in GLA CL2")
print("Python"*3)
print("Python"*3.5)  # can't multiply sequence by non-int of type 'float' """



""" print('P' in "Python")
print('z' in "python")
print('on' in "python")
print('pa' in  "python")

print('b' not in "apple") """


""" s1 = "abcd" 
s2 = "abcdefg"
print(s1==s2)
if(s1==s2):
    print("Both are same")
else:
    print("not same")


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(s1==s2)
if(s1==s2):
    print("Both are same")
else:
    print("not same")
 """

""" s1 = input("Enter first string:")
s2 = input("Enter second string:")
output = "Same" if s1 == s2 else "Not Same"
print(output)
 """



""" s1 = "Amit Singh"
print(len(s1.rstrip().lstrip())) #it will remove the space from both side of the string and then it will count the length of the string 

s1 = "Amit Singh"
print(len(s1.strip())) #it will remove the space from right side of the string and then it will count the length of the string
 """


""" s1 = "python is a programming language. Python is easy to learn. Python is used in many applications."
print(s1)
print(s1.count("Python"))  #it will count the number of times "Python" is present in the string s1
print(s1.find("Python"))   #it will return the index of the first occurrence of "Python" in the string s1
print(s1.index("Python"))  #it will return the index of the first occurrence of "Python" in the string s1
print(s1.find("zython",35))
print(s1.index("zython",35))

output = "Yes" if s1.find("Python")!= -1 else "NO"
print("output")
output = "Yes" if "Python" in s1 else "NO"
print("output") """


""" s1 = "Java programming language"
s2 = s1.replace("Java","Python")
print(s1)
print(s2) """

""" s1 = "python is a programming language. Python is easy to learn. Python is used in many applications."
print(id(s1)) 
s2=s1.count("Python")
print(id(s2))
print(s2)
for i in s1:  
    print(i,s1.count(i) if s1.count(i)>2 else None) """



""" s1 = "Raesh, Suresh, Fazal, Kumar"
s2=s1.split()  #default delimiter is " "
print(s1, type(s1))
print(s1, (type(s2)))
for item in s2:
    #print(item)
    print(item,s1.count(item)) """



""" dob = input("Enter your date of birth in dd-mm-yyyy format: ")
year1 = dob.split("-")[2]
year2 = dob.split("-")[1]
year3 = dob.split("-")[0]
print(year1)
print(year2)
print(year3) """


""" l1 = ["22", "11", "2002"]
s1 = "/".join(l1)
print(s1)
print(type(s1)) """

