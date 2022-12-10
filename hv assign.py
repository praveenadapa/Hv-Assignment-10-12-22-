p=int(input("input 1:"))
r=int(input("input 2:"))
a=int(input("input 3:"))
v=int(input("input 4:"))
e=int(input("input 5:"))
data1=open("data.txt","w")
if(p>0 and r>0 and a>0 and v>0 and e>0):
    print(p+r+a+v+e)
    total=p+r+a+v+e
    data1.write("total: %d"%total)
else:
    print("should provide positive number")
    data1.write("should provide positive number")
data1.close()