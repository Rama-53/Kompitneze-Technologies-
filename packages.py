"""import sys 
print(sys.builtin_module_names)"""

import math
"""help(math)#shows ducumentaion
print(dir(math))#shoes everything avavilable in module 
function=inspect.getmembers(math,inspect.isfunction)
print(function)"""

# print(math.sqrt(4))
# print(math.factorial(5))

"""from math import sqrt as squareroot
print(squareroot(10))
print(math.pow(50,2))"""

#random module
"""import random
print(random.randint(1,10))# random value between 1-10
print(random.random())# prandom value between 0 and 1

students=["Alena","Deepu","Ram","Jithu"]
print(random.choice(students))
print(random.shuffle(students))
print(students)"""


"""import os 
#intercacting with OS 
print(os.getcwd())
os.mkdir("test")
print(os.path.exists("package.py"))
print(os.listdir())
#os.rmdir
#os.remove()
print(os.rmdir("test"))#deletes an emplty directory
print(os.remove("filemname.extention"))
"""

import sys
# print(sys.version)
# print(sys.argv)
#print(sys.path)#used for debugging 
#print("program started")
# sys.exit()
# print("program ended")

import pandas as pd

data = {
    "Name": ["Aparna", "Anu", "Meera"],
    "Mark": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)