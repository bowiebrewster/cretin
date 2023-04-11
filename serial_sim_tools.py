
import os, h5py, glob, shutil
from importlib import reload
import numpy as np
import generator_object, to_generator_string, search, paths, write_run_plot
import matplotlib.pyplot as plt

for obj in [generator_object, to_generator_string, search, paths, write_run_plot]:
    reload(obj)
naming_dict = write_run_plot.naming_dict

# takes as an arugment a (jagged) array consisting of k vectors of size k_i
# returns all possible combinations of the entries in those vectors. 
# for example input array = [[a1,a2,a3],[b1,b2]] returns [[a1,b1],[a1,b2],[a2,b1],[a2,b2],[a3,b1],[a3,b2]]
def combinatorics(arr):
    if len(arr) == 0:
        return [[]]
    else:
        result = []
        for item in arr[0]:
            for combination in combinatorics(arr[1:]):
                result.append([item] + combination)
        return result
    
# path to the dump file
def dump_path(name: str):
    path_test = paths.to_folder_test()
    os.chdir(path_test + '/' + name)
    file_list = glob.glob('*.d*')
    fullpath = path_test + '/' + name + '/' + file_list[0]
    return fullpath

# extracting the data from the dumpfile
def savedict(path):
    dictio = {}
    with h5py.File(path, 'r') as f:
        for key, value in f.items():
            arr = np.array(f[key])
            dictio[key] = arr
            
    return dictio

# checking diffrence between dicionaries
def check_dependancy(path_original:str, path_compare:str):
    global dict_original, dict_compare
    dict_original, dict_compare = savedict(dump_path(path_original)), savedict(dump_path(path_compare))
    
    comparison_dic = {}
    for orignal_key, orignal_value in dict_original.items():
        compare_value = dict_compare[orignal_key]
        
        try:
            comparison_dic[orignal_key] = np.allclose(orignal_value, compare_value)
        except:
            if not(orignal_key == 'model_1' or orignal_key == 'previous'):
                comparison_dic[orignal_key] = 'comparison error'
        
    return comparison_dic

def compare_runs(org_trial: str, curr_trial: str, compare_dict : dict):

        identical_set = set([key.split('_')[0] for key, value in compare_dict.items() if value == True])
        changed_set = set([key.split('_')[0] for key, value in compare_dict.items() if value == False])
        error_set = set([key.split('_')[0] for key, value in compare_dict.items() if value == 'comparison error'])

        identical_lis = [naming_dict[setpiece] for setpiece in identical_set if setpiece in naming_dict]
        changed_lis = [naming_dict[setpiece] for setpiece in changed_set if setpiece in naming_dict]
        error_lis = [naming_dict[setpiece] for setpiece in error_set if setpiece in naming_dict]
        print(f'comparison of {org_trial} and {curr_trial}, identical arrays: {identical_lis}\n changed arrays: {changed_lis}\n comparision error arrays: {error_lis}')

def plot(name : str, plot_duplicates : bool):
    # finding d file
    path_test = paths.to_folder_test()
    os.chdir(path_test + '/' + name)
    file_list = glob.glob('*.d*')
    fullpath = path_test + '/' + name + '/' + file_list[0]

    with h5py.File(fullpath, 'r') as f:
        # managing directories
        path = path_test + name + '/images'
        if os.path.exists(path):
            shutil.rmtree(path) 
        os.mkdir(path)
            

        counter = 0

        for key, value in f.items():
            arr = np.array(f[key])

            # these never need to be plot
            if key in ['model_1','previous','ai','zi','model_id']:
                pass
            elif key.split('_')[0] in ['r', 'u', 'regmap', 'iso']:
                pass

            elif len(arr.shape) == 2:
                plot3d(name, path, key, plot_duplicates, arr)

            elif len(arr.shape) == 1 and len(arr) > 0:
                plot2d(name, path, key, plot_duplicates, arr)

            elif len(arr.shape) > 2:
                print(f'{key} has dimension {len(arr.shape)} and has not been')

            counter += 1

