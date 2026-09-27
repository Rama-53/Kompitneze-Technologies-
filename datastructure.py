"""
user_name="ashok"
# 0 1 2 3 4 (positiuve indexing)
# a s h o k
#-5 -4 -3 -2 -1 
print(user_name[2])
print(user_name[-3])
print(user_name[5])# index out of range

"""
"""
data="Pyhton is a programnming language"
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
#p y t h o n   i s   a     p  r  o  g   r  a m   m  i  n g      l  a  n g  u  a  g  e 
print(data[1:8])
print(data[0:14])
print(data[-10:-3])
print(data[::-6])
print(data[:-6])
print(data[6:])
print(data[::3])

"""
"""
#stringConcationation

string1="hello"
string2="world"
print(string1+string2)

# String repeation
print(string1*5)

#Membership
print("he" in string1)
"""


"""
#string methoides 
car="BMW V8 Engine is a beast"
print(car.upper())
print(car.lower())
print(car.title())

print(car.startswith("BMW"))
print(car.endswith("beast"))

car[3]="l"#string is immutabled

print(id(car))
print(id(car.upper()))
"""
"""
#List 
uset_data=["Ashok",22,"Void"]
print(uset_data)
uset_data.insert(2,"carmel")
uset_data.append("Odin")
print(uset_data)
uset_data,append(["English","Malalyalam"])
uset_data.extend(["HTML","CSS"])
print(uset_data)
print(uset_data[11])
print(uset_data[11][0])

uset_data.remove("HTML")
uset_data.pop()
print(user_data)

uset_data.reverse()
print(uset_data)


#Tuple
tuple=(2,3,5,7,8)

#nested tuple
nested_tuple=("David","Sanjay","Sayoo",(22,23,45,55))
print(nested_tuple)

#tuple[1]=12  #immutable,ordered

#indexing and slicing 
#tuplr unpakcing
person=("ashok",22,"allapuzha")
print(person)
name,age,place=person
print(age)

# number=(2,3,5,7,8)
# a,b,c* =number
# print(c)

# d,*e,f=number 
# print(d)
# print(e)
# print(f)


# number_repeated=(2,2,4,5,6,8,3,4,52,2,2,)
# print(len(number_repeated))
# print(number_repeated.count(2))"""
