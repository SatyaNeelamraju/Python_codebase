from pathlib import Path
path=Path.home()/"dir"
images=path/"images"
text=path/"text"
images.mkdir(exist_ok=True)
text.mkdir(exist_ok=True)
texts=path.glob("*.txt")
imgs=path.glob("*.JPG")
for i in texts:
    j=i.name
    src=path.joinpath(j)
    dest=text.joinpath(j)
    src.replace(dest)

for i in imgs:
    j=i.name
    src=path.joinpath(j)
    dest=text.joinpath(j)
    src.replace(dest)    