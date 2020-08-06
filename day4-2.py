file = open("file.png",'rb')
img = file.read()
file.close()
file = open("複製.png",'wb')
file.write(img)
file.close