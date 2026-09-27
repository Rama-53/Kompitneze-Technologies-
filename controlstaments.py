""""
for variable in sequence:
    code to be  executed

using range function:
    for variable in range(start,stop,skip):
        code to be executed

start=default value 0
stop=always number -1 
skip =1 for positive number
        -1 for negative value

while loop syntax :
  
initilization
while condition :
     code to be exectuted
     updation 

for and while are entry controlled loops
"""

# for i in range (3,0,-1):
#     print(i)

# for j in range (1,10):
#     print(j)

# for k in range(5,36,3):
#     print(k)

# for i in range(10,1,-1):
#     print(i)       IT WILL NOT WORK 


# for m in range(10,0,-1):
#     print(m)

# for  m in range(17,3,-3):
#     print(m)



# num=int(input("Enter Number :"))
# for i in range(1,10+1):
#     print(f" {i} * {num} = {num*i}")


# value=1 
# sum=0
# iterations=int(input("Enter number of iterations:"))
# while value<=iterations:
#     sum+=value
#     value+=1 
# print(sum)


""" 
sum=8,value=1
iterator=8
i<=8 true
    sum=sum+vallue(0+1=0)
    value+=1(i+1=2)
2<=8:
    sum=1+2(3)
    value=3
3<=8:
    sum=3+3(6)
    value=
"""


# num =int(input("Enter the number :"))
# rev=0
# reminder=0
# copy=num

# while num >=1:
#     reminder=num%10
#     rev=rev*10+reminder
#     num//=10

# if rev==copy:
#     print("Palindrom")
# else:
#     print("Not Paalindrom")



# number of 9s between 1-100
count = 0

for num in range(1, 101):
    temp = num

    while temp > 0:
        if temp % 10 == 9:
            count += 1
        temp = temp // 10

print("Number of 9s between 1 and 100:", count)

# num=int(input("enter the number :"))
# sum_=0

# while num>=1:
#     sum_+=num%10
#     num//=10
# print(sum_)

# num=int(input("enter the number :"))
# fact=1
# while num>0:
#     fact*=num
#     num-=1
# print(fact);




