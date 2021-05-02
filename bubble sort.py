a = [7,5,3,4,8]
print("List before sorted : ",a)
 
for j in range(0,len(a)-1):
    for i in range(len(a)-1,j,-1):
        if a[i-1] > a[i]:
            a[i],a[i-1] = a[i-1],a[i]

print("List after sorted : ",a)
            
