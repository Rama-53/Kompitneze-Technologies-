#Square pattern
'''n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()  '''  

#left  alligned triangle
'''n=5 
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    print()
'''
#Inverted
'''n=5 
for i in range(n+1,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()         '''
#Hollow square pattern
'''n=5
for i in range(n):
    for j in range(n):
       if i==0 or i==n-1 or j==0 or j==n-1:
           print("*",end=" ")
       else:
           print(" ",end=" ")
    print() '''      

#Right aligned triangle
'''n=5
for i in range(n):#row 1-5
    for j in range(n):
        if j<= n-i:
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()
'''
#Pyramid
'''n=5
for i in range(n):
   print(" "*(n-i-1)+ "*"*(2*i+1))'''

#Inverted pyramid
'''n=5
for i in range(n,0,-1):
   print(" "*(n-i)+ "*"*(2*i-1))'''

#Number pattern
'''n=5
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()

n=5
for i in range(n):
    for j in range(n):
        print(i,end=" ")
    print()'''

'''n=5
for i in range(n):
    for j in range(n):
        print(chr(65+j),end=" ")
    print()'''   


