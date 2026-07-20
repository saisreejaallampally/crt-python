# def mult(a,b):
#     print(a*b)
# mult(2,4)

# def mult(a,b):
#     return a*b
# x=mult(2,4)
# print(x)

# def add(a,b):
#     print(a+b)
# add(2,3)

# def add(a,b):
#     return a+b
# x=add(3,4)
# print(x)

# def mult(a,b):
#     print(a*b)
# a=int(input())
# b=int(input())
# mult(a,b) 

# def word():
#     print("hello")
# word()

# def mult(a,b):
#     return a*b
# x=int(input())
# y=int(input())
# print(mult(x,y))

# def sqnum(a):
#     return a**2
# n=int(input())
# print(sqnum(n))

# def sqnum(a):
#     print(a**2)
# n=int(input())
# sqnum(n)

# def greatest(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# x=int(input())
# y=int(input())
# print(greatest(x,y))

# def greatest(a,b):
#     if a>b:
#         print(a)
#     else:
#         print(b)
# x=int(input())
# y=int(input())
# greatest(x,y)

# def evenodd(a):
#     if a%2==0:
#         return "even"
#     else:
#         return "odd"
# n=int(input())
# print(evenodd(n))

# def square(s):
#     return s*s
# def rect(l,w):
#     return l*w
# def triangle(b,h):
#     return 0.5*b*h
# s=int(input())
# l=int(input())
# w=int(input())
# b=int(input())
# h=int(input())
# res1=square(s)
# res2=rect(l,w)
# res3=triangle(b,h)
# print("area of square",":",res1)
# print("area of rectangle",":",res2)
# print("area of triangle",":",res3)

# def primenumber(n):
#     for i in range(2,n):
#         if n%i==0:
#             return "not prime"
#         else:
#             return "prime"
# n=int(input())
# print(primenumber(n))


# def primenumber(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return "prime"
#     else:
#         return "not prime"
# n=int(input())
# print(primenumber(n))
        
        
# def armstrong(n):
#     num=n
#     arm=0
#     while(n!=0):
#         rem=n%10
#         arm+=rem**3
#         n=n//10
#     if arm==num:
#         return "arm"
#     else:
#         return "no"
# n=int(input())
# print(armstrong(n))


# def primerange(n):
#     for i in range(2,n+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
# n=int(input())
# primerange(n)


# def primerange(n):
#     for i in range(2,n+1):
#         count=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             print(i)
# n=int(input())
# primerange(n)               


# def perfectnum(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
#     if sum==n:
#         return "perfect"
#     else:
#         return "not"
# n=int(input())
# print(perfectnum(n)) 


# def reverse(n):
#     rev=0
#     while(n!=0):
#        rem=n%10
#        rev=rev*10+rem
#        n=n//10
#     return rev
# n=int(input())
# print(reverse(n))


# def countofnum(n):
#     count=0
#     while(n!=0):
#         rem=n%10
#         count+=1
#         n=n//10
#     return count
# n=int(input())
# print(countofnum(n))


# def palindrome(n):
#     num=n
#     rev=0
#     while(n!=0):
#         rem=n%10
#         rev=rev*10+rem
#         n=n//10
#     if rev==num:
#         return "palindrome"
#     else:
#         return "not"
# n=int(input())
# print(palindrome(n))


# def strong(n):
#     num=n
#     sum=0
#     while(n!=0):
#         rem=n%10
#         fact=1
#         for i in range(1,rem+1):
#             fact*=i
#         sum+=fact
#         n=n//10
#     if sum==num:
#         return "strong"
#     else:
#         return "not"
# n=int(input())
# print(strong(n))


# def reverse(n):
#     print(str(n)[::-1])
# reverse(1234)


