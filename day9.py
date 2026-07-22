# d={}
# n=int(input())
# for i in range(n):
#     key=input("key:")
#     value=input("value:")
#     d[key]=value
# print(d)



# lst = list(map(int, input().split()))
# d = {}
# for num in lst:
#     if num in d:
#         d[num] += 1
#     else:
#         d[num] = 1
# print(d)


# str=input()
# d={}
# for ch in str:
#     if ch in d:
#         d[ch]+=1
#     else:
#         d[ch]=1
# print(d)



# lst = list(map(int, input().split()))
# d = {}
# for i in lst:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1

# keys = list(d.keys())
# max_key = keys[0]
# min_key = keys[0]

# for key in d:
#     if key > max_key:
#         max_key = key
#     if key < min_key:
#         min_key = key

# print("Maximum key =", max_key)
# print("Frequency =", d[max_key])

# print("Minimum key =", min_key)
# print("Frequency =", d[min_key])



# lst = list(map(int, input().split()))
# d = {}
# for i in lst:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# keys = list(d.keys())
# max_key = keys[0]
# min_key = keys[0]
# for key in d:
#     if d[key] > d[max_key]:
#         max_key = key
#     if d[key] < d[min_key]:
#         min_key = key
# print("Maximum frequency key =", max_key)
# print("Minimum frequency key =", min_key)


# lst = list(map(int, input().split()))
# d = {}
# for i in lst:
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] = 1
# keys = list(d.keys())
# max_key = keys[0]
# min_key = keys[0]
# for key in d:
#     if d[key] > d[max_key]:
#         max_key = key
#     if d[key] < d[min_key]:
#         min_key = key
# print("Maximum frequency key =", max_key)
# print("Minimum frequency key =", min_key)


lst=list(map(int,input().split()))
d={
    "even":0,"odd":0
}
for num in lst:
    if num%2==0:
        d["even"]+=1
    else:
        d["odd"]+=1
print(d)