'''
Input và output với file trong Python 
Tham khảo: https://www.tutorialspoint.com/python/python_files_io.htm về các mode để mở file

'''

file = "file.txt"
try:
   f = open(file, 'r')
   print(f.read())
finally:
   f.close()
   print("The file is closed")

print("---")

with open(file, 'r') as f:
   print("File opened")
   f.close()
print("File closed")

print("---")

with open(file, 'r') as f:
   print(f.readline())

print("---")

with open(file, 'r') as f:
   print(f.readlines())

print("---")


with open(file, 'w') as f:
   print(f.write("Learn Python"))

print("---")


lines = ["Learn Python\n", "Learn Computer\n", "Learn using PythonGeeks\n"]
with open(file, 'w') as f:
   print(f.writelines(lines))

print("---")


with open(file, 'a') as f:
   print(f.write("New Content"))

print("---")

with open(file, 'r') as f:
   f.read(4)
   print(f.tell())

'''
import os
file = "file.txt"
os.remove(file)
print(f"{file} is deleted")

os.mkdir("newdir")

os.chdir("newdir")

os.getcwd()

os.rmdir('dirname')
'''