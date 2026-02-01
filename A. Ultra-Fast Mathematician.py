c = input().strip()
d = input().strip()
 
res =""
 
for i in range(len(c)):
    if c[i] !=d[i]:
        res +="1"
    else:
        res +="0"
print(res)
