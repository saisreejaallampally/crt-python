arr=[2,5,6,2,5,6,1]
newarr=[]
for num in arr:
    if num not in newarr:
        count=0
        newarr.append(num)
        for n in arr:
            if n==num:
                count+=1
        print(count)
    

         