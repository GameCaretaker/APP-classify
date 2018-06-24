f=open("getapp_y.txt")
f1=open("getapp_y1.csv","w")
m=f.readlines()
i=list(set(m))
dic={}
dic1={}
for j in range(0,len(i)):
    dic[i[j]]="%d"%j
    dic1["%d"%j]=i[j]
print(dic)
print(dic1)
for i in m:
    f1.write(("%s\n"%dic[i]))