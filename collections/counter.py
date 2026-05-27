from collections import Counter

a="aaaaabbbbsssss"

my_counter=Counter(a)

print(my_counter)
print(my_counter.most_common(2)[0][0])
print(list(my_counter.elements()))