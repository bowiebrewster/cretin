# this cute little tool for manaing all the paths
import os 

def to_personal_data():
    #add the path to your test folder here, the "test" folder contains the premade generator files and will contain 
    # the output of the simulation (ie log files and plots)
    path_test = '/home/brewster/Desktop/bowie/'

    if os.path.exists(path_test): 
        path = path_test 

    else:
        raise Exception("add your path to the 'to_personal_data' in paths.py")

    return path

def to_folder_cretin():
    #add the path to this folder 
    path_test = '/home/brewster/Desktop/cretin/cretin/'

    if os.path.exists(path_test): 
        path = path_test 

    else:
        raise Exception("add your path to the 'to_folder_cretin' in paths.py")

    return path


def to_previous_experiments():
    #add the path to your test folder here, the "test" folder contains the premade generator files and will contain 
    # the output of the simulation (ie log files and plots)
    path_test = '/home/brewster/Desktop/test/'

    if os.path.exists(path_test): 
        path = path_test 

    else:
        raise Exception("add your path to the 'to_previous_experiments' in paths.py")

    return path

def to_cretin_ex():

    #there is where the backend cretin is located that will do our simulations  
    path_cretin_ex = f"{os.environ['HOME']}/Desktop/cretin.v2_19_test/bin"

    if os.path.exists(path_cretin_ex): 
        path = path_cretin_ex 

    else:
        raise Exception("add your path to the 'to_cretin_ex' in paths.py")

    return path