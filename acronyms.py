name=input().split()
string=""
for i in range(len(name)):
    string+=name[i][0]+"."
print(string[:-1])

"""
input:Indian Administrative Service
output:I.A.S

"""
