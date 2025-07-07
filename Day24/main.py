# # one way with close
# file=open("my_file.txt")
# contents=file.read()
# print(contents)
# file.close()

#2nd way without close
with open("/Users/inderkukreja/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

# #Write in file
#
# with open("my_file.txt",mode="a") as file:
#     file.write("\nNew text")
#
# with open("my_file1.txt",mode="a") as file:
#     file.write("New text")