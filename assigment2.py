customer_name=input("Enter Customer Name : ")
product_name=input("Enter Product Name : ")
quantity=int(input("Enter Quantity : "))
per_product_price=int(input("Enter Price Per Product : "))
membership=input("Enter Membership Type : ")
wallet_balance=int(input("Enter Wallet Balance : "))



total_cost=per_product_price*quantity
if membership == "Gold":
    discount = total_cost * 10 / 100
elif membership == "Silver":
    discount = total_cost * 5 / 100
else:
    discount = 0

gst = (total_cost - discount) * 18 / 100
final_bill = total_cost - discount + gst
remainder = quantity % 2

delivery_charge = 0
delivery_charge += 50  
bill_after_delivery = final_bill
bill_after_delivery += delivery_charge
bill_after_delivery -= discount  

free_delivery = final_bill > 1000 and membership == "Gold"
special_offer = membership == "Gold" or membership == "Silver"
not_regular = not (membership == "Regular")

wallet_enough = wallet_balance >= final_bill 

products = ["Rice", "Sugar", "Oil", "Milk", "Bread"]
product_available = product_name in products
product_not_available = product_name not in products


space=20
print("-"*space+"Bill Details"+"-"*space)

print(f"Total Cost : ₹{total_cost:.2f}")
print(f"Discount Amount : ₹{discount:.2f}")
print(f"GST Amount : ₹{gst:.2f}")
print(f"Final Bill Amount : ₹{final_bill:.2f}")

print(f"Wallet Balance Sufficient  : {wallet_enough}")
print(f"Free Delivery Eligible : {free_delivery}")
print(f"Product Available : {product_available}")

print("\nIdentity Operator Results:")

x = 100
y = x

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(f"list1 is list2 : {list1 is list2}")
print(f"x is y : {x is y}")

print("\nBitwise Operations:")
print(f"5 & 3  = {5 & 3}")
print(f"5 | 3  = {5 | 3}")
print(f"5 ^ 3  = {5 ^ 3}")
print(f"5 << 1 = {5 << 1}")
print(f"5 >> 1 = {5 >> 1}")