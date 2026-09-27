# student.txt open()
"""
file=open("filename"."mode")

file=open("student.txt","w")#write mode if no such file exit it will automatically create a file
r -- read
w --- write
a -- apppend
x -- create
r+ -- read+write
w+ --- write+read
a+ -- append+read
b -- binary ModuleNotFoundError
t -- text mode
"""
"""file.write("ram")
file.close()
file=open("student.txt","r")
data=file.read()
print (data)
file.close()| I


# data=file.read()
# print(data)
# file.close()
file open("studnet.txt","w+")
file.write("rahul\n")

file.write("hello\n")

file.writelines(["python ","django ","react "])
file.seek(ø)
data=file.read()
print(data)
file.close

with open("employe.txt","w+") as file:
file.writelines(["rahul\n","anju\n"])
file. seek(1)
print(file.readline())

#read() readline() readlines()
#write() writelines()
#append()
#writety writelines

with open("message.txt","r") as file:
    print(file.tell())#0
    data=file.read(5)
    print(data)#5 I
    file.seek(ø)
    print(file.tell())#0

with open("message.txt","r") as file:
    file.tell(3)
    print(file.read())



"""


# name="aparna"
# age=30

# #student.txt open()

# file=open("filename","mode")
# file=open("student.txt","w")#write mode if no such file exit it will automatically create a file
# r--read
# w---write
# a--apppend
# x--create
# r+--read+write
# w+---write+read
# a+--append+read
# b--binary ModuleNotFoundError
# t--text mode
# file.write("aparna")
# file.close()
# file=open("student.txt","r")
# data=file.read()
# print(data)
# file.close()
# file=open("studnet.txt","w+")
# file.write("rahul\n")

# file.write("hello\n")

# file.writelines(["python ","django ","react "])
# file.seek(0)
# data=file.read()
# print(data)
# file.close


# with open("employe.txt","w+") as file:
#     file.writelines(["rahul\n","anju\n"])
#     file.seek(1)
#     print(file.readline())

#read() readline() readlines()
#write() writelines()
#append()

# with open("message.txt","r") as file:
#     print(file.tell())#0
#     data=file.read(7)
#     print(data)#5
    
#     print(file.tell())#0
"""
with open("message.txt","r") as file:
    print(file.tell())
    file.seek(6)
    print(file.read())
    print(file.tell())
"""

# Write binary data
with open("image_copy.jpg", "wb") as file:
    file.write(b"Hello Binary File")
# Read binary data
with open("image_copy.jpg", "rb") as file:
    data = file.read()

print(data)

with open("original.jpg", "rb") as source:
    with open("copy.jpg", "wb") as destination:
        destination.write(source.read())
