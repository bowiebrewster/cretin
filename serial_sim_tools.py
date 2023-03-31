
import os, h5py, glob
from importlib import reload
import numpy as np
import generator_object, to_generator_string, search, paths

for obj in [generator_object, to_generator_string, search, paths]:
    reload(obj)


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
    
