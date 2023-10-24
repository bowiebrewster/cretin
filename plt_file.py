from importlib import reload
import paths 
reload(paths)
import numpy as np
import matplotlib.pyplot as plt

# We use this file to turn existing data structure 



# for .plt files created by cretin we extract the data here
path = paths.to_personal_data()

# this is an absolute monstrosity of string manipulation
def restructure(line : str, count : int):
    if line[0] == '#':
        name = line.split(' ')[1]
        start_lines[name] = count

    elif count -1 in start_lines.values():
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

        data[vars].append(newline)


def txt_to_plot(folder_name : str, multiplot : bool = False):
    folder = f'{path}{folder_name}'
    global data, start_lines, plot_count
    data, start_lines, plot_count = {},{},0

    
    with open(f'{folder}/{folder_name}.plt') as f:
        lines = f.readlines()

        for count, line in enumerate(lines):
            restructure(line, count)

    if multiplot:
        return data
    
    for key, value in data.items():

        value = np.array(value)
        value = value.astype('float')

        col_count = 0
        for column in value.T:
            if col_count == 0:
                col0 = column
            else:
                plt.plot(col0, column)
            col_count += 1

        plt.title(f'added plot {key}')
        plt.xlabel(key[1])
        plt.ylabel(key[2])
        plt.savefig(f'{folder}/images/{key}.png')
        plt.clf()
        plt.close()

    del data, start_lines, plot_count                    


