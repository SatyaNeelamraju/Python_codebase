from pathlib import Path

#prinitng home path
print(Path.home()) #C:\Users\satya

#Appending directory to the home path method1
path=Path.home()/"temp"
print(path)

#printing cwd
print(Path.cwd()) #E:\Python_Learning\Python_codebase

#method2
path1=Path.home().joinpath("temp")
print(path1)


#checking if file exists or not
filepath=Path.home().joinpath("temp").joinpath("sample.txt.txt")
print(filepath,filepath.exists())

#checking if a given path is file or directory can be used if a file is available or not 
checks1=filepath.is_file()
print(f" checks if this is file or not result: {checks1}")
checks2=filepath.is_dir()
print(f" checks if this is directory or not result: {checks2}")

file_name=Path("sample.txt")

#check if a path is absolute or relative 

print("Checking if filepath is absolute or not:", filepath.is_absolute())
#finding out absolute path for a file works only with path object
# resolve appends current working directory to file
print(file_name,file_name.resolve())

# Accessing all child paths 
for p in filepath.parents:
    print(p)
print(list(filepath.parents),"____",list(filepath.parents)[1])    
print(filepath.parent)

print("anchor:",filepath.anchor)
print("stem:",filepath.stem)
print("suffix:",filepath.suffix)
print("file_name:",filepath.name)