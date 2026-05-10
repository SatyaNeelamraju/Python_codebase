# open(filepath) method is used to open a file before read and write. A file that is opened has to be closed to avoid file locking issues
# or memory lekages

# with open(filepath) as f: 
#This avoid to close the opened file it takes care of closing the file automatically

# The filepath keep changing across os. To handle those scenarios and keep the script os agnostic 

# use Path function to derive path 
from pathlib import Path
path=Path.home()/"temp.txt"
with path.open() as file:  #opens the file
    pass

print("mode:",file.mode)
print("readability_check:",file.readable())
print("writability_check:",file.writable())

#Always define the encoding 
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()


#mentioning new line char

with path.open(mode="w",encoding="utf-8",newline="\r\n") as file:  
    pass

#modes:
# r,w,r+=read and write ,w+=write and read,a,a+=append and read,x

#file.seek() allows you to move to the start of the file

#file.tell tells you total number of chars in the file

#file.readline()

#file.readlines() - returns list

#file.writelines()

# print("written", file=filename)# used to write contents to file using print 

# file.write("satya \n")

#file.writelines(["Satya\n","Sai\n","Srinivas"])

#csv.reader(file)

#csv.DictReader(file)

#csv.writer(file)
#csv.writerow()

#csv.writeRows()
#csv.DictWriter(file,columns)