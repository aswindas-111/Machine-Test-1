read_file = "read.txt"
write_file = "write.txt"

file = open(read_file,"r")
content = file.read()
file.close()

with open(write_file,"a") as file:
    file.write(content)