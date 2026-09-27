"""
1.Artimatic Operators:
2'''.Assigment Operators:
3Logical Operators:
4.Comparison Operators:
5.Bitwise Operators:
6.Membership Operators:
7.Identity Operators:


price_per_book=500
qty=25
total_price=price_per_book*qty
extra_charge=5 
final_price=total_price+extra_charge
discount=25
final_price=final_price-discount
remainder=final_price%qty 
floor_division=final_price//qty
square=price_per_book**2
print(f'Total price of books is: {total_price} , Average price of books is: {total_price/qty} , Final price of books is: {final_price} , Remainder is: {remainder} , Floor division is: {floor_division} , Square of price per book is: {square}a')


"""
#Asiigment Operators
'''
Score=100
Score+=50
print(Score)
Score-=20
print(Score)
'''
#Logical Operators
'''
user_name="admin"
password="admin123" 

entered_username=input("Enter username :")
entered_password=input("Enter Password :")

if entered_username==user_name and entered_password==password:
    print("Login Succesfull")
else:
    print("Invalid Login")
'''

'''
day=input("Enter a Day :")
if day=="Saturday" or day=="Sunday":
    print("Holiday")
else:
    print("Working day")


is_logged_In=False 
if not is_logged_In:
    print("Please Login In")
else:
    print("Welcome to Desktop")
''' 

'''
movies_list=["Avatar","Odyssiss","God of War"]
movie=input("Enter your favourite movie:")
if movie in movies_list:
    print("Movie Available")
else:
    print("Movie is not available")
'''

'''
employee_list=["Ravi","Shankar","Adam"]
employee=input("Enter employee name :")
if employee not in employee_list:
    print("Access Denied")
else:
    print("Access Granted")
'''

#Identity Operator:
'''
value1=5
value2=8
print(value1 == value2)
''' 

'''
number_list1=[1,2,3,4]
number_list2=[1,2,3,4]
print(number_list1 is number_list2)
print(number_list1 == number_list2)
'''
'''
list1=[10,20,30,40]
list2=[10,25,30,45]
list3=list2
print(list2 is list3)
print(list1[1] is list2[1])


age=int(input("enter your age :"))
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


student_name=input("Enter student name :")
student_mark=int(input("Enter student marks :"))
print("Pass : ",student_mark>=40)
print("Distiction : ",student_mark>=80)
print("full marks : ",student_mark==100)
print("Need improvement :", student_mark<40)
print("Not Zero :",student_mark!=0)
print("Below A grade :",student_mark<=85)
'''

#biwise operator
num1=5 #0101
num2=3 #0011

# print(bin(num1 & num2)) #same values are 1 (0001)
# print(num1|num2)
# print(~num1)
# print(5<<2)
# print(5>>2)
# print(num1*(2**num2))#left shift
# print(num1/(2**num2))#right shift