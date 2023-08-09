# Reading from file

info_file = open("info.txt", "r")  # r for read, w for write, a for append, r+ for reading and writing

# print(info_file.readable())

if info_file.readable():
    for info in info_file.readlines():
        print(info)
else:
    print("File cannot be read!")

info_file.close()
