N=int(input("Enter the number :"))

if N<2:
    print("Not a Prime Number")
else:
    prime=True 
    for i in range(2,N):
       if N%i==0:
          prime=False
          break 
    if prime:
        print(f'{N} is a prime number')
    else:
        print(f'{N} is a composite number')