from pathlib import Path
result={}

path_string = "/home/user/notes.txt"
path=Path(path_string)

result["parent"]=str(path.parent)
result["name"]=path.name
result["stem"]=path.stem
result["suffix"]=path.suffix
print(result["parent"],result["name"],result["stem"],result["suffix"])
#--------------------------------------------------------------------------------------

file_path=Path(r"C:\Users\satya\my_folder\my_file.txt")
print(file_path)
print("Checking if file_path exists",file_path.exists())
print(file_path.name)
print(file_path.parent.name)