# s="hi im sai sreeja"
# words=s.split()
# maxcount=0
# maxword=""
# for word in words:
#     count=0
#     for ch in word:
#         if ch!=0:
#             count+=1
#     if count>maxcount:
#         maxcount=count
#         maxword=word
# print(maxword)


# s=input()
# words=s.split()
# longest=""
# for word in words:
#     if len(word)>len(longest):
#         longest=word
# print(longest)


# s=input()
# words=s.split()
# count=[]
# for word in words:
#     count.append(len(word))
# m=max(count)
# for word in words:
#     if len(word)==m:
#         print(word)
#         break


# s=input()
# words=s.split()
# print(max(words,key=len))


# s="banana"
# ns=""
# for ch in s:
#     if ch not in ns:
#         ns+=ch
#         count=0
#         for char in s:
#             if char==ch:
#                 count+=1
#         print(ch,":",count)


# s="I do codinG"
# words=s.split()
# for word in words:
#     print(word[::-1],end=" ")


# s="programming"
# ns=""
# for ch in s:
#     if ch not in ns:
#         ns+=ch
# print(ns)


# s=input()
# lcount=0
# ucount=0
# for ch in s:
#     if ch.isupper():
#         ucount+=1
#     else:
#         lcount+=1
# if ucount>lcount:
#     print(s.upper())  
# else:
#     print(s.lower())


# s=input()
# ns=""
# if len(s)>10:
#     ns+=s[0]+str(len(s)-2)+s[-1]
#     print(ns)
# else:
#     print(s)


# n=int(input())
# for i in range(n):
#    s=input()
#    ns=""
#    if len(s)>10:
#        ns+=s[0]+str(len(s)-2)+s[-1]
#        print(ns)
#    else:
#        print(s)


# s1=input().lower()
# s2=input().lower()
# if s1>s2:
#     print(1)
# elif s1<s2:
#     print(-1)
# else:
#     print(0)


# n=int(input())
# bin=""
# while(n!=0):
#     rem=n%2
#     bin=str(rem)+bin
#     n=n//2
# print(bin)


# n=int(input())
# hex=""
# while(n!=0):
#     rem=n%16
#     if n<10:
#         dec=str(rem)+hex
#     else:
#         hex=chr(rem+55)+hex
#     n=n//16
# print(hex)


n = int(input())
x = 0
for i in range(n):
    s = input()
    if '+' in s:
        x += 1
    else:
        x -= 1
print(x)