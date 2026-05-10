from pathlib import Path
path=Path.home()/"practice_files"/"documents"/"files"/"sample.txt"
print(path)
path.touch()

with path.open(encoding="utf-8",mode="w")as f:
    f.write("Hi ra ! How are you ? \n")
    f.write("Helloooooooooo\n")
    f.write("Reyyyyyyyyy\n")
    f.write("Namaste\n")
    f.writelines(["Satya\n","Sai\n","Srinivas"])

with path.open(encoding="utf-8",mode="r") as f:
    content=f.readlines() # All lines content in one list
    print(content)
#-----------------------------------------------------------------------------------------------------------    
#------------------------------------------------------ csv files -------------------------------------------
# reading from csv file
import csv
path=Path.home()/"practice_files"/"sample.csv"
with path.open(encoding="utf-8",mode="r") as f:
    reader=csv.reader(f)  # dictreader will output dictionary with a column name added as key and column value as value 
    for line in reader:
        print(line)
#-----------------------------------------------------------------------------------------------------------      
# writing and reading to csv files
header = ['Name', 'Age', 'Job']
data = [
    ['Alice', 30, 'Engineer'],
    ['Bob', 25, 'Designer']
]  
newpath=Path.home()/"practice_files"/"demo.csv"
newpath.touch()
with newpath.open(encoding="utf-8",mode="w",newline='') as file:
    writer=csv.writer(file) #object creation 
    writer.writerow(header)
    writer.writerows(data)

with newpath.open(encoding="utf-8",mode="r") as file:
    reader=csv.reader(file)
    for i in reader:
        print(i)

#------------------------------------------------------------------------------------------------------------
#  writing using dict writer
header = ['user_id', 'username', 'email']
data = [
    {'user_id': 1, 'username': 'coder99', 'email': 'dev@example.com'},
    {'user_id': 2, 'username': 'pixel_art', 'email': 'art@example.com'}
] 
path=Path.home()/"practice_files"/"demo1.csv"
path.touch()

with path.open(encoding="utf-8",newline='',mode='w') as file:
    writer=csv.DictWriter(file,header)
    writer.writeheader()
    writer.writerows(data)

with path.open(encoding="utf-8",mode='r') as file:
    reader=csv.reader(file)
    for lines in reader:
        print(lines)

#using dictreader to read the file
with path.open(encoding="utf-8",mode='r') as file:
    reader=csv.DictReader(file)
    for lines in reader:
        print(lines)        