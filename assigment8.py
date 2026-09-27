"""
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n):
    if n % i == 0:
        sum = sum + i

if sum == n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
"""

"""
s = input("Enter a string: ")

frequency = {}

for ch in s:
    if ch in frequency:
        frequency[ch] = frequency[ch] + 1
    else:
        frequency[ch] = 1

for ch in frequency:
    print(ch, ":", frequency[ch])
"""


"""
numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for num in numbers:
    if num not in result:
        result.append(num)

for num in result:
    print(num, end=" ")
"""

"""
n = int(input("Enter a number: "))

largest = -1
second_largest = -1

while n > 0:
    digit = n % 10
    n = n // 10

    if digit > largest:
        second_largest = largest
        largest = digit
    elif digit > second_largest and digit != largest:
        second_largest = digit

if second_largest == -1:
    print("No Second Largest Digit")
else:
    print("Second Largest Digit:", second_largest)
"""