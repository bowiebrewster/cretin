from importlib import reload
import numpy as np
import matplotlib.pyplot as plt
import h5py, os, glob, shutil
import generator_object, to_generator_string, search, paths #these python classes should be in the same folder as cretin_main
for obj in [generator_object, to_generator_string, search, paths]:
    reload(obj)


# takes the text string and writes it to the cretin generator file
def write(name : str, object):
    string = to_generator_string.Text_generator(object).execute()

    if not os.path.exists(paths.to_folder_test() + name):
        os.makedirs(paths.to_folder_test() + name)

    file_loc = paths.to_folder_test() + name + '/' + name + '.gen'
    print(f'\nwriting to {file_loc}')
    with open(file_loc, 'w') as f:
        for x in string:
            f.write(str(x))

#  running cretin using the written generator file
def run(name : str, longprint : bool):
    print(f'running cretin with {name}')
    import subprocess

    env = os.environ.copy()
    path = f'{paths.to_folder_test()}{name}'

    env["ARG_NAME0"] = name
    env["ARG_NAME1"] = f'{paths.to_folder_test()}{name}'

    process = subprocess.Popen(paths.to_folder_cretin() + 'demo.sh', shell = True , stdout = subprocess.PIPE, stderr = subprocess.PIPE, env = env)
    process.wait() # Wait for process to complete.
    out, err = process.communicate()

    if longprint: print(out.decode())
    if len(err.decode()) > 0: print("ERROR:",err.decode())

# the data generated by cretin can be used for plots 


naming_dict = {
"mesh" : "nodal positions", 
"r" : "nodal positions",
"velocity" : "nodal velocities",
"jnu" : "continuum radiation intensity",
"absn": "continuum absorption",
"emis": "emission",
"jbar" : "line strengths",
"radiation" : "jnu + jbar",
"tev" : "electron tempratures",
"tiv" : "ion tempratures",
"trv" : "radiation tempratures",
"temperatures" : "tev + tiv + trv",
"rho" : "mass densities",
"ne": "electron number densities", 
"ni": "ion number densities",
"yiso" : "iso sequence",
"y"  : "atomic level populations",
"populations" : "ni + yiso + y",
"jsp" : "spectral radiation intensity",
"kappa"  :  "spectral absorption",
"emis" : "spectral emmision",
"spectrum" : "jsp + kappa_sp + emis_sp",
"jbar" : "line strength",
"lines" : "jbar + ylinel + ylineu + sigma",
"radiation" : "jnu + jbar",
"drat" : "mesh + kappa_sp + emis_sp + velocity"
}

def split(name : str):
    splitname = name.split('_')
    key = splitname[0]
    index = '_'.join(splitname[1:])
    return key, index



def blacklist_key(key : str):
    if key in ['previous','ai','zi']:
        return True
    elif key.split('_')[0] in ['model','r', 'u', 'regmap', 'iso']:
        return True
    else:
        return False

def plot(name : str, longprint : bool, plot_duplicates : bool):
    path_test = paths.to_folder_test()
    os.chdir(path_test + '/' + name)
    file_list = glob.glob('*.d*')
    fullpath = path_test + '/' + name + '/' + file_list[0]

    with h5py.File(fullpath, 'r') as f:
        path = path_test + name + '/images'
        if os.path.exists(path):
            shutil.rmtree(path) 
        os.mkdir(path)
            
        print(f'plotting {name} to {path}')

        global arrays2d, arrays3d
        arrays2d, arrays3d = {}, {}
        counter = 0

        for key, value in f.items():
            arr = np.array(f[key])

            
            if longprint: 
                print(f'plot nr \t {counter} \t {key} \t {np.shape(arr)}')
            
            # these never need to be plot
            if blacklist_key(key):
                pass
            elif len(arr.shape) == 0:
                pass

            elif len(arr.shape) == 1 and len(arr) > 0:
                plot2d(path, key, longprint, plot_duplicates, arr)

            elif len(arr.shape) == 2 or len(arr.shape) == 3:
                plot3d(path, key, longprint, plot_duplicates, arr)

            else:
                print(f'{key} has shape {arr.shape} and has not been plot')

            counter += 1


def plot3d(path:str, masterkey:str, longprint:bool, plot_duplicates : bool, arr):
    collapse = are_all_vectors_identical(arr)
    if collapse == 'rows':
        vector = arr[0]
        plot2d(path, masterkey, longprint, plot_duplicates, vector)
    elif collapse == 'columns':
        vector = arr[:, 0]
        plot2d(path, masterkey, longprint, plot_duplicates, vector)

    else:        
        save_bool = True
        for key, array in arrays3d.items():
            if np.shape(array) == np.shape(arr):
                if np.allclose(arr, array):
                    save_bool = False
                    if longprint: print(f"{masterkey} is identical to other array")

        if save_bool or plot_duplicates:
            arrays3d[masterkey] = arr
            fig, ax = plt.subplots()
            im = ax.imshow(arr)
            key, index = split(masterkey)
            if key in naming_dict.keys():
                key = naming_dict[key]+ index
            ax.set_title(key)

            fig.savefig(f'{path}/{key}.png')
            fig.clf(); 
            plt.close()

# for data that is represented as 3d but really should be 2d
def are_all_vectors_identical(arr):
    """
    Check if all vectors in a numpy array are identical.
    """
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

def plot2d(path:str, masterkey:str, longprint:bool, plot_duplicates : bool, arr):
    save_bool = True 
    for key, array in arrays2d.items():
        if np.shape(array) == np.shape(arr):
            if np.allclose(arr, array):
                save_bool = False
                if longprint: print(f"{masterkey} is identical to other array")

    if save_bool or plot_duplicates:
        arrays2d[masterkey] = arr
        plt.plot(arr)
        key, index = split(masterkey)
        if key in naming_dict.keys():
            masterkey = naming_dict[key] + index    
        plt.title(masterkey)
        plt.savefig(f'{path}/{masterkey}.png')
        plt.clf()
        plt.close()



def all(name: str, object, longprint : bool, plot_duplicates : bool):
    write(name, object)
    run(name, longprint)
    plot(name, longprint, plot_duplicates)
