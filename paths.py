# this cute little tool for manaing all the paths
import os 

def to_personal_data():
    #add the path to your test folder here
    path_test = '/home/brewster/Desktop/bowie/'

    if os.path.exists(path_test): 
        path = path_test 

    else:
        raise Exception("add your path to the 'to_personal_data' in paths.py")

    return path

def to_folder_cretin():
    #add the path to your test folder here
    path_test = '/home/brewster/Desktop/cretin/cretin/'

    if os.path.exists(path_test): 
        path = path_test 

    else:
        raise Exception("add your path to the 'to_folder_cretin' in paths.py")

    return path


def to_previous_experiments():
    #there is a folder labeled test where people have added their cretins runs, i use this to see what syntax is used most often
    path_test = '/home/brewster/Desktop/test/'

    if os.path.exists(path_test): 
        path = path_test 

    else:
        raise Exception("add your path to the 'to_previous_experiments' in paths.py")

    return path