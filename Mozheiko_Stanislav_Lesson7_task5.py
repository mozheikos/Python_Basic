import os
import json


def dictionary_sort(dictionary):
    sorting = sorted(dictionary.keys())
    sort_dict = {}
    for key in sorting:
        dictionary[key][1] = list(dictionary[key][1])
        sort_dict[key] = tuple(dictionary[key])
    return sort_dict


def dictionary_build(path):
    dictionary = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            name = file[file.find('.'):]
            size = os.stat(os.path.join(root, file)).st_size
            n = 1
            if size < n:
                if not dictionary.get(n):
                    dictionary.setdefault(n, [1, set()])
                    dictionary[n][1].add(name)
                else:
                    dictionary[n][0] = dictionary[n][0] + 1
                dictionary[n][1].add(name)
            else:
                while size > n:
                    n = n * 10
                    if size <= n:
                        if not dictionary.get(n):
                            dictionary.setdefault(n, [1, set()])
                            dictionary[n][1].add(name)
                        else:
                            dictionary[n][0] = dictionary[n][0] + 1
                        dictionary[n][1].add(name)
    return dictionary_sort(dictionary)


root_dir = input('input path \n')
file_name = os.path.join(root_dir, '_summary.json')
with open(file_name, 'w') as f:
    data = json.dumps(dictionary_build(root_dir))
    f.write(data)
print(dictionary_build(root_dir))
