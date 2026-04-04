
from pathlib import Path
import shutil
path=Path.home()/"my_folder"
img=path/"images"
img.mkdir(parents=True,exist_ok=True)
old_path=path/"image1.JPG"
new_path=img/"image1.JPG"

# old_path.replace(new_path)
check=path/"file_1.txt"
check.unlink(missing_ok=True)
shutil.rmtree(path)
shutil.copytree(#source,#dest)
