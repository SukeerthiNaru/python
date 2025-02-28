#write a program to calc factorial of a num using loop
n=int(input("enter a number"))
fact=1
for i in range(1,n+1):
     fact=fact*i
print("factorial of", n,"is",fact)


#Print all numbers from 1 to 100 that are divisible by 3 and 5 using a  for  loop.#
#n1=int(input("enter a number"))
for n1 in range(1,101):
    if n1 % 3 == 0 and n1 %5 == 0:
        print(n1)

#print tables
n2=int(input("enter a number"))
for i in range(1,11):
 print(f"{n2} x {i} = {n2*i}")

