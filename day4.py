# print(26<<7)

# n=30
# binary=""
# while(n>0):
#     rem=n%2
#     binary+=str(rem)
#     n=n//2
# count=0
# binary=int(binary)
# while(binary>0):
#     rem=binary%10
#     if rem==1:
#         count+=1
#     binary=binary//10
# print(count)


# n=30
# count = 0
# while n > 0:
#     if (n & 1) == 1:
#         count += 1
#     n = n >> 1
# print(count)
# print(30>>1)

# n=int(input())
# k=int(input())
# if(n&1<<k!=0):
#     print("Set bit")
# else:
#     print("no")

# n=int(input())
# binary=""
# while(n!=0):
#     rem=n&1
#     binary=str(rem)+binary
#     n=n>>1
# print(binary)


# binary=int(input())
# decimal=0
# power=0
# while(binary!=0):
#     rem=binary%10
#     decimal=decimal+rem*(2**power)
#     power+=1
#     binary=binary//10
# print(decimal)


# n=20
# a=20//8
# b=20%8
# print(str(a)+str(b))

# print(hex(108))
# print(hex)

# print(oct(96))

# n=int(input())
# a=n//8
# b=n%8
# print(str(a)+str(b))

# print(21<<3)

# print(hex(21))

# print(oct(120))


# binary = int(input())
# decimal = 0
# power = 0

# while binary > 0:
#     rem = binary % 10
#     decimal += rem * (2 ** power)
#     power += 1
#     binary = binary // 10

# octal = ""

# while decimal > 0:
#     rem = decimal % 8
#     octal = str(rem) + octal
#     decimal = decimal // 8
# print(octal)


# s=input().lower()
# print(s[::-1])
# if s[::-1]==s:
#     print("palindrome")
# else:
#     print("no")

# s=input().lower()
# ns=""
# for i in range(len(s)-1,-1,-1):
#     ns+=s[i]
# if(ns==s):
#     print("palindrome")
# else:
#     print("no")

# s=input().lower()
# vcount=0
# ccount=0
# for ch in s:
#     if ch in "aeiou":
#         vcount+=1
#     else:
#         ccount+=1
# print(vcount)
# print(ccount)

# s=input()
# lcount=0
# ucount=0
# for ch in s:
#     if ch.isupper():
#         ucount+=1
#     else:
#         lcount+=1
# print(ucount)
# print(lcount)


# s="Hello World"
# ns=""
# for ch in s:
#     if ch!=" ":
#         ns+=ch
# print(ns)

# s=input()
# letters=0
# digits=0
# symbols=0
# for ch in s:
#     if ch.isalpha():
#         letters+=1
#     elif ch.isdigit():
#         digits+=1
#     else:
#         symbols+=1
# print(letters)
# print(digits)
# print(symbols)


# s=input()
# digits=0
# symbols=0
# for ch in s:
#     if ch.isdigit():
#         digits+=1
#     elif not ch.isalpha() and not ch.isspace():
#         symbols+=1
# print(digits)
# print(symbols)


# s="programming"
# es=""
# for ch in s:
#     if ch not in es:
#         es+=ch
#     else:
#         print(ch)

# s="programming"
# es=""
# for ch in s:
#     if ch not in es:
#         es+=ch
#         count=0
#         for char in s:
#            if ch==char:
#               count+=1
#         if count==1:
#             print(ch)
#             break


# s="programming"
# es=""
# for ch in s:
#     if ch not in es:
#         es+=ch
#     else:
#         print(ch)
#         break
        
    
# s="programming"
# for ch in s:
#     if s.count(ch)==1:
#        print(ch)
#        break


# s1="listen"
# s2="silent"
# es=""
# if len(s1)!=len(s2):
#     print("no")
# else:
#     for ch in s1:
#         if s1.count(ch)!=s2.count(ch):
#             print("no")
#             break
#     else:
#         print("anagaram")




