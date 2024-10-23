import os
import shutil

source_dir = 'Python_docs'
dest_dir = 'RESULTS'

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
    
files = os.listdir(source_dir)
print(f"Вміст каталогу '{source_dir}'")
for file in files:
    print(file)
    
files_to_copy = files[:2]
for file in files_to_copy:
    full_file_name = os.path.join(source_dir, file)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, dest_dir)
        
print(f"Перші два файли скопійовано у папку '{dest_dir}'.")