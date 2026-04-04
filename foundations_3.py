from pathlib import Path
path=Path.home()/"notes"
old_file_path=path/"april.txt"
new_file_path=path/"weekly"/"april.txt"
old_file_path.replace(new_file_path)

dir_iter=path/"weekly"
print(list(dir_iter.iterdir()))