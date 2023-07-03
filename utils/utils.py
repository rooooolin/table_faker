import os
import shutil

def find_files(dir_path, file_ext):
    #if any(dir_path.endswith(ext) for ext in file_ext):
    if os.path.isfile(dir_path):
        return [dir_path]
    file_list = []
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            if any(filename.endswith(ext) for ext in file_ext):
                if not os.path.basename(filename).startswith('~$'):
                    file_list.append(os.path.join(root, filename))
    return file_list

def create_folder(folder_path):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)
    os.mkdir(folder_path+'/tmp/')