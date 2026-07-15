# n=int(input())
# if(n%4==0 and n%100!=0) or (n%400==0):
#     print("leap year")
# else:
#     print("no")

# for i in range(5):
#     print("hello")

# for i in range(1,11):
#     if(i%2!=0):
#         print(i)
# for i in range(1,11):
#     if(i%2==0):
#         print(i)

# for i in range(1,11):
#     print("5 *",i,"=",5*i)  

# n=5
# i=1
# while(i<=n):
#     print(i)
#     i+=1

# n=5
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)

# n=5
# sum=0
# i=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)

# n=5
# fact=1
# for i in range(1,6):
#     fact*=i
# print(fact)

# n=5
# fact=1
# i=1
# while(i<=n):
#     fact*=i
#     i+=1
# print(fact)

# n=5
# fact=1
# for i in range(5,0,-1):
#     fact*=i
# print(fact)

# n=5
# fact=1
# i=n
# while(i>0):
#     fact*=i
#     i-=1
# print(fact)

# a=int(input())
# b=int(input())
# years=0
# while(a<=b):
#     a*=3
#     b*=2
#     years+=1
# print(years)

# n=20
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# if count==2:
#     print("prime")
# else:
#     print("no")

# n=100
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# n=100
# for i in range(2,n):
#     count=0
#     for j in range(1,i+1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(i)

# n=int(input())
# for i in range(1,n+1):
#     if(i%3==0 and i%5==0):
#         print("FizzBuzz")
#     elif(i%3==0):
#         print("Fizz")
#     elif(i%5==0):
#         print("Buzz")
#     else:
#         print(i)

# n=10
# a=n**0.5
# if a==int(a):
#     print("true")
# else:
#     print("false")

# n=1234
# rev=0
# while(n!=0):
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# print(rev)  


# n=1234
# num=n
# rev=0
# while(n>0):
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
# if(rev==num):
#     print("palindrome")
# else:
#     print("no")


# n=153
# original=n
# arm=0
# while(n>0):
#     rem=n%10
#     arm=arm+rem*rem*rem
#     n=n//10
# if(arm==original):
#     print("Armstrong num")
# else:
#     print("no")


# x=int(input())
# if(x>5) and (x%5==0):
#     print(x//5)
# elif(x>5):
#     print(x//5+1)
# else:
#     print("1")

# x=int(input())
# count=0
# while(x>0):
#     rem=x%10
#     count+=1
#     x=x//10
# print(count)

# x=int(input())
# if(x<10):
#     print(x)
# sum=0
# sumsum=0
# while(x!=0):
#     rem=x%10
#     sum+=rem
#     x=x//10
# if sum<10:
#     print(sum)
# else:
#     while(sum!=0):
#         rem=sum%10
#         sumsum+=rem
#         sum=sum//10
# print(sumsum)

# n=int(input())
# a=0
# b=1
# for i in range(n):
#     print(a)
#     c=a+b
#     a=b
#     b=c

n=int(input())
if n<10:
    print(n)
else:
    sum=0
    while(n!=0):
        rem=n%10
        sum+=rem
        n=n//10
    n=sum
print(n)



