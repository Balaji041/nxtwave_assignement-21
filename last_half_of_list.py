N=int(input())
l=input().split()
le=(len(l)+1)//2
lie=l[le:]
list_i=[]
for i in lie:
    list_i+=[int(i)]
print(list_i)

"""
input:6
1 2 3 4 5 6
output:[4, 5, 6]

"""
