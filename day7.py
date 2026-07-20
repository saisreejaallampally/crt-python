# lst=[2,3,7,9,11,15,17,8,7]
# print(lst[-4:-7:-2])

# l=[2,3,2,3,2,3]
# print(l[-4:-6:-1])

# lst = list(map(int, input().split()))
# sum=0
# for num in lst:
#     sum+=num
# # print(sum)

# lst=list(map(int,input().split()))
# max=lst[0]
# for num in lst:
#     if num>max:
#         max=num
# print(max)

# n=int(input())
# lst=input().split()
# for i in range(n):
#     lst[i]=int(lst[i])
# max=lst[0]
# for num in lst:
#     if num>max:
#         max=num
# print(max)

# lst=list(map(int,input().split()))
# el=[]
# for i in range(len(lst)):
#     count=0
#     for j in range(len(lst)):
#         if lst[i]==lst[j]:
#             count+=1
#     if count==1:
#         el.append(lst[i])
#         print(lst[i])
# print(len(el))


# lst=list(map(int,input().split()))
# for num in lst:
#     if lst.count(num)==1:
#         print(num)


# lst=[2,3,4,2,3]
# result=0
# for num in lst:
#     result^=num
# print(result)


# lst=[1,2,3,4]
# print(set(lst))

# set={1,2,3,4}
# print(tuple(set))

# tuple=(1,2,3,4)
# print(list(tuple))


# lst=[1,2,3,2,1,4]
# nl=[]
# for num in lst:
#     if num not in nl:
#         nl.append(num)
# print(tuple(nl))


lst=[1,2,3,2,1,4]
print(set(lst))


# lst = [1,2,3,4]
# tup = (2,3,4)
# s = {3,4,5,6}
# for num in lst:
#     if num in tup and num in s:
#         print(num)


# tup=(1,2,3,2,4)
# count=0
# for num in tup:
#     if tup.count(num)==1:
#         count+=1
# print(count)


# lst=[1,2,3]
# set={4,5,6}
# tup=(7,8,9)
# nl=[]
# for num in (lst,set,tup):
#     nl.append(num)
# print(nl)


# l=[1,2,3,4,3,2]
# s={1,2,3}
# for num in l:
#     if num not in s:
#         print(num)
