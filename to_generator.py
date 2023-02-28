class Text_generator():
    def __init__(self, user_input):
        self.user_input = user_input
        self.dict = self.user_input.__dict__.keys()

    def start_chapter(self, name : str):
        deliniator = 'c ------------------------------------------------------------'
        header = deliniator +'\nc   '+name+'\n'+deliniator+'\n'
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
        return [item for sublist in self.user_input.geom_quad for item in sublist]
    
    def materials(self):
        string = self.start_chapter('Materials')

        atoms = self.user_input.atoms
        regions = self.user_input.regions

        # materials_atom
        for atom in atoms:
            line = f'atoms hydrogenic_{atom[2]} {atom[1]} \n'
            string += line

        for region in regions:
            region0, element_of_region, material_of_region, rho_of_region, background_of_region = region
            strings0 = ['region','regionkl','regionklm']
            string += '\n'+strings0[region0[0]-1] + ' '+ self.ilts(region0[1]) + ' '+ self.ilts(region0[2:])

            for el in element_of_region:
                string += '\n\t' + 'element ' + self.ilts(el)

            for mat in material_of_region:
                string += '\n\t' + 'material ' + self.ilts(mat)

            for rho in rho_of_region:
                string += '\n\t' + 'rho ' + str(rho_of_region[0])

            for bac in background_of_region:
                string += '\n\t' + 'background ' + self.ilts(background_of_region[0])
            
        return string

    def geometry(self):
        string = self.start_chapter('Geometry')
        string +='\n geometry ' + str(self.user_input.geometry)

        nodes = self.user_input.geom_nodes[0]
        nodes = [nodes[0] + nodes[1]] + nodes[2:-1]
        string +='\n ' + self.ilts(nodes)
        quad = self.flat(self.user_input.geom_quad)
        string +='\n quad ' + self.ilts(quad)

        return string

    def radiation(self):
        string = self.start_chapter('Radiation')
        if 'rad_ebins' in self.dict:
            ebins = self.user_input.rad_ebins
            string += '\n ebins ' + self.ilts(ebins)
        if 'rad_lbins' in self.dict:
            lbins = self.user_input.rad_lbins
            string += '\n lbins ' + self.ilts(lbins)
        if 'rad_angles' in self.dict:
            angles = self.user_input.rad_angles
            string += '\n angles ' + self.ilts(angles)

        return string
    
    def sources(self):
        if 'sources' in self.dict:
            string = self.start_chapter('Sources')
            sources = self.user_input.sources
            for source in sources:
                if source[0] == 'laser':
                    string += '\n source laser ' + str(source[1]) + 'x ' + self.ilts(self.flat(source[2:-1]))
                else:
                    string +=  '\n ' + self.ilts(source)

        return string 
    
    def controls(self):
        control = self.user_input.control
        string = self.start_chapter('Controls')
        string += '\nt_start '+str(control[0])
        string += '\nt_end '+str(control[1])
        if control[2]:
            string += '\n\nrestart '
        if control[3]:
            string += '\n edits'
        return string
    
    def pop_switches(self):
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