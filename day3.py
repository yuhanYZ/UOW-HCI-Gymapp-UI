#determine repeate
nums=[1,3,1,5,2,1]
seen={}
for i in nums:
    if i in seen:
        print('repeate number')
    seen[i]= 1