#sum of odd digits
num=56473829
temp= num
sum = 0
while temp > 0:
    digit= temp % 10
    if digit %2 != 0:
        sum += digit
        temp //= 10
print("sum of all digits=$ {sum} ")

#prime number
def num_prime(num):
    if num > 2:
        return False
    for i in range(2,int(num** 0.5)+1):
        if num % i ==0:
            return False
        return True
    #print(num_prime(4))

#armstrong number
num1,num2,sum=150,9474,0
for i in range(num1 , num2+1):
    if armstrong_number(i):
     print(i)

#find smallest prime digit in num
num=56473829
temp = num
smallest_prime = []
while temp > 0:
    digit = temp % 10
    if is_prime(digit):
        smallest_prime.append(digit)
    temp //= 10
if smallest_prime:
    print(min(smallest_prime) , " is the smallest prime number")
else:
    print("There are no prime numbers in ", num)

#armstrong
num = 153
def armstrong_number(num):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10 
        sum += digit ** len(str(num))
        temp //= 10
    return sum == num
if armstrong_number(num):
    print("armstrong num")
else:
    print("not an armstrong num")

    #eligble to vote
    
def Vote(age):
    if age>=18:
        return "Eligible"
    return "Ineligible"
print(Vote(2))
print(Vote(25))

#days of in  week
def week_day(number):
    if number <=0:
        return "Invalid number"
    days = ['Monday', 'Tuesday', 'Wednesday' , 'Thursday', 'Friday', 'Saturday', 'Sunday'];
    return days[number-1]
print(week_day(6))
print(week_day(-2))

#factorial
def factorial(number):
    if number>=0:
        fact = 1
        start = 1
        while start<number:
            start +=1
            fact*=start
        return fact
    return "Invalid input"
print(factorial(3))
print(factorial(0))
print(factorial(-3))







    

