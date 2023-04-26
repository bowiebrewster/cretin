# this cute little tool for manaing all the paths
import os 

def to_folder_test():
    #add the path to your test folder here
    paths_test = ['/home/brewster/Desktop/bowie/']

    for path_test in paths_test:
        if os.path.exists(path_test): 
            path = path_test 
            break

    else:
        raise Exception("add your path to the test folder to the paths_test list in paths.py")

    return path

def to_folder_cretin():
    # add your path to the main cretin package (where paths.py should be located in) here 
    paths_main = ['/home/brewster/Desktop/cretin/cretin/']

    for path_main in paths_main:
        if os.path.exists(path_main): 
            path = path_main 
            break
    else:
        raise Exception("add your path to the cretin folder to the paths_main list in paths.py")

    return path
    