'''user_name="Jithu"

0   1  2   3   4  (positive indexing)
J   I  T   H   U
-5 -4 -3  -2  -1  (negative indexing)

print(user_name[1])#indexing
print(user_name[-4])'''
#print(user_name[5])

#string slicing
'''data="Python is a Programming Language"
print(len(data))
print(data[1:8])
print(data[1:8:2])
print(data[-32:])
print(data[:-6])
print(data[6:])
print(data[::3])'''
'''
#string concatenation

string1="Hello"
string2=" World"
print(string1+string2)

#string repetition
print(string1*3)

#membership
print("He" in string1)'''

'''character=input("Enter the Word:")
reverse=character[::-1]
if character==reverse:
    print("Palindrome")
else:
    print("Not Palindrome")'''

#string methods

'''name="jithu is a Very Good Person. He is Good at Improving Himself"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.startswith("ji"))
print(name.endswith("lf"))
# name[3]="t"
print(id(name))
uppercase=name.upper()
print(id(uppercase))'''

#list
'''user_data=["Jithu",23,"Idukki"]
print(user_data)
user_data.insert(3,"MBITS")
print(user_data)
user_data.append("CSE")
print(user_data)
user_data.extend("Python")
print(user_data)
user_data.append(["English","Malayalam"])
print(user_data)
user_data.extend(["HTML","C","Bootstrap"])
print(user_data)
print(user_data[11])
print(user_data[11][0])
user_data.remove("HTML")
print(user_data)
user_data.pop(2)
print(user_data)
user_data.reverse()
print(user_data)'''

#tuple

'''tuple1=(1,3,5,7,9)
print(tuple1)
#nested_tuple=('J','I','T','H','U',(1,2,3,))
#print(nested_tuple)
# tuple1[1]=12
# print(tuple1) Immutable, we can add anything to the tuple but ordered,indexing and slicing possible
#tuple unpacking
person=("Jithu",23,"Idukki")
print(person)
name,age,place=person
print(age)'''

'''numbers=(10,20,30,40,50)
a,b,*c=numbers
print(a,b,c)
d,*e,f=numbers
print(d,e,f)'''

'''number_repeated=(2,4,5,6,2,7,2,4,1,9)
print(len(number_repeated))
print(number_repeated.count(2))
print(number_repeated.index(4))
print(number_repeated[3])'''

#programs
'''user_input=input("Enter a String:")
count=0
for char in user_input:
    count+=1
print(f"Total Number of Characters in the String is {count}")'''

#first non repeating character in a string
'''user_input=input("Enter the Word:")
count=0
for char in user_input:
    if user_input.count(char)==1:
        print(f"First Non Repeating Character is {char} at index position",user_input.index(char))
        break
else:
        print("There are no Non Repeating Character")'''

'''h   e    l    l    o
   0   1    2    3    4'''
'''user_input=input("Enter the Word:")
for i in range(len(user_input)):
    repeated = False
    for j in range(len(user_input)):
        if i!=j and user_input[i]==user_input[j]:
            repeated=True
            break
    if not repeated:
        print("First Non Repeating Character is :",  user_input[i])
        break
else:
    print("There are no Non Repeating Character")'''

#set is an unordered collection of mutable data structure that does not allows duplicate values
'''student1={"English","Malayalam","Hindi"}
student2={"Hindi","English","Python"}
student3={"Python","Urdu"}
print(student1)
print(student2)
print(student3)
student1.add("c++")'''
#student1.add("kannada","tamil") cant add 2 arguments insted use update
'''student1.update(["Kannada","Tamil","Malayalam"]) #didnt allow duplicates
print(student1)
student1.pop()
print(student1)
student1.remove("Kannada")'''
# student1.remove("Java") it will produce error becuase that element is not present
'''student1.discard("Java") #it will not produce error
print(student1)
print(student1.union(student2))
print(student1.intersection(student2))
print(student1.difference(student2))
print(student1.isdisjoint(student3)) '''#return true or false
#check out subset and superset

#frozen set

'''fs1=frozenset("Jithu")
print(fs1)

numbers=frozenset([1,2,2,3,4])
print(numbers)'''

#Dictionary is mutable ds that stores elements as key-value pair
'''student={"Name": "Jithu", "Age":23, "City":"Kumily"}
print(student)
print(student["Name"])

info=dict(city="Kumily",state="Kerala")
print(info)
print(info.keys())
print(info.values())

print(student.get("marks"))
student["marks"]=50
print(student)
student.pop("Age")
print(student)
del student["City"]
print(student)'''

'''employee={"emp1":{"Name": "Jithu","Age":23},
          "emp2":{"Name" : "Ram","Age": 22},
          "emp3":{"Name" : "Arjun","Age": 24},
          "emp4":{"Name" : "Rahul","Age": 23}}#creating nested dictionary
print(employee["emp2"])
print(employee["emp2"] ["Name"])'''
