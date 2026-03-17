#Variable =A container for a value(string, integer, float, boolean)
# A variable behaves as it it was the value it contains.

#Strings
first_name="Abhipsa"
food="burger"
email="abhi@g.com"
print(first_name)
print(f"Hello {first_name}")
print(f"I Love eating {food}")
print("My email is",email)

#Integers
age= 25
quantity= 3
num_of_students= 30
print(f"You are {age} years old.")
print(f"Ypu are buying {quantity} items")
print("Your class has",num_of_students)

#Float
price=10.99
gpa=9.4
distance= 5.5

print(f"The price of the item is {price}")
print(f"My gpa is {gpa}")
print(f"Distance covered it {distance}")

# Boolean----> True or False
is_student= True
if is_student:
    print("You are a student")
else:
    print("You are not student")


is_online=False
if is_online:
    print("You are online.")
else:
    print("You are offline")