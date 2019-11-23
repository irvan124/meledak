
tgl = int(input("Masukkan Tanggal : "))

if tgl > 1:
    for i in range(2,tgl):
        if (tgl % i) == 0:
            print(tgl, "bukan bilangan prima")
            print(i, "kali", tgl//i, "=", tgl)
            break
    else:
        print(tgl,"adalah bilangan prima")

