import os
import yaml
from yaml.loader import SafeLoader


def create_folder(path, names):
    for name in names:
        os.chdir(path)
        if isinstance(name, str):
            if name.find('.') != -1:
                create_file(path, name)
            if name not in os.listdir(path):
                os.mkdir(os.path.join(path, name))
            name_ = name
        else:
            create_folder(os.path.join(path, name_), name)


def create_file(path, name):
    if name not in os.listdir(path):
        with open(os.path.join(path, name), 'w', encoding='UTF-8') as file:
            file.write('')


path = os.getcwd()
with open('config.yaml', 'r', encoding='UTF-8') as f:
    folder_names = yaml.load(f, SafeLoader)


if __name__ == '__main__':
    create_folder(path, folder_names)
