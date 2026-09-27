# function types

# user-defined-fuctions-with args,without args 
# with args-positional,keyworad,default


"""
def function_name (parameters):
        code to be exectucted


def welcome():
    print("Welcome to Python programming")



def Greeting(username,user_age):
    print(f"Welcome {username} , you are {user_age} yaers old")

def addition(num1,num2):
    return num1+num2 




num1=int(input("Enter num 1 :"))
num2=int(input("Enter num 2 :"))
print(addition(num1,num2))

"""


#positional argumnets

# def book_ticket(movie_name,customer_name,seats,ticket_price):
#     total=seats*ticket_price
#     return f"{customer_name} booked {seats} ticket for {movie_name} Rs {total}"

# print(book_ticket("Jumanji","Basil",5,150))
# print(book_ticket("Basil","Jumanji",5,150))


#Keyword arguments   

# def customer_details(custm_name,custm_age,city):



#defaulr arguments 

# def booking_status(custm_name,status="confermed",screen="screen1"):
#     print(f"{custm_name} 's Booking status : {status} \n Screen Alllocated : {screen}")

# booking_status("ravi")
# booking_status("ravi","Rejevcted","nil")
# booking_status(screen="screen2",status="confirmed")


"""Multiple Arguemnts(*args,** kwargs)""" 



def calculate_bill(* ticket_prices):
    print(f"ticket prices :{ticket_prices}")
    print("total bill : ",sum(ticket_prices))

calculate_bill(100,300,400,450,50)

#paasing multipele keywords and arguments 

def passsenger_info(** info):
    for key ,value in info.items():
        print(f"{key} : {value}")

passsenger_info(
    passsenger_name="ravi",
    seats=6,
    paymend_status="paid",
    destination="kera"
)