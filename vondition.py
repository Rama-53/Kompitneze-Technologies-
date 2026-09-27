"""
if condition:
    code to be executed
elif condition:
    code to be exectued
else:
    code to be executed
"""

# num=int(input("Enter a number: "))
# if num>=0:
#     print("Positive number")
# else:
#     print("Negative number")


# char =input("Enter a charecter :")
# if char.lower() in ["a","e","i","o","u"]:
#     print("Vowel")
# else:
#     print("Consonent")

# num=int(input("Enter a number :"))
# if  num%2==0:
#     print(f"{num} is Even ")
# else:
#     print(f'{num} is Odd')

# age=int(input("Enetr Age :"))
# if age<13 :
#     print("Child")
# elif age<18:
#     print("Teenager")
# elif age<60:
#     print("Adult")
# else:
#     print("Senior")

# num=int(input("Enter a number :"))
# if num>0:
#     if num%2==0:
#         print(f"{num} is Positive and Even ")
#     else:
#         print(f"{num} is Positive and Odd")
# else:
#     print("Number is Negative :")

# num=int(input("Enter a number :"))
# if num<1000 and num>=100:
#     print("3 digit number")
# elif num<100:
#     print("2 or 1 digit number")
# else:
#     print("4 or higher digit number")


balance=int(input("Enter Balance Amount :"))
withdraw_amount=int(input("Enter withdrawal amount :"))
if balance>=withdraw_amount:
    print("withrawal Possible ")
else:
    print("withdrawal not Possible")