pembayaran = int(input(' Total Harga Belanja : '))


if pembayaran>=20000: disc = 40/100*pembayaran
elif pembayaran>=50000: disc = 30/100*pembayaran
elif pembayaran<20000: disc = 0

total = pembayaran - disc



print("Potongan Harga : Rp. ",disc)
print("Harga yg harus di bayar : Rp. ",total)
uangbayar = int(input(' Uang yang di bayar : Rp.'))
kembalian = uangbayar - total
print("Kembalian : Rp. ",kembalian)
