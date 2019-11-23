def drawLine(text,length):
    for row in range (length):
        for col in range (length):
            if row==col :
                print(text[col])
            else:
                print(end=" ")
        print(" ")
                
text=input("Masukkan Text : ")
length=len(text)
drawLine(text,length)