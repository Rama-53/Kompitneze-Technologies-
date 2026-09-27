#inbuit Function

"""print(len("Spiderman"))
print(sum([1,2]))
print(max([1,5,7,9]))
print(min([1,5,8,2]))
print(sorted([5,7,8,2,4]))
print(sorted([1,3,7,2,5,9],reverse=True))
languages=["Malayalam","hindi","Japanese","english"]#M=77,"e"=101
print(sorted(languages))
print(sorted(languages,reverse=True,key=len))"""

##TRy "Enumeration function"

"""
    LEGB Rule
    L=local
    E=enclosing
    G=global
    B=Builtin
"""

def student_details():
    name="Ram"#local variable 
    print(name)
#student_details()
#print(name)  Trying to acesss functional variable hence will fail 

"""collage_name="MBITS" #global variable 
def display():
    print("Collage name is ",collage_name)
#display()

#enclosing example 
def department():#outer function
    department_name="computer science"
    def student():#inner function 
        print("Department name is ",department_name)
    student()
department()"""

#Billing System
#tax - global variable,discount=enclosing ,amount=local

tax=150
def shopping():
    discount=50
    def bill():
        amount=5000
        total_amount=amount-discount+tax 
        print(total_amount)
    bill()
shopping(  
)