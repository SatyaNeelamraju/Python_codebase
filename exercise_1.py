text="""\
Discovery
Enterprise
Defiant
Voyager
"""
from pathlib import Path
path = Path.home()/"exercises"/"starships.txt"
path.touch()
with path.open(encoding="utf-8",mode="w",newline='')as file:

    # file.writelines(["Discovery\n","Enterprise\n","Defiant\n","Voyager"])
    file.write(text)
    
with path.open(encoding="utf-8",mode="r")as file:
    content=file.readlines()
    for line in content:
        print(line,end='')