def plot3d(name: str, path:str, masterkey:str,  plot_duplicates : bool, arr):
    collapse = are_all_vectors_identical(arr)
    if collapse == 'rows':
        vector = arr[0]
        plot2d(name, path, masterkey, plot_duplicates, vector)
    elif collapse == 'columns':
        vector = arr[:, 0]
        plot2d(name, path, masterkey, plot_duplicates, vector)

    else:        
        save_bool = True
        for key, array in arrays3d.items():
            if np.shape(array) == np.shape(arr):
                if np.allclose(arr, array):
                    save_bool = False
                    

        if save_bool or plot_duplicates:
            arrays3d[masterkey] = arr

def plot2d(name : str, path:str, masterkey:str,  plot_duplicates : bool, arr):
    save_bool = True 
    for key, array in arrays2d.items():
        if np.shape(array) == np.shape(arr):
            if np.allclose(arr, array):
                save_bool = False
               

    if save_bool or plot_duplicates:
        arrays2d[masterkey] = arr

# Check if all vectors in a numpy array are identical.
def are_all_vectors_identical(arr):

    # Check that the array has at least one row
    if arr.shape[0] < 1:
        return False
    
    # Get the first row as a reference vector
    ref_vector = arr[0]
    ref_column = arr[:, 0]
    # Check if all other vectors are equal to the reference vector
    if np.all(np.equal(arr, ref_vector), axis=1).all():
        return 'rows'
    
    elif np.all(np.equal(arr, ref_column.reshape(-1, 1)), axis=0).all():
        return 'columns'
    
    else:
        return True

all_trials_dict = {}

def plot_all(foldername:str, trials : list):
    for trial in trials:
        global arrays2d, arrays3d
        arrays2d, arrays3d = {}, {}
        plot(trial, plot_duplicates = False)
        all_trials_dict[trial] = [arrays2d, arrays3d]

    # we love list comprehesion
    keys2d = all_trials_dict[trials[0]][0].keys()
    keys3d = all_trials_dict[trials[0]][1].keys()
    keys2d = [list(all_trials_dict[trial][0].keys()) for trial in trials]
    keys3d = [list(all_trials_dict[trial][1].keys()) for trial in trials]
    set_2d = set([item for sublist in keys2d for item in sublist])
    set_3d = set([item for sublist in keys3d for item in sublist])

    path = f'{paths.to_folder_test()}{foldername}'
    print(f'multiplot too {path}')
    if os.path.exists(path):
        shutil.rmtree(path) 
    os.mkdir(path)

    if len(keys2d) >0:
        for key in set_2d:
            all(path, key, trials)

    if len(keys3d) >0:
        for key in set_3d:
            all(path, key, trials)

axis_dict = {
    'ne' : 'nodes',
    'ni' : 'nodes',
    'r' : 'nodes',
    'te' : 'nodes',
    'u' : 'nodes',
    'eav': 'ebins',
    'emis': 'ebins',
    'ev': 'ebins',
    'jnu': 'ebins',
    'kappa': 'ebins',
}

def all(path: str, key: str, trials:list):
    legend = []
    for trial in trials:
        trial_dict = all_trials_dict[trial][0]
        if key in trial_dict.keys():
            arr = trial_dict[key]
            plt.plot(arr)
            legend.append(trial)
    plt.legend(legend)

    realkey = key.split('_')[0]

    if realkey in axis_dict.keys():
        plt.xlabel(axis_dict[realkey])
    
    try:
        start = xaxis_delimitter(arr)[0]
        end = xaxis_delimitter(arr)[1]
        plt.xlim(start - 1, end + 1)
        pass
    except:
        pass

    index = '_'.join(key.split('_')[1:])
    if realkey in naming_dict.keys():
        realkey = naming_dict[realkey]+index


    plt.title(realkey)
    plt.savefig(f'{path}/{realkey}.png')
    plt.clf()
    plt.close()

def xaxis_delimitter(lst):
    ranges = []
    start_idx = None
    for i in range(len(lst)):
        if lst[i] != 0 and start_idx is None:
            # Start of a new range
            start_idx = i
        elif lst[i] == 0 and start_idx is not None:
            # End of the current range
            ranges.append((start_idx, i-1))
            start_idx = None
    if start_idx is not None:
        # End of the list is also end of the last range
        ranges.append((start_idx, len(lst)-1))

    start = ranges[0][0]
    end = ranges[-1][-1]

    return start, end
