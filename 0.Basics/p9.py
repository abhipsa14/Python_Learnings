# format specifiers ={value:flags} format a value based on what flags are inserted
# .(number)f=round to that many decimal places(fixed point)
# :(number) = allocate that many spaces
# :03= allocate and zero pad that many spaces
# :< = left justify
#  :> = right justify
#  :^ =center align
#  :+ = use a plus sign to indicate posittive Value
#  := = place sign to leftmost position
#  :  = insert a sapce before positive numbers
#  :, = comma separator

p1= 3.14159
p2= -28938789.393893
p3= 12.34


print(f"Price 1 is {p1:.3f}")
print(f"Price 2 is {p2:,}")
print(f"Price 3 is {p3:>}")