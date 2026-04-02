#for loops = execute a block of code a fixed number of times.
# you can iterate over a range, string, sequence, etc.

for x in range(1,11):
    print(x,end=" ")

for x in reversed(range(1,11)):
    print(x,end=" ")

for x in range(1,11,2):
    print(x)

credit_card= "12333565312"
for i in credit_card:
    print(i)


#continue, break, pass

for x in range(1,21):
    if x==13:
        break #continue
    else:
        print(x)