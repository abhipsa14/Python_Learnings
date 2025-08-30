# def display_name(username):
#     print(f"Hello, Welcome {username.title()}")

# def fav_book(book):
#     print(f"Your favourite: {book.title()}")

# def describe_pet(animal_type, pet_name):
#     print(f"\nI have a {animal_type.lower()}.")
#     print(f"My {animal_type.lower()}'s name is {pet_name.title()}.")

# username = input("Enter your good name: ")
# book = input("Enter your favourite book: ")
# animal_type = input("Enter the pet type you have: ")
# pet_name = input("Enter the name of the pet: ")

# display_name(username)
# fav_book(book)
# describe_pet(animal_type, pet_name)  # Positional
# # Or: describe_pet(pet_name=pet_name, animal_type=animal_type)  # Keyword

def get_formatted_name(first_name,last_name):
    full_name=f"{first_name}+{last_name}"
    return full_name
   


while(True):
    print("Please enter your name:")
    print("If you want to quit, press q")
     
    first_name=input("Enter your first name:")
    if(first_name=='q' or first_name=='Q'):
        break
    else:
         last_name=input("Enter your last name:")
    print(f"\nHello",get_formatted_name(first_name,last_name))