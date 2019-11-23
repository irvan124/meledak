import random
import string

num= int(input("Masukkan jumlah serial Number yang ingin di buat : "))
def randomString(stringLength):
   

    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))
   
for j in range(num):
  print (randomString(4),"-",randomString(4),"-",randomString(4),"-",randomString(4) )

