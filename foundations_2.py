from pathlib import Path
path=Path.home().joinpath("notes")

#checking if dir exists
print("check if path exists or not:",path.exists())

#creating directory exist_ok will not throw error if directory exists already
print("creating directory:",path.mkdir(exist_ok=True))
#checking dir after creating
print("check if path exists or not:",path.exists())

#creating subdirectories "notes" and "weekly" by enabling parents flag in mkdir
path1=Path.home().joinpath("notes").joinpath("weekly")
print("creating all parent dirs if not there:",path1.mkdir(parents=True,exist_ok=True))

#creating file 
path2=Path.home()/"notes"/"weekly"/"january.txt"
path3=Path.home()/"notes"/"weekly"/"february.txt"
path4=Path.home()/"notes"/"weekly"/"march.txt"
path2.touch()
path3.touch()
path4.touch()
diriter=Path(r"C:\Users\satya\notes\weekly")
#iterating directory 
print(list(diriter.iterdir()))

#using glob for pattern search 
txtfiles1=diriter.glob("*.txt")
txtfiles2=diriter.glob("*ar?.*")
txtfiles3=diriter.glob("*[h].txt")
print(list(txtfiles1),list(txtfiles2),list(txtfiles3))
print("------------------")
#example of recursive glob
path=Path.home()/"notes"
findall=path.rglob("*.txt")
otherop=path.glob("**\*.txt")
print(list(findall))
print("*************")
final=[i.name for i in list(sorted(otherop))]
print(final)


