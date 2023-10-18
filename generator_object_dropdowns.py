import ipywidgets as widgets
from ipywidgets import HBox
from IPython.display import display
import pandas as pd
import paths
#this is a casual 1600 line python file what about it


class User_input():
    def __init__(self):
        # materials
        self.atoms = []
        self.regions = []

        # sources 
        self.sources = []
        self.sources_aprd = []

        # plots
        self.plots = []

        # histories 
        self.source_histories = []

    # Define your function
    def drop_source_jnu(self):
        # Create interactive widgets for all arguments
        self.E_range_input = widgets.Text(
            description="energy range (list):",
            placeholder="[1, 2]",
            layout=widgets.Layout(width="200px"))

        self.option_1_dropdown = widgets.Dropdown(
            options=['value', 'rate', 'integral', 'initial'],
            description="option 1:",
            layout=widgets.Layout(width="200px"))

        self.option_2_dropdown = widgets.Dropdown(
            options=['xfile', 'history', 'profile', 'svlist', 'constant'],
            description="option 2:",
            layout=widgets.Layout(width="200px"))

        self.values_input = widgets.Text(
            description="values (list):",
            placeholder="[10, 20, 30]",
            layout=widgets.Layout(width="200px"))

        self.nodes_input = widgets.Text(
            description="nodes (list):",
            placeholder="[A, B, C]",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add jnu source")
        def on_button_click(b):
            E_range_value = eval(self.E_range_input.value)
            option_1_value = self.option_1_dropdown.value
            option_2_value = self.option_2_dropdown.value
            values_value = eval(self.values_input.value)
            nodes_value = eval(self.nodes_input.value)

            self.lasray_lis = []
            data = ['jnu', E_range_value, option_1_value, option_2_value, values_value, nodes_value, self.lasray_lis]
            self.sources.append(data)

        self.button.on_click(on_button_click)


        # Display the widgets
        display(HBox([self.E_range_input, self.option_1_dropdown, self.option_2_dropdown, self.values_input, self.nodes_input, self.button],layout = widgets.Layout(flex_flow='wrap')))


    def drop_source_jbndry(self):

        # Create interactive widgets for all arguments
        self.index_input = widgets.IntText(
            description="index:",
            value=0,
            layout=widgets.Layout(width="200px"))

        self.E_range_input = widgets.Text(
            description="energy range (list):",
            placeholder="[1, 2]",
            layout=widgets.Layout(width="200px"))

        self.option_1_dropdown = widgets.Dropdown(
            options=['value', 'rate', 'integral', 'initial'],
            description="option_1:",
            layout=widgets.Layout(width="200px"))

        self.option_2_dropdown = widgets.Dropdown(
            options=['xfile', 'history', 'profile', 'svlist', 'constant'],
            description="option_2:",
            layout=widgets.Layout(width="200px"))

        self.values_input = widgets.Text(
            description="values (list):",
            placeholder="[10, 20, 30]",
            layout=widgets.Layout(width="200px"))

        self.nodes_input = widgets.Text(
            description="nodes (list):",
            placeholder="[A, B, C]",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add jbndry source")

        # Define your function
        def on_button_click(b):
            index_value = self.index_input.value
            E_range_value = eval(self.E_range_input.value)
            option_1_value = self.option_1_dropdown.value
            option_2_value = self.option_2_dropdown.value
            values_value = eval(self.values_input.value)
            nodes_value = eval(self.nodes_input.value) if self.nodes_input.value else None

            self.lasray_lis = []
            data = ['jbndry', index_value, E_range_value, option_1_value, option_2_value, values_value, nodes_value, self.lasray_lis]
            self.sources.append(data)

        self.button.on_click(on_button_click)

        # Display the widgets
        display(HBox([self.index_input, self.E_range_input, self.option_1_dropdown, self.option_2_dropdown, self.values_input, self.nodes_input, self.button], layout = widgets.Layout(flex_flow='wrap')))


    def drop_source_laser(self):

        # Create interactive widgets for all arguments
        self.laser_wavelength_input = widgets.FloatText(
            description="laser wavelength:",
            value=0.0,
            layout=widgets.Layout(width="200px"))

        self.option_1_dropdown = widgets.Dropdown(
            options=['value', 'rate', 'integral', 'initial'],
            description="option 1:",
            layout=widgets.Layout(width="200px"))

        self.option_2_dropdown = widgets.Dropdown(
            options=['xfile', 'history', 'profile', 'svlist', 'constant'],
            description="option 2:",
            layout=widgets.Layout(width="200px"))

        self.values_input = widgets.Text(
            description="values (list):",
            placeholder="[10, 20, 30]",
            layout=widgets.Layout(width="200px"))

        self.nodes_input = widgets.Text(
            description="nodes (list):",
            placeholder="[A, B, C]",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add laser source")

        # Define your function
        def on_button_click(b):
            laser_wavelength_value = self.laser_wavelength_input.value
            option_1_value = self.option_1_dropdown.value
            option_2_value = self.option_2_dropdown.value
            values_value = eval(self.values_input.value)
            nodes_value = eval(self.nodes_input.value)

            self.lasray_lis = []
            data = ['laser', laser_wavelength_value, option_1_value, option_2_value, values_value, nodes_value, self.lasray_lis]
            self.sources.append(data)

        self.button.on_click(on_button_click)

        # Display the widgets
        display(widgets.HBox([self.laser_wavelength_input, self.option_1_dropdown, self.option_2_dropdown, self.values_input, self.nodes_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_source_boundary(self):

        # Create interactive widgets for all arguments
        self.package_dropdown = widgets.Dropdown(
            options=['radiation', 'conduction', 'hydro', 'velocity', 'pressure', 'divertor', 'current', 'all'],
            description="package:",
            layout=widgets.Layout(width="200px"))

        self.type_dropdown = widgets.Dropdown(
            options=["value","gradient", "flux", "reflecting", "mirror", "milne", "isotropic", "streaming","recycling"],
            description="type:",
            layout=widgets.Layout(width="200px"))

        self.nodes_input = widgets.Text(
            description="nodes (list):",
            placeholder="[A, B, C]",
            layout=widgets.Layout(width="200px"))

        self.value_input = widgets.FloatText(
            description="value:",
            value=0.0,
            layout=widgets.Layout(width="200px"))

        self.mult_input = widgets.FloatText(
            description="mult (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Specifiy boundary conditions for package-type pairing", layout=widgets.Layout(width="400px"))

        # Define your function
        def on_button_click(b):
            package_value = self.package_dropdown.value
            type_value = self.type_dropdown.value
            nodes_value = eval(self.nodes_input.value)
            value_value = self.value_input.value
            mult_value = self.mult_input.value if self.mult_input.value is not None else None

            if len(nodes_value) not in [1, 4, 6]:
                raise Exception("""The only allowed combinations are as follows:
                1) boundary package type [ir] (history id) multiplier value or
                2) boundary package type [k1 k2 l1 l2] (history id) value or
                3) boundary package type [k1 k2 l1 l2 m1 m2] (history id) value
                """)

            self.source_bound = [package_value, type_value, nodes_value, mult_value, value_value]
            self.lasray_lis = []
            data = ['boundary', self.source_bound, self.lasray_lis]
            self.source_boundaries = data

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.package_dropdown, self.type_dropdown, self.nodes_input, self.value_input, self.mult_input, self.button], layout = widgets.Layout(flex_flow='wrap')))


    def drop_source_lasray(self):
        # Create interactive widgets for all arguments
        self.entrance_position_input = widgets.FloatText(
            description="Entrance Position:",
            layout=widgets.Layout(width="200px"),
            value=0.0)  # Default value set to 0.0

        self.entrance_direction_mu_input = widgets.FloatText(
            description="Entrance Direction (mu):",
            layout=widgets.Layout(width="200px"),
            value=0.0)  # Default value set to 0.0

        self.entrance_direction_phi_input = widgets.FloatText(
            description="Entrance Direction (phi):",
            layout=widgets.Layout(width="200px"),
            value=0.0)  # Default value set to 0.0

        self.fractional_power_input = widgets.FloatText(
            description="Fractional Power:",
            layout=widgets.Layout(width="200px"),
            value=0.0)  # Default value set to 0.0

        self.res_frac_input = widgets.FloatText(
            description="Resolution Fraction (Optional):",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add Lasray")

        # Define your function
        def on_button_click(b):
            entrance_position_value = self.entrance_position_input.value
            entrance_direction_mu_value = self.entrance_direction_mu_input.value
            entrance_direction_phi_value = self.entrance_direction_phi_input.value
            fractional_power_value = self.fractional_power_input.value
            res_frac_value = self.res_frac_input.value

            if not hasattr(self, 'lasray_lis'):
                raise Exception('lasray command must be added after laser command')
            else:
                lasray_data = [entrance_position_value, entrance_direction_mu_value,
                               entrance_direction_phi_value, fractional_power_value, res_frac_value]
                self.lasray_lis.append(lasray_data)

        self.button.on_click(on_button_click)

        # Display the widgets
        display(HBox([self.entrance_position_input, self.entrance_direction_mu_input, self.entrance_direction_phi_input,
                      self.fractional_power_input, self.res_frac_input, self.button]))


    def drop_geometry_quad(self):

        # Create interactive widgets for all arguments
        self.node_1_input = widgets.Text(
            description="node 1 (list):",
            placeholder="[x1, y1]",
            layout=widgets.Layout(width="200px"))

        self.node_2_input = widgets.Text(
            description="node 2 (list):",
            placeholder="[x2, y2]",
            layout=widgets.Layout(width="200px"))

        self.x_cors_input = widgets.Text(
            description="x cors (list):",
            placeholder="[x1, x2]",
            layout=widgets.Layout(width="200px"))

        self.y_cors_input = widgets.Text(
            description="y cors (list):",
            placeholder="[y1, y2]",
            layout=widgets.Layout(width="200px"))

        self.ratios_input = widgets.Text(
            description="ratios (list):",
            placeholder="[ratio1, ratio2]",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add quad geometry")

        # Define your function
        def on_button_click(b):
            node_1_value = eval(self.node_1_input.value)
            node_2_value = eval(self.node_2_input.value)
            x_cors_value = eval(self.x_cors_input.value)
            y_cors_value = eval(self.y_cors_input.value)
            ratios_value = eval(self.ratios_input.value)

            self.geom_quad = [node_1_value, node_2_value, x_cors_value, y_cors_value]

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.node_1_input, self.node_2_input, self.x_cors_input, self.y_cors_input, self.ratios_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_geometry_product_mesh(self):

        # Create interactive widgets for all arguments
        self.product_mesh_checkbox = widgets.Checkbox(
            description="make 2d/3d mesh from 1d meshing command",
            value=False,
            layout=widgets.Layout(width="400px"))

        self.button = widgets.Button(description="Add product mesh")

        # Define your function
        def on_button_click(b):
            product_mesh_value = self.product_mesh_checkbox.value
            self.prod_mesh = product_mesh_value

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.product_mesh_checkbox, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_radiation_ebins(self):

        # Create interactive widgets for all arguments
        self.n_boundaries_input = widgets.IntText(
            description="number of group boundaries:",
            value=0,
            layout=widgets.Layout(width="200px"))

        self.start_input = widgets.FloatText(
            description="start:",
            value=0.0,
            layout=widgets.Layout(width="200px"))

        self.end_input = widgets.FloatText(
            description="end:",
            value=0.0,
            layout=widgets.Layout(width="200px"))

        self.ratio_input = widgets.FloatText(
            description="ratio (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Define group structure for continuum radiation",layout=widgets.Layout(width="300px"))

        # Define your function
        def on_button_click(b):
            n_boundaries_value = self.n_boundaries_input.value
            start_value = self.start_input.value
            end_value = self.end_input.value
            ratio_value = self.ratio_input.value if self.ratio_input.value is not None else None

            self.rad_ebins = [n_boundaries_value, start_value, end_value, ratio_value]

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.n_boundaries_input, self.start_input, self.end_input, self.ratio_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_radiation_angles(self):

        # Create interactive widgets for all arguments
        self.n_rays_input = widgets.IntText(
            description="number of rays:",
            value=0,
            layout=widgets.Layout(width="200px"))

        self.n_angles_input = widgets.IntText(
            description="number of angles (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Set rays for transfer problems")

        # Define your function
        def on_button_click(b):
            n_rays_value = self.n_rays_input.value
            n_angles_value = self.n_angles_input.value if self.n_angles_input.value is not None else None

            self.rad_angles = [n_rays_value, n_angles_value]

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.n_rays_input, self.n_angles_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_radiation_line(self):

        # Create interactive widgets for all arguments
        self.index_input = widgets.IntText(
            description="index:",
            value=0,
            layout=widgets.Layout(width="200px"))

        self.model_input = widgets.IntText(
            description="model:",
            value=0,
            layout=widgets.Layout(width="200px"))

        self.lower_state_input = widgets.Text(
            description="lower state (list):",
            placeholder="[state1, state2]",
            layout=widgets.Layout(width="200px"))

        self.higher_state_input = widgets.Text(
            description="higher state (list):",
            placeholder="[state3, state4]",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Define radiative transiition", layout=widgets.Layout(width="200px"))

        # Define your function
        def on_button_click(b):
            index_value = self.index_input.value
            model_value = self.model_input.value
            lower_state_value = eval(self.lower_state_input.value)
            higher_state_value = eval(self.higher_state_input.value)

            self.rad_line = [index_value, model_value, lower_state_value, higher_state_value]
            self.rad_lbins = []

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.index_input, self.model_input, self.lower_state_input, self.higher_state_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_radiation_lbins(self):
        # Create interactive widgets for all arguments
        self.n_bins_input = widgets.IntText(
            description="number of Bins:",
            layout=widgets.Layout(width="200px"))

        self.energy_span1_input = widgets.FloatText(
            description="energy Span 1:",
            layout=widgets.Layout(width="200px"))

        self.ratio_width1_input = widgets.FloatText(
            description="ratio Width 1:",
            layout=widgets.Layout(width="200px"))

        self.energy_span2_input = widgets.FloatText(
            description="energy Span 2:",
            layout=widgets.Layout(width="200px"))

        self.ratio_width2_input = widgets.FloatText(
            description="ratio Width 2:",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Define bin structure")

        # Define your function
        def on_button_click(b):
            n_bins_value = self.n_bins_input.value
            energy_span1_value = self.energy_span1_input.value
            ratio_width1_value = self.ratio_width1_input.value
            energy_span2_value = self.energy_span2_input.value
            ratio_width2_value = self.ratio_width2_input.value

            lbins_data = [n_bins_value, energy_span1_value, ratio_width1_value, energy_span2_value, ratio_width2_value]
            self.rad_lbins.append(lbins_data)

            # Clear input fields after adding the bins
            self.n_bins_input.value = None
            self.energy_span1_input.value = None
            self.ratio_width1_input.value = None
            self.energy_span2_input.value = None
            self.ratio_width2_input.value = None

        self.button.on_click(on_button_click)

        # Display the widgets
        display(HBox([self.n_bins_input, self.energy_span1_input, self.ratio_width1_input,
                      self.energy_span2_input, self.ratio_width2_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_materials_region_material(self):

        # Create interactive widgets for all arguments
        self.rho_input = widgets.FloatText(
            description="density:",
            value=6.9,
            layout=widgets.Layout(width="200px"))

        self.atom_n_input = widgets.FloatText(
            description="atom n:",
            value=1,
            layout=widgets.Layout(width="200px"))

        self.charge_avg_input = widgets.FloatText(
            description="average charge Z:",
            value=11,
            layout=widgets.Layout(width="200px"))

        self.charge_avg_squared_input = widgets.FloatText(
            description="average charge squared:",
            value=121,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add material to region")

        # Define your function
        def on_button_click(b):
            rho_value = self.rho_input.value
            atom_n_value = self.atom_n_input.value
            charge_avg_value = self.charge_avg_input.value
            charge_avg_squared_value = self.charge_avg_squared_input.value

            self.material_of_region.append([rho_value, atom_n_value, charge_avg_value, charge_avg_squared_value])

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.rho_input, self.atom_n_input, self.charge_avg_input, self.charge_avg_squared_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_materials_region_background(self):

        # Create interactive widgets for all arguments
        self.ion_density_input = widgets.FloatText(
            description="ion density:",
            value=0.0,
            layout=widgets.Layout(width="200px"))

        self.electron_density_input = widgets.FloatText(
            description="electron density:",
            value=0.0,
            layout=widgets.Layout(width="200px"))

        self.avg_atomic_number_input = widgets.FloatText(
            description="avg atomic number:",
            value=0.0,
            layout=widgets.Layout(width="200px"))

        self.average_charge_input = widgets.FloatText(
            description="average charge Z:",
            value=0.0,
            layout=widgets.Layout(width="200px"))

        self.average_charge_squared_input = widgets.FloatText(
            description="average charge squared:",
            value=0.0,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add region backgrond")

        # Define your function
        def on_button_click(b):
            ion_density_value = self.ion_density_input.value
            electron_density_value = self.electron_density_input.value
            avg_atomic_number_value = self.avg_atomic_number_input.value
            average_charge_value = self.average_charge_input.value
            average_charge_squared_value = self.average_charge_squared_input.value

            self.background_of_region.append([ion_density_value, electron_density_value, avg_atomic_number_value, average_charge_value, average_charge_squared_value])

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.ion_density_input, self.electron_density_input, self.avg_atomic_number_input, self.average_charge_input, self.average_charge_squared_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_materials_region_opacity(self):

        # Create interactive widgets for all arguments
        self.form_dropdown = widgets.Dropdown(
            options=['constant: p1', 'power-law: p1 ρ^p2 T^p3 Exp(p4)', 'exponential: p1 ρ^p2 T^p3 Exp(-(e-p4)/p5)', 'gaussian: p1 ρ^p2 T^p3 Exp(-(e-p4)/p5)^2','cosine: p1 ρ^p2 T^p3 Cos(-(e-p4)/p5)', 'cutoff: p1 p5 ρ^p2 T^p3 e^p4, p5=1 if e < p6,'],
            description="form:",
            layout=widgets.Layout(width="200px"))

        self.p_vals_input = widgets.Text(
            description="p values (list):",
            placeholder="[p1, p2...]",
            layout=widgets.Layout(width="200px"))

        self.e_vals_input = widgets.Text(
            description="valid photon energy range (list):",
            placeholder="[e1, e2]",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Set opacity behaviour")

        # Define your function
        def on_button_click(b):
            form_value = self.form_dropdown.value
            p_vals_value = eval(self.p_vals_input.value)
            e_vals_value = eval(self.e_vals_input.value)

            string_input_requirement(form_value, ['constant', 'power-law', 'exponential', 'gaussian', 'cutoff'])

            self.opacity_of_region.append([form_value, p_vals_value, e_vals_value])

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.form_dropdown, self.p_vals_input, self.e_vals_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_materials_region_level(self):

        # Create interactive widgets for all arguments
        self.index_input = widgets.IntText(
            description="index:",
            value=0,
            layout=widgets.Layout(width="200px"))

        self.isoelectronic_sequence_input = widgets.IntText(
            description="isoelectronic sequence:",
            value=0,
            layout=widgets.Layout(width="200px"))

        self.level_input = widgets.IntText(
            description="level:",
            value=0,
            layout=widgets.Layout(width="200px"))

        self.iso_range_input = widgets.Text(
            description="iso range (list, optional):",
            placeholder="[iso1, iso2]",
            layout=widgets.Layout(width="200px"))
        
        self.ion_density = widgets.Text(
            description="ion density",
            placeholder="6.9",
            layout=widgets.Layout(width="200px"))


        self.button = widgets.Button(description="Assign ion population to element iso-sequnce pair",layout=widgets.Layout(width="350px"))

        # Define your function
        def on_button_click(b):
            index_value = self.index_input.value
            isoelectronic_sequence_value = self.isoelectronic_sequence_input.value
            level_value = self.level_input.value
            ion_density = self.ion_density.value
            iso_range_value = eval(self.iso_range_input.value) if self.iso_range_input.value else None

            list_input_requirement([iso_range_value])

            self.level_of_region.append([index_value, isoelectronic_sequence_value, level_value, ion_density, iso_range_value])

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.index_input, self.isoelectronic_sequence_input, self.level_input, self.ion_density, self.iso_range_input, self.button], 
                             layout = widgets.Layout(flex_flow='wrap')))

    def drop_geometry(self):

        # Create interactive widgets for all arguments
        self.type_dropdown = widgets.Dropdown(
            options=['none', 'plane', 'slab', 'cylinder', 'sphere', 'wedge', 'xy', 'rz', 'xyz'],
            description="type:",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add geometry")

        # Define your function
        def on_button_click(b):
            type_value = self.type_dropdown.value

            string_input_requirement(type_value, ['none', 'plane', 'slab', 'cylinder', 'sphere', 'wedge', 'xy', 'rz', 'xyz'])

            if type_value == 'none' and self.dimension != 0:
                raise Exception("if type is none, dimension should equal zero")
            elif type_value in ['plane','slab','cylinder','sphere','wedge'] and self.dimension != 1:
                raise Exception(f"if type is {type_value} dimension should equal 1")
            elif type_value in ['xy','rz'] and self.dimension != 2:
                raise Exception(f"if type is {type_value} dimension should equal 2")
            elif type_value == 'xyz' and self.dimension != 3:
                raise Exception(f"if type is {type_value} dimension should equal 3")

            self.geometry0 = type_value

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.type_dropdown, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_geometry_nodes(self):

        # Create interactive widgets for all arguments
        self.coordinate_dropdown = widgets.Dropdown(
            options=['r', 'x', 'y', 'x'],
            description="coordinate:",
            layout=widgets.Layout(width="200px"))

        self.scaling_type_dropdown = widgets.Dropdown(
            options=['lin', 'log', 'geom', 'exp'],
            description="scaling type:",
            layout=widgets.Layout(width="200px"))

        self.nodes_input = widgets.Text(
            description="nodes (list):",
            placeholder="[node1, node2]",
            layout=widgets.Layout(width="200px"))

        self.nodes_range_input = widgets.Text(
            description="nodes range (list):",
            placeholder="[nstart, nend]",
            layout=widgets.Layout(width="200px"))

        self.ratio_input = widgets.FloatText(
            description="ratio (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.drmin_input = widgets.FloatText(
            description="drmin (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.slope_input = widgets.FloatText(
            description="slope (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add nodes")

        # Define your function
        def on_button_click(b):
            if type(self.geometry0) == type(''):
                raise Exception(f'geometry setting {self.geometry0} makes nodes call obsolete')

            coordinate_value = self.coordinate_dropdown.value
            scaling_type_value = self.scaling_type_dropdown.value
            nodes_value = eval(self.nodes_input.value)
            nodes_range_value = eval(self.nodes_range_input.value)
            ratio_value = self.ratio_input.value if self.ratio_input.value is not None else None
            drmin_value = self.drmin_input.value if self.drmin_input.value is not None else None
            slope_value = self.slope_input.value if self.slope_input.value is not None else None

            string_input_requirement(coordinate_value, ['r', 'x', 'y', 'x'])

            if coordinate_value == 'r' and self.dimension != 1:
                raise Exception("coordinate r is only compatible with 1d")

            string_input_requirement(scaling_type_value, ['lin', 'log', 'geom', 'exp'])

            self.geom_nodes = [coordinate_value, scaling_type_value, nodes_value, nodes_range_value, ratio_value, drmin_value, slope_value]

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.coordinate_dropdown, self.scaling_type_dropdown, self.nodes_input, self.nodes_range_input, self.ratio_input, self.drmin_input, self.slope_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_materials_atom(self):

        # Create interactive widgets for all arguments
        self.element_input = widgets.Text(
            description="element:",
            placeholder="H",
            layout=widgets.Layout(width="200px"))

        self.quantum_n_max_input = widgets.IntText(
            description="quantum_n_max (optional):",
            value=3,
            layout=widgets.Layout(width="200px"))

        self.iso_min_input = widgets.IntText(
            description="iso sequence min (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.iso_max_input = widgets.IntText(
            description="iso sequence max (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.index_input = widgets.IntText(
            description="index (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add atom")

        # Define your function
        def on_button_click(b):
            element_value = self.element_input.value
            quantum_n_max_value = self.quantum_n_max_input.value
            iso_min_value = self.iso_min_input.value if self.iso_min_input.value is not None else None
            iso_max_value = self.iso_max_input.value if self.iso_max_input.value is not None else None
            index_value = self.index_input.value if self.index_input.value is not None else None

            element_input_requirement(element_value)

            self.modeltype_of_atom = []
            self.atom0 = [element_value, quantum_n_max_value, iso_min_value, iso_max_value]
            self.atoms.append((self.atom0, self.modeltype_of_atom))

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.element_input, self.quantum_n_max_input, self.iso_min_input, self.iso_max_input, self.index_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_materials_atom_modeltype(self):

        # Create interactive widgets for all arguments
        self.type1_dropdown = widgets.Dropdown(
            options=['fly', 'term', 'dca', 'radonly', 'sublevel', 'johnson'],
            description="type1:",
            layout=widgets.Layout(width="200px"))

        self.type2_dropdown = widgets.Dropdown(
            options=[None,'fly', 'term', 'dca', 'radonly', 'sublevel', 'johnson'],
            description="type2: optional",
            layout=widgets.Layout(width="200px"))

        self.type3_dropdown = widgets.Dropdown(
            options=[None,'fly', 'term', 'dca', 'radonly', 'sublevel', 'johnson'],
            description="type3: optional",
            layout=widgets.Layout(width="200px"))
        
        self.type4_dropdown = widgets.Dropdown(
            options=[None,'fly', 'term', 'dca', 'radonly', 'sublevel', 'johnson'],
            description="type4: optional",
            layout=widgets.Layout(width="200px"))


        self.button = widgets.Button(description="Add screened hydrogenic modeltype", layout=widgets.Layout(width="300px"))

        # Define your function
        def on_button_click(b):
            type1_value = self.type1_dropdown.value
            type2_value = self.type2_dropdown.value
            type3_value = self.type3_dropdown.value
            type4_value = self.type4_dropdown.value

            string_input_requirement(type1_value, ['fly', 'term', 'dca', 'radonly', 'sublevel', 'johnson'])

            try:
                self.modeltype_of_atom.append([type1_value, type2_value, type3_value, type4_value])
            except:
                raise Exception('first define an atom using materials atom')

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.type1_dropdown, self.type2_dropdown, self.type3_dropdown, self.type4_dropdown, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_materials_region(self):

        # Create interactive widgets for all arguments
        self.nodes_input = widgets.Text(
            description="nodes (list):",
            placeholder="[node1, node2]",
            layout=widgets.Layout(width="200px"))

        self.elec_temp_input = widgets.FloatText(
            description="elec temp(ev):",
            value=1,
            layout=widgets.Layout(width="200px"))

        self.ion_temp_input = widgets.FloatText(
            description="ion temp(ev)(optional):",
            value=1,
            layout=widgets.Layout(width="200px"))

        self.rad_temp_input = widgets.FloatText(
            description="rad_temp(ev)(optional):",
            value=1,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add region temperature",layout=widgets.Layout(width="200px"))

        # Define your function
        def on_button_click(b):
            nodes_value = eval(self.nodes_input.value)
            elec_temp_value = self.elec_temp_input.value
            ion_temp_value = self.ion_temp_input.value if self.ion_temp_input.value is not None else None
            rad_temp_value = self.rad_temp_input.value if self.rad_temp_input.value is not None else None

            interger_input_requirement(len(nodes_value), [2, 4, 6])
            self.dimension = int(len(nodes_value) / 2)

            self.elements_of_region, self.material_of_region, self.rho_of_region = [], [], []
            self.background_of_region, self.opacity_of_region, self.level_of_region = [], [], []

            self.region0 = [self.dimension, nodes_value, elec_temp_value, ion_temp_value, rad_temp_value]
            self.regions.append((self.region0, self.elements_of_region, self.material_of_region, self.rho_of_region, self.background_of_region))

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.nodes_input, self.elec_temp_input, self.ion_temp_input, self.rad_temp_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_materials_region_rho(self):

        # Create interactive widgets for all arguments
        self.rho_input = widgets.FloatText(
            description="rho:",
            value=0.0,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Assign mass density to region")

        # Define your function
        def on_button_click(b):
            rho_value = self.rho_input.value

            self.rho_of_region.append(rho_value)

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.rho_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

    def drop_materials_region_element(self):
        # Create interactive widgets for all arguments
        self.index_input = widgets.IntText(
            description="index:",
            layout=widgets.Layout(width="200px"))

        self.initial_ion_population_input = widgets.FloatText(
            description="initial Ion Population:",
            layout=widgets.Layout(width="200px"))

        self.isoelectronic_sequence_input = widgets.Text(
            description="isoelectronic Sequence(optional):",
            placeholder="[1, 2, 3]",
            layout=widgets.Layout(width="200px"))

        self.use_lte_checkbox = widgets.Checkbox(
            value=False,
            description="use LTE",
            layout=widgets.Layout(width="200px"))

        self.electron_temp_input = widgets.FloatText(
            description="electron Temperature(optional):",
            layout=widgets.Layout(width="200px"))

        self.ion_temp_input = widgets.FloatText(
            description="ion Temperature(optional):",
            layout=widgets.Layout(width="200px"))

        self.ion_velocities_input = widgets.FloatText(
            description="ion Velocities(optional):",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add Element")

        # Define your function
        def on_button_click(b):
            index_value = self.index_input.value
            initial_ion_population_value = self.initial_ion_population_input.value
            isoelectronic_sequence_value = eval(self.isoelectronic_sequence_input.value)
            use_lte_value = self.use_lte_checkbox.value
            electron_temp_value = self.electron_temp_input.value
            ion_temp_value = self.ion_temp_input.value
            ion_velocities_value = self.ion_velocities_input.value

            element_data = [index_value, initial_ion_population_value, isoelectronic_sequence_value,
                            use_lte_value, electron_temp_value, ion_temp_value, ion_velocities_value]
            self.elements_of_region.append(element_data)

            # Clear input fields after adding the element
            self.index_input.value = None
            self.initial_ion_population_input.value = None
            self.isoelectronic_sequence_input.value = ""
            self.use_lte_checkbox.value = False
            self.electron_temp_input.value = None
            self.ion_temp_input.value = None
            self.ion_velocities_input.value = None

        self.button.on_click(on_button_click)

        # Display the widgets
        display(HBox([self.index_input, self.initial_ion_population_input, self.isoelectronic_sequence_input,
                      self.use_lte_checkbox, self.electron_temp_input, self.ion_temp_input, self.ion_velocities_input,
                      self.button],layout = widgets.Layout(flex_flow='wrap')))

    

    def drop_source_history(self):
        # Create interactive widgets for all arguments
        self.id_input = widgets.IntText(
            description="ID:",
            layout=widgets.Layout(width="200px"))

        self.value_multiplier_input = widgets.FloatText(
            description="Value Multiplier (Optional):",
            layout=widgets.Layout(width="200px"))

        self.time_multiplier_input = widgets.FloatText(
            description="Time Multiplier (Optional):",
            layout=widgets.Layout(width="200px"))

        self.pulse_type_dropdown = widgets.Dropdown(
            options=['gaussian'],
            description="Pulse Type:",
            layout=widgets.Layout(width="200px"))

        self.p1_input = widgets.FloatText(
            description="P1 (Optional):",
            layout=widgets.Layout(width="200px"))

        self.p2_input = widgets.FloatText(
            description="P2 (Optional):",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add History")

        # Define your function
        def on_button_click(b):
            id_value = self.id_input.value
            value_multiplier_value = self.value_multiplier_input.value
            time_multiplier_value = self.time_multiplier_input.value
            pulse_type_value = self.pulse_type_dropdown.value
            p1_value = self.p1_input.value
            p2_value = self.p2_input.value

            string_input_requirement(pulse_type_value, ['gaussian'])

            data = [id_value, value_multiplier_value, time_multiplier_value, pulse_type_value, p1_value, p2_value]
            self.source_histories.append(data)

            # Clear input fields after adding the history data
            self.id_input.value = None
            self.value_multiplier_input.value = None
            self.time_multiplier_input.value = None
            self.pulse_type_dropdown.value = None
            self.p1_input.value = None
            self.p2_input.value = None

        self.button.on_click(on_button_click)

        # Display the widgets
        display(widgets.HBox([self.id_input, self.value_multiplier_input, self.time_multiplier_input,
                              self.pulse_type_dropdown, self.p1_input, self.p2_input, self.button]))
    
    
    def drop_source_rswitch(self):

        # Create interactive widgets for all arguments
        self.c_is_inf_checkbox = widgets.Checkbox(
            value=None,
            description="c_is_inf",
            layout=widgets.Layout(width="200px"))

        self.assume_NLTE_checkbox = widgets.Checkbox(
            value=None,
            description="assume_NLTE",
            layout=widgets.Layout(width="200px"))

        rad_1d_dict = {'do flux-limited diffusion': 0.5, 'do transport using Feautrier formalism': -1, 'do transport using integral formalism': -2}
        rad_2d_dict = {'use iccg': 1, 'use ilur': 2}

        self.radiation_transfer_algorithm1d_dropdown = widgets.Dropdown(
            options=list(rad_1d_dict.keys()),
            description="radiation_transfer_algorithm1d:",
            layout=widgets.Layout(width="200px"))

        self.radiation_transfer_algorithm2d_dropdown = widgets.Dropdown(
            options=list(rad_2d_dict.keys()),
            description="radiation_transfer_algorithm2d:",
            layout=widgets.Layout(width="200px"))

        self.max_iter_intensities_temp_input = widgets.IntText(
            description="max_iter_intensities_temp (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        multi_group_acceleration_dict = {'no acceleration (or direct solution for 1 group)': 0,
                                         'grey acceleration': 1, 'direct multigroup acceleratio': 2,
                                         'direct solution (1-d only)': 3, 'diagonal ALI multigroup acceleration (1-d only)': 4}

        self.multi_group_acceleration_dropdown = widgets.Dropdown(
            options=list(multi_group_acceleration_dict.keys()),
            description="multi_group_acceleration:",
            layout=widgets.Layout(width="200px"))

        self.use_flux_limiting_checkbox = widgets.Checkbox(
            value=None,
            description="use_flux_limiting",
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add rswitches")

        # Define your function
        def on_button_click(b):
            c_is_inf_value = self.c_is_inf_checkbox.value
            assume_NLTE_value = self.assume_NLTE_checkbox.value
            radiation_transfer_algorithm1d_value = self.radiation_transfer_algorithm1d_dropdown.value
            radiation_transfer_algorithm2d_value = self.radiation_transfer_algorithm2d_dropdown.value
            max_iter_intensities_temp_value = self.max_iter_intensities_temp_input.value if self.max_iter_intensities_temp_input.value is not None else None
            multi_group_acceleration_value = self.multi_group_acceleration_dropdown.value if self.multi_group_acceleration_dropdown.value is not None else None
            use_flux_limiting_value = self.use_flux_limiting_checkbox.value

            string0 = 'rswitch 5 0' if c_is_inf_value else None
            string1 = 'rswitch 20 1' if assume_NLTE_value else None

            if radiation_transfer_algorithm1d_value is not None and radiation_transfer_algorithm2d_value is not None:
                raise Exception("Dimensionality incompatible")
            elif radiation_transfer_algorithm1d_value is None and radiation_transfer_algorithm2d_value is None:
                string2 = None
            elif radiation_transfer_algorithm1d_value is not None and radiation_transfer_algorithm2d_value is None:

                string2 = 'rswitch 1 ' + str(rad_1d_dict[radiation_transfer_algorithm1d_value])
            elif radiation_transfer_algorithm1d_value is None and radiation_transfer_algorithm2d_value is not None:
                string_input_requirement(radiation_transfer_algorithm2d_value, rad_2d_dict.keys())
                string2 = 'rswitch 1 ' + str(rad_2d_dict[radiation_transfer_algorithm2d_value])
            else:
                raise Exception('Error in source rswitch radiation_transfer_algorithm1')

            string2 = 'rswitch 1 ' + str(string2) if string2 is not None else None
            string3 = 'rswitch 3 ' + str(max_iter_intensities_temp_value) if max_iter_intensities_temp_value is not None else None

            if multi_group_acceleration_value is None:
                string4 = None
            else:
                string_input_requirement(multi_group_acceleration_value, multi_group_acceleration_dict.keys())
                string4 = 'rswitch 4 ' + str(multi_group_acceleration_dict[multi_group_acceleration_value])

            string5 = 'rswitch 6 1' if use_flux_limiting_value else None

            self.source_rswitch0 = [value for key, value in locals().items() if 'string' in key]

        self.button.on_click(on_button_click)

        # Display the widgets within an HBox
        display(widgets.HBox([self.c_is_inf_checkbox, self.assume_NLTE_checkbox, self.radiation_transfer_algorithm1d_dropdown, 
                              self.radiation_transfer_algorithm2d_dropdown, self.max_iter_intensities_temp_input, 
                              self.multi_group_acceleration_dropdown, self.use_flux_limiting_checkbox, self.button],layout = widgets.Layout(flex_flow='wrap')))

    def drop_popular_switches(self):

        # Create interactive widgets for all arguments
        self.include_degeneracy_dropdown = widgets.Dropdown(
            options=['include electron degeneracy', 'ignore additional correction for ionizations', 'integrate collisional ionizations numerically', 'integrate collisional excitations numerically'],
            description="include degeneracy:",
            layout=widgets.Layout(width="200px"))

        self.timestep_type_dropdown = widgets.Dropdown(
            options=['use constant timesteps', 'use_dynamic_timesteps'],
            description="timestep type:",
            layout=widgets.Layout(width="200px"))

        self.continuum_transfer_dropdown = widgets.Dropdown(
            options=['do steady-state continuum transfer', 'do time-dependent continuum transfer', 'do steady-state and use Feautrier formalism', 'do steady-state and use integral formalism formalism'],
            description="continuum transfer:",
            layout=widgets.Layout(width="200px"))

        self.continuum_transfer_evolves_temp_checkbox = widgets.Checkbox(
            value=False,
            description="continuum transfer_evolves_temp",
            layout=widgets.Layout(width="200px"))

        self.timestep_between_snapshot_input = widgets.IntText(
            description="timestep between_snapshot (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.kinematics_dropdown = widgets.Dropdown(
            options=['steady-state kinetics', 'time-dependent kinetics', 'use approx. LTE and QSS distributions to choose LTE or NLTE', 'calculate approx. LTE and QSS distribution', 'no kinetics'],
            description="kinematics:",
            layout=widgets.Layout(width="200px"))

        self.initialization_control_dropdown = widgets.Dropdown(
            options=['LTE at fixed electron density', 'LTE at fixed ion density', 'steady-state w/ radiation transfer', 'steady-state kinetics w/o radiation transfer', 'no kinetics', 'broadcast boundary radiation', 'none'],
            description="initialization control:",
            layout=widgets.Layout(width="200px"))

        self.continuum_lowering_control_dropdown = widgets.Dropdown(
            options=['approximate accounting for missing Rydberg levels', 'no continuum lowering', 'Stewart-Pyatt with formula for degeneracy lowering', 'Stewart-Pyatt with microfield degeneracy lowering', 'microfield degeneracy lowering w/o continuum lowering', 'SP/EK w/o degeneracy lowering', 'use maximum of SP/EK and approximate accounting'],
            description="continuum lowering control:",
            layout=widgets.Layout(width="200px"))

        self.raytrace_checkbox = widgets.Checkbox(
            value=False,
            description="raytrace",
            layout=widgets.Layout(width="200px"))

        self.temparture_calc_heating_rates_dropdown = widgets.Dropdown(
            options=['temp calc = none', 'temp calc = time dependant', 'temp calc = steady state'],
            description="temparture calc heating rates (list):",
            layout=widgets.Layout(width="200px"))

        self.max_iterations_per_timestep_input = widgets.IntText(
            description="max iterations per timestep (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add switches")

        # Define your function
        def on_button_click(b):
            include_degeneracy_value = self.include_degeneracy_dropdown.value
            timestep_type_value = self.timestep_type_dropdown.value
            continuum_transfer_value = self.continuum_transfer_dropdown.value
            continuum_transfer_evolves_temp_value = self.continuum_transfer_evolves_temp_checkbox.value
            timestep_between_snapshot_value = self.timestep_between_snapshot_input.value if self.timestep_between_snapshot_input.value is not None else None
            kinematics_value = self.kinematics_dropdown.value
            initialization_control_value = self.initialization_control_dropdown.value
            continuum_lowering_control_value = self.continuum_lowering_control_dropdown.value
            raytrace_value = self.raytrace_checkbox.value
            temparture_calc_heating_rates_value = self.temparture_calc_heating_rates_dropdown.value
            max_iterations_per_timestep_value = self.max_iterations_per_timestep_input.value if self.max_iterations_per_timestep_input.value is not None else None

            include_degeneracy_dict = {'include electron degeneracy': 0.5, 'ignore additional correction for ionizations': -0.5, 'integrate collisional ionizations numerically': 1.5, 'integrate collisional excitations numerically': 2.5}
            time_step_dict = {'use constant timesteps': -1, 'use_dynamic_timesteps': 1}
            continuum_transfer_dict = {'do steady-state continuum transfer': 0.5, 'do time-dependent continuum transfer': -0.5, 'do steady-state and use Feautrier formalism': 1, 'do steady-state and use integral formalism formalism': 2}
            kinematics_dict = {'steady-state kinetics': 0, 'time-dependent kinetics': 0.5, 'use approx. LTE and QSS distributions to choose LTE or NLTE': 1.5, 'calculate approx. LTE and QSS distribution': -1, 'no kinetics': -1.5}
            initialization_control_dict = {'LTE at fixed electron density': -1, 'LTE at fixed ion density': 0, 'steady-state w/ radiation transfer': 1, 'steady-state kinetics w/o radiation transfer': 2, 'no kinetics, broadcast boundary radiation': 3, 'none': 4}
            continuum_lowering_control_dict = {'approximate accounting for missing Rydberg levels': -1, 'no continuum lowering': 0, 'Stewart-Pyatt with formula for degeneracy lowering': 1, 'Stewart-Pyatt with microfield degeneracy lowering': 2, 'microfield degeneracy lowering w/o continuum lowering': 3, 'SP/EK w/o degeneracy lowering': 5, 'use maximum of SP/EK and approximate accounting': 10}
            temp_calc_dict = {'temp calc = none': 0, 'temp calc = time dependant': 1, 'temp calc = steady state': -1}

            string0 = f'switch 25 {str(kinematics_dict[kinematics_value])}' if kinematics_value else None
            string1 = f'switch 28 {str(initialization_control_dict[initialization_control_value])}' if initialization_control_value else None
            string2 = f'switch 29 {str(time_step_dict[timestep_type_value])}' if timestep_type_value else None
            string3 = f'switch 30 {str(timestep_between_snapshot_value)}' if timestep_between_snapshot_value is not None else None
            string4 = f'switch 31 {str(temp_calc_dict[temparture_calc_heating_rates_value])}' if temparture_calc_heating_rates_value else None
            string5 = f'switch 36 {str(continuum_transfer_dict[continuum_transfer_value])}' if continuum_transfer_value else None
            string6 = f'switch 44 {str(max_iterations_per_timestep_value)}' if max_iterations_per_timestep_value is not None else None
            string7 = f'switch 45 1' if raytrace_value else None
            string8 = f'switch 55 {str(continuum_lowering_control_dict[continuum_lowering_control_value])}' if continuum_lowering_control_value else None
            string9 = f'switch 100 1' if continuum_transfer_evolves_temp_value else None
            string10 = f'switch 151 {str(include_degeneracy_dict[include_degeneracy_value])}' if include_degeneracy_value else None

            data = [value for key, value in locals().items() if 'string' in key]
            self.pop_switches = data

        self.button.on_click(on_button_click)

        # Display the widgets
        display(HBox([self.include_degeneracy_dropdown, self.timestep_type_dropdown, self.continuum_transfer_dropdown, self.continuum_transfer_evolves_temp_checkbox,
                      self.timestep_between_snapshot_input, self.kinematics_dropdown, self.initialization_control_dropdown, self.continuum_lowering_control_dropdown,
                      self.raytrace_checkbox, self.temparture_calc_heating_rates_dropdown, self.max_iterations_per_timestep_input, self.button],layout = widgets.Layout(flex_flow='wrap')))


    def drop_parameters(self):

        # Create interactive widgets for all arguments
        self.scattering_muliplier_input = widgets.FloatText(
            description="scattering muliplier (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.initial_timestep_input = widgets.FloatText(
            description="initial timestep (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.minimum_timestep_input = widgets.FloatText(
            description="minimum timestep (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.maximum_timestep_input = widgets.FloatText(
            description="maximum timestep (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.time_between_snapshots_input = widgets.FloatText(
            description="time between_snapshots (optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add paramters")

        # Define your function
        def on_button_click(b):
            scattering_muliplier_value = self.scattering_muliplier_input.value if self.scattering_muliplier_input.value is not None else None
            initial_timestep_value = self.initial_timestep_input.value if self.initial_timestep_input.value is not None else None
            minimum_timestep_value = self.minimum_timestep_input.value if self.minimum_timestep_input.value is not None else None
            maximum_timestep_value = self.maximum_timestep_input.value if self.maximum_timestep_input.value is not None else None
            time_between_snapshots_value = self.time_between_snapshots_input.value if self.time_between_snapshots_input.value is not None else None

            string1 = f'param 5 {scattering_muliplier_value}' if scattering_muliplier_value else None
            string2 = f'param 41 {initial_timestep_value}' if initial_timestep_value else None
            string3 = f'param 44 {minimum_timestep_value}' if minimum_timestep_value else None
            string4 = f'param 45 {maximum_timestep_value}' if maximum_timestep_value else None
            string5 = f'param 40 {time_between_snapshots_value}' if time_between_snapshots_value else None

            self.pop_parameters = [value for key, value in locals().items() if 'string' in key]

        self.button.on_click(on_button_click)

        # Display the widgets
        display(HBox([self.scattering_muliplier_input, self.initial_timestep_input, self.minimum_timestep_input,
                      self.maximum_timestep_input, self.time_between_snapshots_input, self.button]))

    def drop_add_plot(self):

        # Create interactive widgets for all arguments
        self.name_input = widgets.Text(
            description="name (str):",
            placeholder="plot name",
            layout=widgets.Layout(width="200px"))

        self.xvar_dropdown = widgets.Dropdown(
            options=['cycle', 'iter', 'time', 'ir', 'r', 'cdens', 'x2d', 'y2d', 'z2d', 'x3d', 'y3d', 'z3d', 'xy',
                     'k', 'kx', 'ky', 'kz', 'kr', 'l', 'lx', 'ly', 'lz', 'lr', 'm', 'mx', 'my', 'mz', 'mr', 'ifr',
                     'energy', 'freq', 'wvl', 'ebins', 'fbins', 'wbins', 'ifrline', 'evline', 'isp', 'sp_energy',
                     'sp_freq', 'sp_nu', 'sp_wvl', 'iso', 'ziso', 'level', 'elev'],
            description="xvar (str):",
            layout=widgets.Layout(width="200px"))

        self.yvar_dropdown = widgets.Dropdown(
            options=['cycle', 'iter', 'time', 'ir', 'r', 'cdens', 'x2d', 'y2d', 'z2d', 'x3d', 'y3d', 'z3d', 'xy',
                     'k', 'kx', 'ky', 'kz', 'kr', 'l', 'lx', 'ly', 'lz', 'lr', 'm', 'mx', 'my', 'mz', 'mr', 'ifr',
                     'energy', 'freq', 'wvl', 'ebins', 'fbins', 'wbins', 'ifrline', 'evline', 'isp', 'sp_energy',
                     'sp_freq', 'sp_nu', 'sp_wvl', 'iso', 'ziso', 'level', 'elev'],
            description="yvar (str):",
            layout=widgets.Layout(width="200px"))

        self.element_or_transition_input = widgets.Text(
            description="element/transition (str, optional):",
            placeholder="element/transition",
            layout=widgets.Layout(width="200px"))

        self.node_input = widgets.IntText(
            description="node (int, optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.frequency_or_isosequence_input = widgets.Text(
            description="frequency/isosequence (str, optional):",
            placeholder="frequency/isosequence",
            layout=widgets.Layout(width="200px"))

        self.direction_or_level_input = widgets.Text(
            description="direction/level (str, optional):",
            placeholder="direction/level",
            layout=widgets.Layout(width="200px"))

        self.multiplier_input = widgets.FloatText(
            description="multiplier (float, optional):",
            value=None,
            layout=widgets.Layout(width="200px"))

        self.button = widgets.Button(description="Add plot")

        # Define your function
        def on_button_click(b):
            name_value = self.name_input.value
            xvar_value = self.xvar_dropdown.value
            yvar_value = self.yvar_dropdown.value
            element_or_transition_value = self.element_or_transition_input.value if self.element_or_transition_input.value else None
            node_value = self.node_input.value if self.node_input.value is not None else None
            frequency_or_isosequence_value = self.frequency_or_isosequence_input.value if self.frequency_or_isosequence_input.value else None
            direction_or_level_value = self.direction_or_level_input.value if self.direction_or_level_input.value else None
            multiplier_value = self.multiplier_input.value if self.multiplier_input.value is not None else None

            extra_indices = [element_or_transition_value, node_value, frequency_or_isosequence_value,
                             direction_or_level_value, multiplier_value]
            summ = sum(x is not None for x in extra_indices)

            if summ == 5:
                self.plots.append([name_value, xvar_value, yvar_value, element_or_transition_value, node_value,
                                   frequency_or_isosequence_value, direction_or_level_value, multiplier_value])
            elif summ == 0:
                self.plots.append([name_value, xvar_value, yvar_value])
            else:
                raise Exception('Including some of "element_or_transition, node, frequency_or_isosequence, direction_or_level, multiplier" is ambiguous and may lead to incorrect behavior in "add_plots')


            lis = [name_value, xvar_value, yvar_value, element_or_transition_value, node_value,
                    frequency_or_isosequence_value, direction_or_level_value, multiplier_value]
            lis = [x for x in lis if x is not None]
            self.plots.append(lis)

        self.button.on_click(on_button_click)

        # Display the widgets
        display(HBox([self.name_input, self.xvar_dropdown, self.yvar_dropdown, self.element_or_transition_input,
                      self.node_input, self.frequency_or_isosequence_input, self.direction_or_level_input,
                      self.multiplier_input, self.button], layout = widgets.Layout(flex_flow='wrap')))

#################################################################################################################################################

    # materials
    def materials_atom(self, element : str, quantum_n_max : int = 10, iso_min : int = None, iso_max : int= None, index : int = None):
        element_input_requirement(element)

        self.modeltype_of_atom =[]
        self.atom0 = [element, quantum_n_max, iso_min, iso_max]
        self.atoms.append((self.atom0, self.modeltype_of_atom))

    def materials_atom_modeltype(self, type1 : str, type2 : str):
        string_input_requirement(type1, ['fly','term','dca','radonly','sublevel','johnson'])
        string_input_requirement(type2, ['fly','term','dca','radonly','sublevel','johnson'])
        self.modeltype_of_atom.append([type1, type2])

    def materials_region(self, nodes :list, elec_temp : float, ion_temp : float = None, rad_temp : float = None):
        if ion_temp == None:
            ion_temp = elec_temp
        if rad_temp == None:
            rad_temp = elec_temp

        interger_input_requirement(len(nodes), [2,4,6])
        self.dimension = int(len(nodes)/2)
        
        self.elements_of_region, self.material_of_region, self.rho_of_region= [], [], []
        self.background_of_region, self.opacity_of_region, self.level_of_region  = [], [], []

        # this works retroactively, I put the material_of_region list inside the self.region, if i later change 
        # the list it gets changed while its in the self.region
        self.region0 = [self.dimension, nodes, elec_temp, ion_temp, rad_temp]
        self.regions.append((self.region0, self.elements_of_region, self.material_of_region, self.rho_of_region, self.background_of_region))

    def materials_region_rho(self, rho : float):
        self.rho_of_region.append(rho)

    def materials_region_element(self,  initial_ion_population : float, index : int = None, isoelectric_sequence : list = None,
                                  use_lte:bool = False, electron_temp : float = None, ion_temp :float = None, ion_velocities :float = None):
        self.elements_of_region.append([index, initial_ion_population, isoelectric_sequence, use_lte, electron_temp, ion_temp, ion_velocities])

    def materials_region_material(self, rho : float, atom_n : float, charge_avg : float, charge_avg_squared: float):
        self.material_of_region.append([rho, atom_n, charge_avg, charge_avg_squared])

    def materials_region_background(self, ion_density: float, electron_density: float, avg_atomic_number : float,
                                     average_charge: float, average_charge_squared : float):
        self.background_of_region.append([ion_density, electron_density, avg_atomic_number, average_charge, average_charge_squared])

    def materials_region_opacity(self, form : str , p_vals : list, e_vals : list):
        # see page 26 of documentation for exact fomulas corresponding to forms
        string_input_requirement(form, ['constant', 'power-law','exponential','gaussian','cutoff'])
        self.opacity_of_region.append([form, p_vals, e_vals])

    def materials_region_level(self, index : int, isoelectronic_sequence : int, level : int, iso_range : list = None):
        list_input_requirement([iso_range])
        self.level_of_region.append([index, isoelectronic_sequence, level, iso_range])

    def geometry(self, type : str = 'plane'):
        string_input_requirement(type, ['none', 'plane', 'slab', 'cylinder', 'sphere', 'wedge', 'xy', 'rz', 'xyz'])
        if type == 'none' and self.dimension != 0:
            raise Exception("if type is none dimension should equal zero")
        elif type in ['plane','slab','cylinder','sphere','wedge'] and self.dimension != 1:
            raise Exception(f"if type is {type} dimension should equal 1")
        elif type in ['xy','rz'] and self.dimension != 2:
            raise Exception(f"if type is {type} dimension should equal 2")
        elif type == 'xyz' and self.dimension != 3:
            raise Exception(f"if type is {type} dimension should equal 3")
        self.geometry0 = type


    def geometry_nodes(self, coordinate : str, scaling_type: str, nodes : list, nodes_range : list, ratio : float = None, drmin : float = None, slope : float = None):
        if type(self.geometry) == type(''):
            raise Exception(f'geometry setting {self.geometry} makes nodes call obsolete')
        
        string_input_requirement(coordinate, ['r','x','y','x'])
        if coordinate == 'r' and self.dimension != 1:
            raise Exception("coordinate r is only compatible with 1d")

        string_input_requirement(scaling_type, ['lin','log','geom','exp'])
        self.geom_nodes = [coordinate, scaling_type, nodes, nodes_range, ratio, drmin, slope]

    def geometry_quad(self, node_1 : list, node_2: list, x_cors : list, y_cors :list, ratios: list):
        list_input_requirement([node_1, node_2, x_cors, y_cors, ratios])
        self.geom_quad = [node_1, node_2, x_cors, y_cors]

    def geometry_product_mesh(self, product_mesh: bool = False):
        self.prod_mesh = product_mesh

    def radiation_ebins(self, n_boundaries: int, start: float, end : float, ratio : float = None):
        self.rad_ebins  = [n_boundaries, start, end, ratio]

    def radiation_angles(self, n_rays : int, n_angles : int = None):
        self.rad_angles = [n_rays, n_angles]

    def radiation_line(self, index : int, model : int, lower_state : list, higher_state : list):
        self.rad_line = [index, model, lower_state, higher_state]
        self.rad_lbins = []

    def radiation_lbins(self, n_bins : int, energy_span_1 : float, ratio_width1: float, energy_span_2 : float = None, ratio_width2: float = None):
        self.rad_lbins.append([n_bins, energy_span_1, ratio_width1, energy_span_2, ratio_width2])

    def radiation_spectrum(self, n_energies : int, energy_range : list, ratio : float):
        self.rad_spectrum = [n_energies, energy_range, ratio]

    def radiation_aprd(self, voigt_parameters : list):
        self.sources_aprd.append(voigt_parameters)
    
    def source_boundary(self, package: str, type : str, nodes : list, value : float , mult : float = None):
        string_input_requirement(package, ['radiation', 'conduction', 'hydro', 'velocity', 'pressure', 'divertor', 'current','all'])
        string_input_requirement(type, ['streaming', 'milne','value'])
        if len(nodes) not in [1,4,6]:
            raise Exception(""" the only allowed combinations are as follows:
            1) boundary package type [ir] (history id) multiplier value or
            2) boundary package type [k1 k2 l1 l2] (history id) value or
            3) boundary package type [k1 k2 l1 l2 m1 m2] (history id) value
            """)

        self.source_bound = [package, type, nodes, mult, value]

    def source_laser(self, laser_wavelength : float, option_1 : str, option_2 : str, values : list, nodes : list):
        string_input_requirement(option_1, ['value', 'rate', 'integral', 'initial'])
        string_input_requirement(option_2, ['xfile', 'history', 'profile', 'svlist','constant'])
        self.lasray_lis = []

        self.sources.append(["laser", laser_wavelength, option_1, option_2, values, nodes, self.lasray_lis])
    
    def source_jbndry(self, index : int, E_range : list, option_1 : str, option_2 : str, values : list, nodes : list = None):
        string_input_requirement(option_1, ['value', 'rate', 'integral', 'initial'])
        string_input_requirement(option_2, ['xfile', 'history', 'profile', 'svlist','constant'])

        self.lasray_lis = []
        self.sources.append(['jbndry', index, E_range, option_1, option_2, values, nodes, self.lasray_lis])

    def source_jnu(self, E_range : list, option_1 : str, option_2 : str, values : list, nodes : list):
        string_input_requirement(option_1, ['value', 'rate', 'integral', 'initial'])
        string_input_requirement(option_2, ['xfile', 'history', 'profile', 'svlist','constant'])

        self.lasray_lis = []
        self.sources.append(['jnu', E_range, option_1, option_2, values, nodes, self.lasray_lis])

    def source_lasray(self, entrance_position:float, entrance_direction_mu:float, entrance_direction_phi:float, fractional_power:float, res_frac:float = None):
        if not hasattr(self, 'lasray_lis'):
            raise Exception('lasray command must be added after laser command')
        else:
            self.lasray_lis.append([entrance_position, entrance_direction_mu, entrance_direction_phi, fractional_power, res_frac])


    def source_history(self, id: int, value_multiplier : float = None, time_multiplier : float = None, pulse_type : str = None, p1 : float = None, p2 : float = None):
        string_input_requirement(pulse_type, ['gaussian'])
        if not recursive_search(self.sources, 'history'):
            raise Exception('history command must bec attached to some earlier history input inside f.e source laser command')
        data = [id, value_multiplier, time_multiplier, pulse_type,p1, p2]
        self.source_histories.append(data)

    def source_rswitch(self, c_is_inf : bool = None, assume_NLTE : bool = None, radiation_transfer_algorithm1d : str = None, 
                       radiation_transfer_algorithm2d : str = None, max_iter_intensities_temp : int = None, 
                       multi_group_acceleration : str = None, use_flux_limiting : bool = None):
        string0 = 'rswitch 5 0' if c_is_inf == True else None
        string1 = 'rswitch 20 1' if assume_NLTE == True else None
        rad_1d_dict = {'do flux-limited diffusion':.5,'do transport using Feautrier formalism':-1,'do transport using integral formalism':-2}
        rad_2d_dict = {'use iccg':1, 'use ilur':2}

        if radiation_transfer_algorithm1d != None and radiation_transfer_algorithm2d != None:
            raise Exception("Dimensionality incompatible")
        elif radiation_transfer_algorithm1d == None and radiation_transfer_algorithm2d == None:
            string2 = None
        elif radiation_transfer_algorithm1d != None and radiation_transfer_algorithm2d == None:
            string_input_requirement(radiation_transfer_algorithm1d, rad_1d_dict.keys())
            string2 = rad_1d_dict[radiation_transfer_algorithm1d]
        elif radiation_transfer_algorithm1d == None and radiation_transfer_algorithm2d != None:
            string_input_requirement(radiation_transfer_algorithm2d, rad_2d_dict.keys())
            string2 = rad_2d_dict[radiation_transfer_algorithm2d]
        else:
            raise Exception('Error in source rswitch radiation_transfer_algorithm1')
        
        string2 = 'rswitch 1 ' + str(string2) if string2 != None else None
        string3 = 'rswitch 3 ' + str(max_iter_intensities_temp) if max_iter_intensities_temp != None else None
        multi_group_acceleration_dict = {'no acceleration (or direct solution for 1 group)':0,'grey acceleration':1,
                                         'direct multigroup acceleratio':2,'direct solution (1-d only)':3,'diagonal ALI multigroup acceleration (1-d only)':4}

        if multi_group_acceleration == None:
            string4 = None
        else:
            string_input_requirement(multi_group_acceleration, multi_group_acceleration_dict.keys())
            string4 =  'rswitch 4 ' + str(multi_group_acceleration_dict[multi_group_acceleration])
                    
        string5 = 'rswitch 6 1' if use_flux_limiting == True else None

        self.source_rswitch0 = [value for key, value in locals().items() if 'string' in key]

    def controls(self, t_start : float, t_end : float, restart : bool = False, edits : bool = False):
        self.control = [t_start, t_end, restart, edits]

    def controls_history(self, id : int, value_mutiplier : float, time_multiplier, type : list = None):
        self.controls_hist = [id, value_mutiplier, time_multiplier, type]
        self.tv = []

    def controls_history_tv(self, time : float, value : float):
        self.tv.append([time, value])

    def popular_switches(self, include_degeneracy : str = None, timestep_type : str = None, continuum_transfer : str = None,
                          continuum_transfer_evolves_temp : bool = False, timestep_between_snapshot : int = None, 
                          kinematics : str = None, initialization_control : str = None, continuum_lowering_control  : str = None,
                          raytrace : bool = None, temparture_calc_heating_rates : list = None, max_iterations_per_timestep : float = None):
        
        # using the gather_data.ipynb file i've searched for the most common switches 
        if include_degeneracy == None:
            string0 = None
        else:
            include_degeneracy_dict = {'include electron degeneracy' : .5,' ignore additional correction for ionizations' : -.5,
                                       'integrate collisional ionizations numerically': 1.5,'integrate collisional excitations numerically': 2.5}
            string_input_requirement(include_degeneracy, include_degeneracy_dict.keys())
            string0 = f'switch 151 {str(include_degeneracy_dict[include_degeneracy])}'

        if timestep_type == None:
            string1 = None
        else:
            time_step_dict = {'use constant timesteps' : -1, 'use_dynamic_timesteps' : 1}
            string_input_requirement(timestep_type, time_step_dict.keys())   
            string1 = f'switch 29 {str(time_step_dict[timestep_type])}'

        if continuum_transfer == None:
            string2 = None
        else:
            continuum_transfer_dict = {'do steady-state continuum transfer': .5, 'do time-dependent continuum transfer':-.5, 'do steady-state and use Feautrier formalism': 1, 'do steady-state and use integral formalism formalism':2}
            string_input_requirement(continuum_transfer, continuum_transfer_dict.keys())   
            string2 = f'switch 36 {str(continuum_transfer_dict[continuum_transfer])}'

        string3 =  'switch 100 1' if continuum_transfer_evolves_temp == True else None
        string4 = None if timestep_between_snapshot == None else f'switch 30 {str(timestep_between_snapshot)}'

        if kinematics == None:
            string5 = None
        else:
            kinematics_dict = {'steady-state kinetics': 0, 'time-dependent kinetics':.5, 'use approx. LTE and QSS distributions to choose LTE or NLTE': 1.5, 'calculate approx. LTE and QSS distribution': -1, 'no kinetics':-1.5}
            string_input_requirement(kinematics, kinematics_dict.keys())   
            string5 = f'switch 25  {str(kinematics_dict[kinematics])}'

        if initialization_control == None:
            string6 = None
        else:
            initialization_control_dict = {'LTE at fixed electron density':-1,' LTE at fixed ion density':0,'steady-state w/ radiation transfer':1,
                                           'steady-state kinetics w/o radiation transfer':2,': no kinetics, broadcast boundary radiation':3, 'none':4}
            string_input_requirement(initialization_control, initialization_control_dict.keys())
            string6 = f'switch 28 {str(initialization_control_dict[initialization_control])}' if initialization_control != None else None
        
        if continuum_lowering_control == None:
            string7 = None
        else:
            continuum_lowering_control_dict = {'approximate accounting for missing Rydberg levels':-1,' no continuum lowering':0,'Stewart-Pyatt with formula for degeneracy lowering':1,
                                      'Stewart-Pyatt with microfield degeneracy lowering':2,'microfield degeneracy lowering w/o continuum lowering':3,
                                      'SP/EK w/o degeneracy lowering':5,' use maximum of SP/EK and approximate accounting':10}

            string7 = f'switch 55 {str(continuum_lowering_control_dict[continuum_lowering_control])}' if continuum_lowering_control != None else None

        if continuum_lowering_control == None:
            string7 = None
        else:
            continuum_lowering_control_dict = {'approximate accounting for missing Rydberg levels':-1,' no continuum lowering':0,'Stewart-Pyatt with formula for degeneracy lowering':1,
                                      'Stewart-Pyatt with microfield degeneracy lowering':2,'microfield degeneracy lowering w/o continuum lowering':3,
                                      'SP/EK w/o degeneracy lowering':5,' use maximum of SP/EK and approximate accounting':10}

            string7 = f'switch 55 {str(continuum_lowering_control_dict[continuum_lowering_control])}' if continuum_lowering_control != None else None
        
        if raytrace == None or raytrace == False:
            string8 = None
        else:
            string8 = 'switch 45 1'

        if temparture_calc_heating_rates == None:
            string9 = None
        else:
            temp1, heat1 = temparture_calc_heating_rates[0], temparture_calc_heating_rates[1]
            temp_calc_dict = {'temp calc = none' : 0,'temp calc = time dependant' : 1,' temp calc = steady state' : -1}

            heating_type_dict = {'heating rates = electronic' : 1,' heating rate uses internal energy rates':2,
                              'heating rate uses interal energy deltas':3}
            
            string_input_requirement(temp1, temp_calc_dict.keys())
            string_input_requirement(heat1, heating_type_dict.keys())

            sol = temp_calc_dict[temp1]*heating_type_dict[heat1]
            string9 = f'switch 31 {sol}'


        if max_iterations_per_timestep == None:
            string10 = None
        else:
            string10 = f'switch 44 {max_iterations_per_timestep}'
            
        self.pop_switches = [value for key, value in locals().items() if 'string' in key]


    def other_switches(self, population_calculation: str  = None, subcycle_maximum : int = None, do_kinetics_zone_centerd : bool = None, 
                       resonant_absrption_fraction: str = None, control_calc_thermal_conduct: str = None):
        #switches   2,3,10,49,47

        pop_cal_dict = {'assuming steady state diffusion': 0, 'time dependent diffusion': 1}
        string0 = switch_format(population_calculation, pop_cal_dict, 2)

        if subcycle_maximum == None:
            string1 = None
        else:
            string1 = f'switch 3 {subcycle_maximum}' 


        if do_kinetics_zone_centerd == None:
            string2 = f'switch 10 0' 
        else:
            string2 = f'switch 10 1' 

        resonant_absrption_fraction_dict = {'constant value for each ray from lasray': 0, 
                                            'Ginzburg formula': 1,
                                            'Ginzburg formula + smooth resonant absorption over neighboring zones':-1,
                                            'tabulated values': .5,
                                            'tabulated values + smooth resonant absorption over neighboring zones':-.5}
        string3 = switch_format(population_calculation, resonant_absrption_fraction_dict, 47)
        thermal_conduction_dict = {
            'no thermal conduction': 0,
            'include thermal conduction': 1,
            'use iccg': 2,
            'use ilur': 3,
            'use gmres with diagonal preconditioning': 4,
            'use gmres with iccg preconditioning': 5,
            'use gmres with ilur preconditioning': 6,
            'use gmres with no preconditioning': 7
        }
        string4 = switch_format(control_calc_thermal_conduct, thermal_conduction_dict, 49)

        self.ot_switches = [value for key, value in locals().items() if 'string' in key]


    def parameters(self, scattering_muliplier : float = None, initial_timestep : float = None, minimum_timestep : float = None, maximum_timestep : float = None, time_between_snapshots : float = None):
        if scattering_muliplier == None:
            string1 = None
        else:
            string1 = f'param 5 {scattering_muliplier}'

        if initial_timestep == None:
            string2 = None
        else:
            string2 = f'param 41 {initial_timestep}'

        if minimum_timestep == None:
            string3 = None
        else:
            string3 = f'param 44 {minimum_timestep}'

        if maximum_timestep == None:
            string4 = None
        else:
            string4 = f'param 45 {maximum_timestep}'

        if time_between_snapshots == None:
            string5 = None
        else:
            string5 = f'param 40 {time_between_snapshots}'               
        
            
        self.pop_parameters = [value for key, value in locals().items() if 'string' in key]

    def add_plot(self, name:str, xvar:str, yvar:str, element_or_transition:str = None, node: int = None,
                  frequency_or_isosequence : str = None, direction_or_level: str = None, multiplier : float = None):
        extra_indices = [element_or_transition, node, frequency_or_isosequence, direction_or_level, multiplier]
        summ = sum(x is None for x in extra_indices)

        vars = """cycle,iter,time
        ir,r,cdens,x2d,y2d,z2d,x3d,y3d,z3d,xy,k,kx,ky,kz,kr,l,lx,ly,lz,lr,m,mx,my,mz,mr
        ifr,energy,freq,wvl,ebins,fbins,wbins,ifrline,evline,isp,sp_energy,sp_freq,sp_nu,sp_wvl,iso,ziso
        level,elev"""
        #string_input_requirement(xvar,vars.split(","))
        #string_input_requirement(yvar,vars.split(","))

        if summ == 5:
            self.plots.append([name, xvar, yvar, element_or_transition, node, frequency_or_isosequence, direction_or_level, multiplier])
        elif summ == 0:
            self.plots.append([name, xvar, yvar])
        else:
            raise Exception('Including some of "element_or_transition, node, frequency_or_isosequence, direction_or_level, multiplier" is ambiguous and may lead to incorrect behavior in "add_plots')
        lis = [name, xvar, yvar, element_or_transition, node, frequency_or_isosequence, direction_or_level, multiplier]
        lis.remove(None)
        self.plots.append(lis)

#################################################################################################################################################

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
        df = pd.read_csv(f'{paths.to_folder_cretin()}periodic_table.csv')
        element_list = df['Symbol'].to_string(index = False)

    new = []
    for entry in element_list:
        entry = ''.join(entry.split())
        entry = entry.upper()
        new.append(entry)

    element_list = new
    element = element.upper()
    if element not in element_list: 
        #raise Exception('must be one of H, HE, LI, BE ...')
        pass

def interger_input_requirement(inter : int, options : list):
    if inter not in options:
        fstrin = f'{inter} is not one of: {options}'
        raise Exception(fstrin)
    

def recursive_search(item, target):
    if isinstance(item, list):
        for sub_item in item:
            if recursive_search(sub_item, target):
                return True
    elif item == target:
        return True
    return False

def switch_format(entry, dict, switch_nr):
    if entry == None:
        return None
    else:
        string_input_requirement(entry, dict.keys())
        return f'switch {switch_nr} {dict[entry]})'
                
