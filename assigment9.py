"""a = int(input("Enter num1:"))
b = int(input("Enter num2:"))

a = a + b
b = a - b
a = a - b

print(a)
print(b)"""

"""
sentence =input("Enter sentance :")
count = 0
in_word = False

for ch in sentence:
    if ch != " " and not in_word:
        count += 1
        in_word = True
    elif ch == " ":
        in_word = False
print(count)"""

"""n =int(input("Enter no of digits :"))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b"""

"""nums =list(map(int,input().split()))
repeated = []
for i in range(len(nums)):
    if nums[i] in nums[:i]:
        if nums[i] not in repeated:
            repeated.append(nums[i])
print(repeated)"""


"""
s = input()

for i in range(len(s)):
    found = False

    for j in range(len(s)):
        if i != j and s[i] == s[j]:
            found = True
            break

    if not found:
        print(s[i])
        break
"""