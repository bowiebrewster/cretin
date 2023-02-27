import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# this is the generator file for the cretin .gen files since 
# the goal of this file is to convert the rather archaic generator file with something more intuitive.
# to keep the scope small, i've implemented only the most popular demand (by frequency of implementation in the gen files in the test folder)

# one experiment corresponds too one generator class object, 
# all the data of the simulation is stored in the dictionaries in the init, 
# data is added to those dictionaries via function calls 
class User_input():
    def __init__(self):
        # materials
        self.atoms = []
        self.regions = []

        # sources 
        self.sources = []

    # materials
    def materials_atom(self, element : str, quantum_n_max : int = 10, iso_min : int = None, iso_max : int= None):
        element_input_requirement(element)
        self.atoms.append([element, quantum_n_max, iso_min, iso_max])

    def materials_region(self,nodes :list, elec_temp : float, dimension : int = 1, ion_temp : float = None, rad_temp : float = None):
        if ion_temp == None:
            ion_temp = elec_temp
        if rad_temp == None:
            rad_temp = elec_temp
        interger_input_requirement(dimension, [1,2,3])
        
        self.elements_of_region = []
        self.material_of_region = []
        self.rho_of_region = []
        self.background_of_region = []
        # this works retroactively, I put the material_of_region list inside the self.region, if i later change 
        # the list it gets changed while its in the self.region
        self.region0 = [dimension, nodes, elec_temp, ion_temp, rad_temp]
        self.regions.append((self.region0, self.elements_of_region, self.material_of_region, self.rho_of_region, self.background_of_region))

    def materials_region_rho(self, rho : float):
        self.rho_of_region.append(rho)

    def materials_region_element(self, iz : int, initial_ion_population : float):
        self.elements_of_region.append([iz, initial_ion_population])

    def materials_region_material(self, rho : float, atom_n : float, charge_avg : float, charge_avg_squared: float):
        self.material_of_region.append([rho, atom_n, charge_avg, charge_avg_squared])

    def materials_region_background(self, ion_density: float, electron_density: float, avg_atomic_number : float, average_charge: float, average_charge_squared : float):
        self.background_of_region.append([ion_density, electron_density, avg_atomic_number, average_charge, average_charge_squared])

    def geometry(self, type : str = 'plane'):
        string_input_requirement(type, ['none','plane','slab','cylinder','sphere','wedge','xy','rz', 'xyz'])
        self.geometry = type
        self.geom_nodes = []

    def geometry_nodes(self, coordinate : str, scaling_type: str, node1 : int, node2: int, min : float, max: float, ratio : float = None, drmin : float = None, slope : float = None):
        string_input_requirement(coordinate, ['r','x','y','x'])
        string_input_requirement(scaling_type, ['lin','log','geom','exp'])
        self.geom_nodes.append([coordinate, scaling_type, node1, node2, min, max, ratio, drmin, slope])

    def geometry_quad(self, node_1 : list, node_2: list, x_cors : list, y_cors :list, ratios: list):
        list_input_requirement([node_1, node_2, x_cors, y_cors, ratios])
        self.geom_quad = [node_1, node_2, x_cors, y_cors]

    def radiation_ebins(self, n_boundaries: int, start: float, end : float, ratio : float = None):
        self.rad_ebins  = [n_boundaries, start, end, ratio]

    def radiation_angles(self, n_rays : int, n_angles : int = None):
        self.rad_angles = [n_rays, n_angles]

    def radiation_lbins(self, n_bins : int, energy_span_1 : float, ratio_width1: float, energy_span_2 : float, ratio_width2: float):
        self.rad_lbins = [n_bins, energy_span_1, ratio_width1, energy_span_2, ratio_width2]

    def source_laser(self, laser_wavelength : float, option_1 : str, option_2 : str, x_maxima : list, y_maxima : list = None, z_maxima : list = None):
        list_input_requirement([x_maxima, y_maxima, z_maxima])
        string_input_requirement(option_1, ['value', 'rate', 'integral', 'initial'])
        string_input_requirement(option_2, ['xfile', 'history', 'profile', 'svlist','constant'])

        self.sources.append(["laser", laser_wavelength, option_1, option_2, x_maxima, y_maxima, z_maxima])
    
    def source_jbndry(self, index : float, E_min : float, E_max : float, option_1 : str, option_2 : str, x_maxima : list, y_maxima : list = None, z_maxima : list = None):
        string_input_requirement(option_1, ['value', 'rate', 'integral', 'initial'])
        string_input_requirement(option_2, ['xfile', 'history', 'profile', 'svlist','constant'])
        list_input_requirement([x_maxima, y_maxima, z_maxima])

        self.sources.append(['jbndry',index, E_min, E_max, option_1, option_2, x_maxima, y_maxima, z_maxima])

    def source_jnu(self, E_min, E_max, option_1 : str, option_2 : str, x_maxima : list, y_maxima : list = None, z_maxima : list = None):
        string_input_requirement(option_1, ['value', 'rate', 'integral', 'initial'])
        string_input_requirement(option_2, ['xfile', 'history', 'profile', 'svlist','constant'])
        list_input_requirement([x_maxima, y_maxima, z_maxima])

        self.sources.append(['jnu', E_min, E_max, option_1, option_2, x_maxima, y_maxima, z_maxima])

    def controls(self, t_start : float, t_end : float, restart : bool = False, edits : bool = False):
        self.control = [t_start, t_end, restart, edits]

    def popular_switches(self, include_degeneracy : str = None, timestep_between_snapshot : int = 1000, time_step_control : str = 'use_dynamic_timesteps', line_transfer : str = None, kinematics = 'calculate approx. LTE and QSS distributions', continuum_transfer : str = None):
        if include_degeneracy == None:
            string0 = None
        else:
            include_degeneracy_dict = {'include electron_degeneracy' : .5,' ignore additional correction for ionizations' : -.5,'integrate collisional ionizations numerically': 1.5,'integrate collisional excitations numerically': 2.5}
            string_input_requirement(include_degeneracy, include_degeneracy_dict.values())
            string0 = 'switch 151 '+include_degeneracy_dict[include_degeneracy]
            
        string_input_requirement(time_step_control, ['use constant timesteps', 'use_dynamic_timesteps'])
        if line_transfer != None:
            string_input_requirement(line_transfer, ['do steady-state line transfer', 'do time-dependent line transfer'])
        string_input_requirement(kinematics, ['calculate approx. LTE and QSS distributions','time-dependent kinetics','use approx. LTE and QSS distributions to choose LTE or NLTE','steady-state kinetics','no kinetics'])
        if continuum_transfer != None:
            string_input_requirement(continuum_transfer, ['do steady-state continuum transfer','do time-dependent continuum transfer','1-d: use Feautrier formalism, integral formalism otherwise'])
        self.pop_switches = [string0, timestep_between_snapshot, time_step_control, line_transfer, kinematics, continuum_transfer]

    def other_switches(self):
        pass
        """
        28 1 ! steady-state initialization                   8
        100 1 ! do radiation                                 8
        55 1 ! do continuum lowering                         7
        11 1 ! make ascii plot file                          6
        38 1 ! symmetric line profiles                       6
        44 10 ! maximum # of iterations                      5
        111 1 ! iterate zones independently                  5
        """


def list_input_requirement(lis):
    for input in lis: 
        if input != None: 
            if len(input) != 2: 
                raise Exception("list of size 2 required")
            for value in input:
                if (type(value) != type(1)) and (type(value) != type(1.)): 
                    raise Exception('list must contain int or float')

def string_input_requirement(string: str, options: list):
    opt = ', '.join(options)
    if string not in options: 
        fstrin = f'{string} is not one of: {opt}'
        raise Exception(fstrin)

def element_input_requirement(element: str):
    if 'element_list' not in globals():
        global element_list
        df = pd.read_csv('periodic_table.csv')
        element_list = df['Symbol'].to_string(index=False)

    if element.upper() not in (name.upper() for name in element_list): 
        raise Exception('must be one of H, HE, LI, BE ...')
    
def interger_input_requirement(inter : int, options : list):
    if inter not in options:
        fstrin = f'{inter} is not one of: {options}'
        raise Exception(fstrin)

