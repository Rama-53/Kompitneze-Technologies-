"""n=int(input("Enter number:"))
fact=1
for i in range(2,n+1):
    fact*=i
print(fact)
"""

"""def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)#3*factoral(3-1)-->2*factoral(2-1)--->return 1
num=int(input("Enter number :"))
print(f"Factorail of {num} is {factorial(num)}")
"""

#Lambda fuction:

def add(num1,num2):
    return num1+num2
#print(add(3,6))

#syntax
# lamda arguments:expression 
"""
add=lambda a,b:a+b
#print(add(5,4))

swaure=lambda a:a*a 
print(swaure(5))"""

# largest=lambda a,b : a if a>b else b 