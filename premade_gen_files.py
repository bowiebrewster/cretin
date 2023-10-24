# here we are running all the premades .gen files in the test folder
import os
import paths
import write_run_plot

def run_premades(sub_name:str = None):

    for file_name in os.listdir(paths.to_personal_data()):
        if sub_name in file_name:
            write_run_plot.run(file_name, longprint=False)
            write_run_plot.plot(file_name, longprint=False, plot_duplicates=False)
        elif sub_name == None:
            write_run_plot.run(file_name, longprint=False)
            write_run_plot.plot(file_name, longprint=False, plot_duplicates=False)

        else:
            raise Exception('name not present in any files in test folder')

