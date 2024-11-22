# import os
# file = open("myData.txt", "r")

# print(file.read())

# # Write a new file
# newFile = open("filename.txt", "w")
# newFile.write("We add the content of that file")

# # Removing/deleting files
# os.remove("filename.txt",)










# Error handling and exception

try:
    file = open("mydata.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("This file is not found")
finally:
    print("Incomplete file")





