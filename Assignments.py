############################# assignment -1 #######################

from pathlib import Path
import shutil
path=Path.home()/"my_folder"

file1=path.joinpath("file1.txt")
file2=path.joinpath("file2.txt")
image1=path.joinpath("image1.jpg")

path.mkdir(exist_ok=True)
file1.touch()
file2.touch()
image1.touch()

img=path/"images"
img.mkdir(exist_ok=True)

src=path/image1.name
dest=img/image1.name

if src.exists():
    src.replace(dest)

file1.unlink()
shutil.rmtree(path)

############################# assignment -2 #######################    

IMAGE_EXTENSIONS = (".png", ".gif", ".jpg")
source_dir=Path.home()
dir=source_dir/"practice_files"
imgs=dir/"images"
imgs.mkdir(exist_ok=True)
lists=[]
for i in IMAGE_EXTENSIONS:
    j=f"*{i}"
    lists=dir.rglob(j)   
    for k in lists:
        l=k.name
        dest=imgs.joinpath(l)
        k.replace(dest)
    



