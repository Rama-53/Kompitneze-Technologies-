#primt number 
"""num=int(input("Enter a number: "))
if num<=1:
    print("Not a Prime number")
else:
    for i in range(2,num):
        if num%i==0:
            print("Not a prime  number")
            break
    else:
        print("prime number")    

        5
        5<1 False
        else 5%2==0
             5%3==0 False
"""

#Fiibinonnice Series 
#0 1 1 2 3 5 8 13 ........
"""num=int(input("Enter the no of iterations :"))
a=0
b=1
for i in range(num):
    print(a,end=" ")
    c=a+b
    a=b
    b=c"""

""" 
a=0,b=1,c=a+b=0+1=1
a=b,b=c,
"""

#find largest and smallest from a list of elements 
"""num_list=[]
no_iteration=int(input("Enter the no of Elements to Insert into the list:"))
for i in range(no_iteration):
    num=int(input(f"Enter no {i+1}"))
    num_list.append(num)
largest=num_list[0]
smallest=[]

for num in num_list:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num 
print(f"Largest num is {largest}")
print(f"Smallest num is {smallest}")"""

"""num_list=[]
no_iteration=int(input("Enter the no of Elements to Insert into the list:"))
for i in range(no_iteration):
    num=int(input(f"Enter no {i+1}"))
    num_list.append(num)
positive_list=[]
negative_list=[]
for num in num_list:
    if num>0:
        positive_list.append(num)
    else:
        negative_list.append(num)
print(f"Positive list :{positive_list}")
print(f"Negative list :{negative_list}")"""

"""num_tuple=tuple(map(int,input("")))
num_dict={}
for i in num_tuple:
    if i not in num_dict.keys():
        num_dict[i]=1
    else:
        num_dict[i]+=1
print(f"count of charecters {num_dict}")
    """

#Positivve and Negative

"""d={"a":1,"b":2,"c":3}
rev_d=dict((value,key) for key,value in d.items())
print(rev_d)

revered={}
for key in list(d.keys())[::-1]:
    revered[key]=d[key]
print(revered)"""

#linear search 

"""user_marks=list(map(int,input("Enter the elemnetsa to be inserted:").split("")))
serach_element=int(input("Enter the elemnt to be serached :"))
for i in range(len(user_marks)):
    if user_marks[i]==serach_element:
        print(f"Elemnet Found at : {i}")
        break 
else:
    print("Elemnt not Found")"""

#bubble sort-arranging elements in ascending order

# numbers = list(map(int, input("Enter the Elements to be Inserted: ").split()))
# for i in range(len(numbers) - 1):
#     for j in range(len(numbers) - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
# print(numbers)
'''
0  1   2   3   4
13 89  10  75  51
i=0 j=1
13 89 10 75 51
i=0 j=2
10 89 13 75 51
i=0 j=3
10 89 13 75 51
i=0 j=4
10 89 13 75 51

i=1 j=2
10 13 89 75 51
i=1 j=3
10 13 89 75 51
.....

i=2 j=3
10 13 75 89 51
i=2 j=4
10 13 51 75 89
'''

"""def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers
user_input = list(map(int, input("Enter the Elements to be Inserted: ").split()))
print(bubble_sort(user_input))"""


#Git hub
GLOBAL INFORMATION TRACKLER


UNTRACKED
ADDED 
MODIFIED