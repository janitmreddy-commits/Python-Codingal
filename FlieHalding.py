new_file = open('New_File.txt','x')
new_file.close()


import os
print("Checking if my_file exists or not....")
if os.path.exists("Codingal.txt"):
    os.remove("Codingal.txt")
else:
    print("The file does not exist")



my_file = open("Codingal.txt","w")
my_file.write("Hi! I am Penguin and I am 1 yr old. ")
my_file.close()

os.remove('Codingal.txt')