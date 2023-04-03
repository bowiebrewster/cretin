from importlib import reload
import generator_object, to_generator_string, search, paths, write_run_plot, serial_sim_tools #these python classes should be in the same folder as cretin_main
for obj in [generator_object, to_generator_string, search, paths, write_run_plot, serial_sim_tools]:
    reload(obj)
import numpy as np
import os, shutil
import matplotlib.pyplot as plt
# this is an absolute monstrosity of string manipulation, do not judge me father.

path = paths.to_folder_test()
data = {}
start_lines = []
plot_count = 0

def restructure(line : str, count : int):
    if line[0] == '#' and ':' in line:
        key = line.split(':')[1].strip(' ')
        start_lines.append(count)

    elif count -1 in start_lines:
        global plot_count, vars, data
        plot_count +=1
        vars = line.split('         ')

        vars = [var.strip(' ').strip('$') for var in vars]
        if vars[-1] == '\n':
            vars = vars[0:-1]

        if '\n' in vars[-1]:
            vars[-1] = ' '.join(vars[-1].split('\n')[:-1]).strip(' ')

        vars[0] = vars[0].strip(' ')
        vars = [plot_count] + vars

        vars = tuple(vars)
        data[vars] = []


    if line[0] not in ['$', '#'] and 'vars' in globals():
        line = line.split(' ')
        line[-1] =' '.join(line[-1].split('\n')[:-1])

        newline = []
        for entry in line:
            if len(entry) >3:
                newline.append(entry)

        lis =  data[vars].append(newline)


def txt_to_plot(name : str):
    folder = f'{path}{name}'

    with open(f'{folder}/{name}.plt') as f:
        lines = f.readlines()

        
        for count, line in enumerate(lines):
            restructure(line, count)

    
    if os.path.exists(f'{folder}/images'):
        shutil.rmtree(f'{folder}/images') 
    os.mkdir(f'{folder}/images')

    for key, value in data.items():

        value = np.array(value, dtype=object)

        try:
            value = value.astype('float')

            col_count = 0
            for column in value.T:
                if col_count == 0:
                    col0 = column

                else:
                    plt.plot(col0, column)
                    plt.title(key)
                    plt.savefig(f'{folder}/images/{str(key[0])}.png')
                    plt.clf()
                    plt.close()


                col_count += 1
        except:
            print(f'error with {key}')
            
    print(f'finished writing too {folder}/images')

