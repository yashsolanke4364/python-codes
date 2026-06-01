A=[19,25,30,45,23,35,44]
positive_num=[]
negative_num=[]
for i in A:
    if (i>0) :
     positive_num.append(i)
    else:
         negative_num.append(i)

print("postive_num:",positive_num)
print("negative_num:",negative_num)
sum=0
total = 0

for num in A:
    total += num

mean = total / len(A)

print(f"The mean of the elements in the list is:",mean)





