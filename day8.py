# lst=[4,1,5,3,9]
# min=lst[0]
# for num in lst:
#     if num<min:
#         min=num
# print(min)


# lst=[4,1,5,3,9]
# min1=lst[0]
# min2=lst[0]
# for num in lst:
#     if num<min1:
#         min2=min1
#         min1=num
#     elif num<min2 and num!=min1:
#         min2=num
# print(min2)


# lst=[4,1,5,3,9]
# max1=lst[0]
# max2=lst[0]
# for num in lst:
#     if num>max1:
#         max2=max1
#         max1=num
#     elif num>max2 and num!=max1:
#         max2=num
# print(max2)


# n=int(input())
# m=0
# for i in range(n):
#     lst=list(map(int,input().split()))
#     count=0
#     for num in lst:
#         if num==1:
#             count+=1
#     if count>1:
#         m+=1
# print(m)


# s=input()
# ns=""
# for ch in s:
#     if ch not in ns:
#         ns+=ch
# if len(ns)%2==0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")


# s=input()
# name=set(s)
# if len(name)%2==0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")


# lst=list(map(int,input().split()))
# for num in lst:
#     count=0
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print(num)


# lst=list(map(int,input().split()))
# for num in lst:
#     sum=0
#     for i in range(1,num):
#         if num%i==0:
#             sum+=i
#     if sum==num:
#         print(num)


# n = int(input())
# count = 0
# while n % 2 == 0:
#     count += 1
#     n = n // 2
# print(count)


# def trailingzero(lst):
#     for n in lst:
#         count=0
#         while n%2==0:
#             count+=1
#             n=n//2
#         print(count)
# lst=list(map(int,input().split()))
# trailingzero(lst)



