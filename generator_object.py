import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# this is the class that creates the generator class object which stores the user input and makes it accesible, readable and returns error messages.
# this class allows ur to write readable intuitive code in the main cretin ipynb notebook using the full 
# capabilities of python

class User_input():
    def __init__(self):
        # materials
        self.atoms = []
        self.regions = []

        # sources 
        self.sources = []
        self.sources_aprd = []

    # materials
    def materials_atom(self, element : str, quantum_n_max : int = 10, iso_min : int = None, iso_max : int= None):
        element_input_requirement(element)

        self.modeltype_of_atom =[]
        self.atom0 = [element, quantum_n_max, iso_min, iso_max]
        self.atoms.append([self.atom0, self.modeltype_of_atom])

    def materials_atom_modeltype(self, type1 : str, type2 : str):
        string_input_requirement(type1, ['fly','term','dca','radonly','sublevel','johnson'])
        string_input_requirement(type2, ['fly','term','dca','radonly','sublevel','johnson'])
        self.modeltype_of_atom.append([type1, type2])

    def materials_region(self,nodes :list, elec_temp : float, dimension : int = 1, ion_temp : float = None, rad_temp : float = None):
        if ion_temp == None:
            ion_temp = elec_temp
        if rad_temp == None:
            rad_temp = elec_temp
        interger_input_requirement(dimension, [1,2,3])
        
        self.elements_of_region, self.material_of_region, self.rho_of_region= [], [], []
        self.background_of_region, self.opacity_of_region, level_of_region  = [], [], []

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

    def materials_region_background(self, ion_density: float, electron_density: float, avg_atomic_number : float,
                                     average_charge: float, average_charge_squared : float):
        self.background_of_region.append([ion_density, electron_density, avg_atomic_number, average_charge, average_charge_squared])

    def materials_region_opacity(self, form : str , p_vals : list, e_vals : list):
        # see page 26 of documentation for exact fomulas corresponding to forms
        string_input_requirement(form, ['constant', 'power-law','exponential','gaussian','cutoff'])
        self.opacity_of_region.append([form, p_vals, e_vals])

    def materials_region_level(self, iz : int, isoelectronic_sequence : int, level : int, iso_range : list = None):
        list_input_requirement(iso_range)
        self.level_of_region.append([iz, isoelectronic_sequence, level, iso_range])

    def geometry(self, type : str = 'plane'):
        string_input_requirement(type, ['none','plane','slab','cylinder','sphere','wedge','xy','rz', 'xyz'])
        self.geometry = type
        self.geom_nodes = []

    def geometry_nodes(self, coordinate : str, scaling_type: str, node1 : int, node2: int, min : float, 
                       max: float, ratio : float = None, drmin : float = None, slope : float = None):
        string_input_requirement(coordinate, ['r','x','y','x'])
        string_input_requirement(scaling_type, ['lin','log','geom','exp'])
        self.geom_nodes.append([coordinate, scaling_type, node1, node2, min, max, ratio, drmin, slope])

    def geometry_quad(self, node_1 : list, node_2: list, x_cors : list, y_cors :list, ratios: list):
        list_input_requirement([node_1, node_2, x_cors, y_cors, ratios])
        self.geom_quad = [node_1, node_2, x_cors, y_cors]

    def geometry_product_mesh(self, product_mesh: bool = False):
        self.prod_mesh = product_mesh

    def radiation_ebins(self, n_boundaries: int, start: float, end : float, ratio : float = None):
        self.rad_ebins  = [n_boundaries, start, end, ratio]

    def radiation_angles(self, n_rays : int, n_angles : int = None):
        self.rad_angles = [n_rays, n_angles]

    # TODO should be part of line
    def radiation_lbins(self, n_bins : int, energy_span_1 : float, ratio_width1: float, energy_span_2 : float, ratio_width2: float):
        self.rad_lbins = [n_bins, energy_span_1, ratio_width1, energy_span_2, ratio_width2]

    def radiation_line(self, index : int, model : int, lower_state : list, higher_state : list):
        self.rad_line = [index, model, lower_state, higher_state]

    def radiation_spectrum(self, n_energies : int, energy_range : list, ratio : float):
        self.rad_spectrum = [n_energies, energy_range, ratio]

    def radiation_aprd(self, voigt_paramters : list):
        self.sources_aprd.append(voigt_paramters)
    
    def source_boundary(self, type : str, node_ir : float = None, node_1 : list = None, node_2 : list = None, node3 : list = None):
        string_input_requirement(type, ['streaming', 'milne','value'])
        if node_ir != None and node_1 == None and node_2 == None and node3 == None:
            pass #type1
        elif node_ir == None and node_1 != None and node_2 != None and node3 == None:
            pass #type2
        elif node_ir == None and node_1 != None and node_2 != None and node3 != None:
            pass #type3
        else:
            raise Exception(""" the only allowed combinations are as follows:
            boundary package type ir [history id] multiplier value or
            boundary package type k1 k2 l1 l2 [history id] value or
            boundary package type k1 k2 l1 l2 m1 m2 [history id] value
            """)

        self.source_bound = [type, node_ir, node_1, node_2, node3]

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

    # TODO
    def source_rswitch(self):
        pass

    def controls(self, t_start : float, t_end : float, restart : bool = False, edits : bool = False):
        self.control = [t_start, t_end, restart, edits]

    def popular_switches(self, include_degeneracy : str = None, timestep_type : str = None, continuum_transfer : str = None,
                          continuum_transfer_evolves_temp : bool = False, timestep_between_snapshot : int = None, kinematics : str = None):
        # TODO include switch 11, 28, 30, 55
        
        # using the gather_data.ipynb file i've searched for the most common switches 
        if include_degeneracy == None:
            string0 = None
        else:
            include_degeneracy_dict = {'include electron degeneracy' : .5,' ignore additional correction for ionizations' : -.5,
                                       'integrate collisional ionizations numerically': 1.5,'integrate collisional excitations numerically': 2.5}
            string_input_requirement(include_degeneracy, include_degeneracy_dict.keys())
            string0 = 'switch 151 '+str(include_degeneracy_dict[include_degeneracy])

        if timestep_type == None:
            string1 = None
        else:
            time_step_dict = {'use constant timesteps' : -1, 'use_dynamic_timesteps' : 1}
            string_input_requirement(timestep_type, time_step_dict.keys())   
            string1 = 'switch 29 '+str(time_step_dict[timestep_type])

        if continuum_transfer == None:
            string2 = None
        else:
            continuum_transfer_dict = {'do steady-state continuum transfer': .5, 'do time-dependent continuum transfer':-.5, '1-d: use Feautrier formalism, integral formalism otherwise': 1}
            string_input_requirement(continuum_transfer, continuum_transfer_dict.keys())   
            string2 = 'switch 36 '+str(continuum_transfer_dict[continuum_transfer])

        if continuum_transfer_evolves_temp == False:
            string3 = None
        else:
            string3 = 'switch 100 1'

        if timestep_between_snapshot == None:
            string4 = None
        else:
            string4  = 'switch 30 '+str(timestep_between_snapshot)

        if kinematics == None:
            string5 = None
        else:
            kinematics_dict = {'steady-state kinetics': 0, 'time-dependent kinetics':.5, 'use approx. LTE and QSS distributions to choose LTE or NLTE': 1.5, 'calculate approx. LTE and QSS distribution': -1, 'no kinetics':-1.5}
            string_input_requirement(kinematics, kinematics_dict.keys())   
            string5 = 'switch 25 '+str(kinematics_dict[kinematics])

        self.pop_switches = [string0, string1, string2, string3, string4, string5]

    # TODO
    def pop_paramters():
        pass
    
    # TODO
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
