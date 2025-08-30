print("---------------------------GUEST LIST--------------------------")


n=int(input("Enter the list of guest you want to invite for dinner:"))
guest_lst=[]

for i in range(0,n):
    guest_name=input("Enter the guest name:")
    guest_lst.append(guest_name)

guest_not=[]

print("-----------------INVITATION FOR GUEST-------------------------")

ch=input("Enter your choice(Y/N) to you want to attend the dinner:")
while(True):
    if(ch.lower()=='y'):
        guest_conf_name=input("Enter your name:")
        guest_not.append(guest_conf_name)
        guest_lst.remove(guest_conf_name)
        break
    elif(ch.lower()=='n'):
        print("Thank you for replying!")
        break
    else:
        print("Invalid choice.")


print("List of Confirmed list of guest are:")
print(guest_lst)

print("List of Guest who are not coming:")
print(guest_not)
    