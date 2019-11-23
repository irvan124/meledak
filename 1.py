data = [2,3,4,5,6]
data1 = data[0]
data2 = data[1]
data3 = data[2]
data4 = data[3]
data5 = data[4]

p1=data1+data2+data3+data4
p2=data1+data2+data3+data5
p3=data1+data2+data5+data4
p4=data1+data5+data3+data4
p5=data5+data2+data3+data4

besar = max(p1,p2,p3,p4,p5)
kecil = min(p1,p2,p3,p4,p5)
print("Angka terkecil dan terbesar adalah ",kecil,"dan",besar)
