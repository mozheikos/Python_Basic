import os
from shutil import copytree


def copying(path_1, path_2, root_name):
    folders = list(filter(lambda x: x.find('.') == -1, os.listdir(path_1)))
    for folder in folders:
        path = os.path.join(path_1, folder)
        if folder == root_name:
            for name in os.listdir(path):
                copytree(os.path.join(path, name), os.path.join(path_2, name))
        else:
            copying(path, path_2, root_name)


base_path = r'c:\my_project\my_project'
final_path = r'c:\my_project\my_project\templates'
final_folder = 'templates'
copying(base_path, final_path, final_folder)
