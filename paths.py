# this cute little tool for manaing all the paths
import os 

def to_folder_test():
    paths = []

    #insert the path to your test folder here
    paths_test = ["/Users/bowie/OneDrive/Desktop/recretincode/cretin.v2_19_test/test/",
        '/home/brewster/Desktop/cretin.v2_19_test/test/',
        'C:/Users/M65E255/Onedrive - NN/desktop/cretin_data/']

    for path_test in paths_test:
        if os.path.exists(path_test): 
            path = path_test 
            break

    else:
        raise Exception("add your path to the test folder to the paths_test list in paths.py")

    return path

def to_folder_cretin():
    paths_main = ['/home/brewster/Desktop/cretin/cretin-1/',
                    'c:/Users/M65E255/Onedrive - NN/desktop/cretin/']

    for path_main in paths_main:
        if os.path.exists(path_main): 
            path = path_main 
            break
    else:
        raise Exception("add your path to the cretin folder to the paths_main list in paths.py")

    return path
    