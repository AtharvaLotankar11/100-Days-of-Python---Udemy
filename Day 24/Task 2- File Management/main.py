#alt to file = open("my_file.txt")
with open("my_file.txt") as file:
    contents = file.read() #Read the opened file
    print(contents)

#with will also close the file so no need of file.close()

with open("new_file.txt", mode="a") as file: #default mode=r
    file.write("\nNew text.")

#modes = w(write new), a(append)