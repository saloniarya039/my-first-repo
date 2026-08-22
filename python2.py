""" print("Hello world")
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
print(c+a) """
""" a = True 
b = False 
print(a)
print(b)
print(a+a)
print(a+b) """
""" print("hi")
a = "Amit"
a = bool(a)
print(type(a))
print(a) """
""" a = ""
a = bool(a)
print(type(a))
print(a*102)"""

# str1 = "hello" 
#str2 = "world"
#str3 = """this
#is
#a
#string"""
#print(str1)
#print(str2)
#print(str3)
""" x = [10, 20, 30, 100, 0, 15]
y = bytes(x)
print(type(y))
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])
print(y[5]) """
""" x = [10, 20, 30, 40, 50, 60, 15]
y = bytes(x)
for  a in y:
    print(a) """
""" x = [10, 20, 30, 40, 50, 800, 0, 56, 90]
y = bytes(x)
y[0] = 30 """
""" a = range(5)
print(a)
for x in a:
    print(x) """
""" Range(7)
Range(2.10) 
Range(2,10,3) 
Range(10,2, -2) 
Range(10,2)
print(range(7))  """ 


""" a = 89 #any number is True except 0 or none
a = "Amit"  #string us True except empty string
print(bool(a)+3)
a = 5
print("123"+str(a))
print(a+int("123")) """


""" a = 10
n = float(a)
print(n)
print(type(n)) """


""" a = 10 
b = 20 
c = (a if a<b else b)+20
print(c) """


""" age1 = 24 
age2 = 16
eligibility1 = "eligible" if age1 >= 18 else "not eligible"
eligibility2 = "eligible" if age2 >= 18 else "not eligible"
print(f"Age 1: {age1}, Eligibility: {eligibility1}")
print(f"Age 2: {age2}, Eligibility: {eligibility2}")

 """

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
