
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
    
def dump_path(name: str):
    path_test = paths.to_folder_test()
    os.chdir(path_test + '/' + name)
    file_list = glob.glob('*.d*')
    fullpath = path_test + '/' + name + '/' + file_list[0]
    return fullpath

dictio = {}

def check_dependancy(path_original:str = 'trial0', path_compare:str = 'trial1'):
    dump_original, dump_compare =  dump_path(path_original),  dump_path(path_compare)

    with h5py.File(dump_original, 'r') as f:
        counter = 0
        dictio = f
        for key, value in f.items():
            arr = np.array(f[key])
