number  = int(input("enter from what "))
number2  =  int(input("enter to what "))
k = 0
for i in range(number,number2):
    if i%2:
        k = k
    else:
        k += 1

print(k)
