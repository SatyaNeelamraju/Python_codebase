from pathlib import Path
path=Path.home()/"practice_files"
images=path.glob("image[0-9]*")
new_path=path/"images"
new_path.mkdir(exist_ok=True)
for i in images:
    print("i:",i)
    j=i.name
    src=path.joinpath(j)
    dest=new_path.joinpath(j)
    print(src,dest)
    src.replace(dest)