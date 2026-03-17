#Typecasting - the process of converting a variable from one data type to another
#  str(),int(),float(),bool()
# It is of two types: 1.Implicit 2. Explicit

name= "Abhipsa"
age= 21
gpa= 9.2
is_student= True

#name=int(name)
#age=str(age)
age=float(age)
print(age)
#gpa=int(gpa)
gpa=str(gpa)
print(type(gpa))

if is_student:
    print(f"{name} is a student with age {age}")
else:
    print("Not a student")

