
# n = 19
# visited = []

# while n != 1 and n not in visited:
#     visited.append(n)

#     s = 0
#     while n != 0:
#         rem = n % 10
#         s += rem ** 2
#         n = n // 10

#     n = s

# if n == 1:
#     print("Happy")
# else:
#     print("Unhappy")

# n=int(input())
# while n!=1 and n!=4:
#     sum=0
#     while n!=0:
#        rem=n%10
#        sum+=rem**2
#        n=n//10
#     n=sum
# if n==1:
#     print("happy")
# else:
#     print("no")


# n=10
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


# n=10
# c=0
# for i in range(2,n+1):
#     count=0
#     for j in range(2,i):
#         if i%j==0:
#             count+=1
#     if count==0:
#         c+=1
#         print(i)
# print(c)

# for i in range(4):
#     print("*",end="")

# for i in range(4):
#     for j in range(4):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n=5
# for i in range(1,n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(n-i):
#         print("*",end=" ")
#     print()


# for i in range(5,0,-1):
#     print(" "*(5-i),"*"*(i))       

# n=5
# for i in range(1,n):
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(i):
#         print("*",end=" ")
#     print()


# n=6
# for i in range(1,n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(i):
#         print("*",end=" ")
#     for l in range(1,i):
#         print("*",end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(1,5):
#     for j in range(i,10):
#         print(j,end="")
#     print()
    

# n=1
# for i in range(1,5):
#     for j in range(i):
#         print(n,end="")
#         n+=1
#     print()

# for i in range(1,5):
#     for j in range(i):
#         print(i,end="")
#     print()


# for i in range(1,6):
#     for j in range(i):
#         print(chr(j+97),end="")
#     print()


# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# for i in range(1,5):
#     ch=65
#     for j in range(i):
#         print(chr(ch),end="")
#         ch+=1
#     print()


# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ")
#     print()


# n=5
# for i in range(1,n):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(1,i+1):
#         print(k,end=" ")
#     for l in range(i-1,0,-1):
#         print(j,end=" ")
#     print()

# for i in range(1,5):
#     ch=65
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(1,i+1):
#         print(chr(ch),end=" ")
#         ch+=1
#     ch-=2
#     for l in range(1,i):
#         print(chr(ch),end=" ")
#         ch-=1
#     print()

# for i in range(0,5):
#     for j in range(5-i):
#         print(" ",end=" ")
#     for j in range(0,i+1):
#         print(chr(j+65),end=" ")
#     for l in range(i-1,-1,-1):
#         print(chr(l+65),end=" ")
#     print()

# n=5
# for i in range(n):
#     for j in range(n):
#         if j==0 or j==n-1 or i==n//2:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# n=6
# if n&1==1:
#     print("odd")
# else:
#     print("even")

# n=7
# if n&n-1==0:
#     print("true")
# else:
#     print("no")


