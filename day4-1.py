import os.path
if os.path.isfile('filename.txt'):
    print('file存在')
else:
    print('file不存在')
    
fo = open("filename.txt",'w')
fo = fo.write('hey')
fo = open("filename.txt",'r')
fo = fo.read
fo = open("filename.txt",'a')
fo = fo.write('hi')
