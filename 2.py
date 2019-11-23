def hitungKembalian(a,b,c,d):
    for x in range (0, 6):
        i=0
        while c >= d[x]:
            c = c - d[x]
            i = i+1
            if (i>0):
                print ("%d x %d " %(i,d[x]))
            else:
                print ("")
    print ("")
                
a = int(input("Masukkan nilai total belanja: Rp."))
b = int(input("Masukkan uang yang dibayar: Rp. "))
c=b-a
print ("Kembalian sebesar Rp.",c,"dengan Rincian kembalian ")
d = [50000, 20000, 10000, 5000, 2000, 1000, 500]
hitungKembalian(a,b,c,d)