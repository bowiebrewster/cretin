# this file turns the creting generator object into a .gen file 

class Text_generator():
    def __init__(self, user_input):
        self.user_input = user_input
        self.dict = self.user_input.__dict__.keys()

    # generates a "chapter" string in the generator file
    def start_chapter(self, name : str):
        deliniator = 'c ------------------------------------------------------------'
        header = f'\n{deliniator} \nc   {name}\n{deliniator}\n'
        return header
    
    # int list to string
    def ilts(self, lis:list):
        return_lis = []
        for x in lis:
            if x != None:
                if type(x) == type([]):
                    x = x[0]
                return_lis.append(str(x))
        return ' '.join(return_lis)
    
    #flatten
    def flat(self, lis:list):
        return [item for sublist in lis for item in sublist]
    
    def materials(self):
        string = self.start_chapter('Materials')

        atoms = self.user_input.atoms
        regions = self.user_input.regions

        # materials_atom
        for atom in atoms:
            atom0, modeltpye = atom
            if atom0[2] == None:
                atom0[2] == ''
            line = f'atoms hydrogenic_{atom0[1]} {atom0[0]} \n'
            string += line

        for region in regions:
            region0, element_of_region, material_of_region, rho_of_region, background_of_region = region
            strings0 = ['region','regionkl','regionklm']
            string += f'\n{strings0[region0[0]-1]} {self.ilts(region0[1])} {self.ilts(region0[2:])}'

            for el in element_of_region:
                string += f'\n\telement {self.ilts(el)}'

            for mat in material_of_region:
                string += f'\n\tmaterial {self.ilts(mat)}'

            for rho in rho_of_region:
                string += f'\n\trho {str(rho_of_region[0])}'

            for bac in background_of_region:
                string += f'\n\tbackground {self.ilts(background_of_region[0])}'
        return string

    def geometry(self):
        string = self.start_chapter('Geometry')
        if 'geometry0' in self.dict:
            string +='\n geometry ' + str(self.user_input.geometry0)

        if 'geom_nodes' in self.dict:
            nodes = self.user_input.geom_nodes
            nodes0 = nodes[0] + nodes[1]+ f" {self.ilts(nodes[2])} {self.ilts(nodes[3])} "


            string +='\n ' + nodes0
            for val in nodes[4:-1]:
                if val != None:
                    string += f"{val} "
        
        if 'geom_quad' in self.dict:
            quad = self.flat(self.user_input.geom_quad)
            string +='\n quad ' + self.ilts(quad)

        return string

    def radiation(self):
        string = self.start_chapter('Radiation')
        if 'rad_line' in self.dict:
            rad_lin = self.user_input.rad_line

            string += f'line {self.ilts(rad_lin[0:2])} {self.ilts(rad_lin[2])} {self.ilts(rad_lin[3])}'
        
            if 'rad_lbins' in self.dict:
                lbins = self.user_input.rad_lbins
                string += '\n\tlbins ' + self.ilts(lbins[0])

        if 'rad_ebins' in self.dict:
            ebins = self.user_input.rad_ebins
            string += '\nebins ' + self.ilts(ebins)

        if 'rad_angles' in self.dict:
            angles = self.user_input.rad_angles
            string += '\nangles ' + self.ilts(angles)

        return string
    
    def sources(self):
        if 'sources' not in self.dict:
            return ''

        string = self.start_chapter('Sources')
        sources = self.user_input.sources
        for source in sources:
            if source[0] == 'laser':
                string += f'source {source[0]} {source[1]}x {source[2]} {source[3]} {self.ilts(source[4])} {self.ilts(source[-1])}'
            elif source[0]== 'jbndry':
                string += f'source {source[0]} {source[1]} {self.ilts(source[2])} {source[3]} {source[4]} {self.ilts(source[-2])} {self.ilts(source[-1])}'
            elif source[0]== 'jnu':
                string += f'source {source[0]} {self.ilts(source[1])} {source[2]} {source[3]} {self.ilts(source[-1])}'
            else:
                raise Exception("Source must be type 'jbndry', 'jnu' or 'laser' ")
            
            string += '\n'

        return string 
    
    def controls(self):
        if 'control' not in self.dict:
            return ""
        control = self.user_input.control
        string = self.start_chapter('Controls')
        string += '\ntstart '+str(control[0])
        string += '\ntquit '+str(control[1])
        if control[2]:
            string += '\n\nrestart '
        if control[3]:
            string += '\n edits'
        string += '\n\ndump all'

        return string
    
    def pop_switches(self):
        if 'pop_switches' not in self.dict:
            return ''
        pop = self.user_input.pop_switches
        string = self.start_chapter('Switches')
        for string0 in pop:
            if string0 != None:
                string += '\n '+string0
        return string
    
    def execute(self):
        output = ''
        for func in [self.materials, self.geometry, self.radiation, self.sources, self.controls, self.pop_switches]:
            output += func()+'\n'
        return output