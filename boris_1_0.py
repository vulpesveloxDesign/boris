#!/usr/bin/env python3
import shutil
import os
import json

"""for now he only serves as a text bot, but lo' and behold, in time he will grow more powerful!"""

from_folder     = 'D:\\'
to_folder       = 'C:\\Users\\vulpes\\Desktop\\file_machine\\main_folder'
dirt_folder     = 'C:\\Users\\vulpes\\Desktop\\file_machine\\junk_folder'
root_text_file  = 'C:\\Users\\vulpes\\Desktop\\file_machine\\notarius.txt'

if not os.path.exists(to_folder):
    os.mkdir(to_folder)
if not os.path.exists(dirt_folder):
    os.mkdir(dirt_folder)
if not os.path.exists(root_text_file):
    texty_beast = open(root_text_file, 'w')
    texty_beast.close()


def writer(current_file):
    """using json, this one makes short work of file metadata."""
    size_queen = os.stat(foldername + '\\' + current_file).st_size
    current_path = foldername + '\\' + current_file
    this_dict = {'streetname': current_file, 'areacode': current_path, 'fatness': size_queen}
    dumper = json.dumps(this_dict)
    with open(root_text_file, 'a', encoding='utf8') as append_to_note:
        append_to_note.write('{}\n'.format(dumper))


def reader(current_file):
    """this one unpacks the json files one by one and checks whether the file is a usual suspect."""
    with open(root_text_file, 'r', encoding='utf8') as de_filer:
        for f in de_filer.readlines():
            soup_monster = json.loads(f)
            if current_file == soup_monster['streetname'] and int(os.stat(foldername + '\\' + current_file).st_size) == int(soup_monster['fatness']):
                return False
    return True


os.chdir(from_folder)

for foldername, subfolders, filenames in os.walk(from_folder):
    format_types = ['.txt', '.pdf', '.odt', '.rtf', '.doc', '.wpd']
    if 'django' in subfolders:
        subfolders.remove('django')
    for filename in filenames:
        # if filename.endswith(('.txt')):
        if filename.endswith('.txt') or filename.endswith('.pdf') or filename.endswith('.odt') or filename.endswith('.rtf') or filename.endswith('.doc') or filename.endswith('.docx') or filename.endswith('.wpd'):
            if reader(filename) == True:
                print('copied:\t{}'.format(filename))
                shutil.copy((foldername + '\\' + filename), to_folder)
                writer(filename)
            else:
                print('I\'ve caught a crook, master! Look! --> {}'.format(filename))
                shutil.copy((foldername + '\\' + filename), dirt_folder)
