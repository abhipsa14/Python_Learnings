#if = Do some code only if some condition is True
# Else do something else

age= int(input("Enter your age:"))

# if age>= 18:
#     print("You can sign up.")
# if age<18:
#     print("You cannot sign up.")

if age>=100:
    print("You are too old to sign up")
elif age>=18:
    print("You can sign up.")
elif age<0:
    print("You are not born yet!!")
else:
    print("You cannot sign up.")