# n=int(input("Input : "))
# sum=0
# temp=n
# while temp>0:
#     digit=temp%10
#     sum+=digit 
#     temp=temp//10
# if n%sum ==0:
#     print("Harshid Number")
# else:
#     print("False")

# 2
# True
# True 

# 3 10 21 36

# list_nums=list(map(int,input("Input :").split()))
# f_large=list_nums[0]
# f_large_index=0
# for i,index in enumerate(list_nums):
#     if i>f_large:
#         f_large=i 
#         f_large_index=index
# s_large=0
# s_large_index=0
# for i,index in enumerate(list_nums):
#     if index!=f_large_index and i>s_large:
#         s_large=i 
#         s_large_index=index
# f_small=999999999
# f_small_index=999999
# for i,index in enumerate(list_nums):
#     if i>f_small:
#         f_small=i
#         f_small_index=index 
# s_small=99999999
# s_small_index=0
# for i,index in enumerate(list_nums):
#     if index!=s_small_index and i<s_small:
#         s_small=i
#         s_small_index=index
# print(f'Second Smallest : {s_small}')
# print(f'Second Largest : {s_large}')


# input_str1,input_str2=input().split()
# if len(input_str1)!=len(input_str2):
#     print("Not Anangram ")
#     exit(0)
# let_dict={}
# for i in input_str1:
#     if i not in let_dict.keys():
#         let_dict[i]=1 
#     else:
#         let_dict[i]+=1
# let_dict1={}
# for i in input_str2:
#     if i not in let_dict1.keys():
#         let_dict1[i]=1
#     else:
#         let_dict[i]+=1 
# anagram=True
# for i in let_dict:
#     if i not in let_dict1:
#         anagram=False
#         break
# if anagram:
#     print("Anagram")
# else:
#     print("Not Anagram")


# arr=list(map(int,input().split()))
# l_large=-9999999
# s_large=-9999998
# f_small=999999
# s_small=999999
# for i in arr:
#     if i>l_large:
#         s_large=l_large
#         l_large=i
#     elif i>s_large and i!=l_large:
#         s_large=i 
#     if i<f_small:
#         s_small=f_small
#         f_small=i 
#     elif i<s_small and i!=f_small:
#         s_small=i
# print(s_small)
# print(s_large)