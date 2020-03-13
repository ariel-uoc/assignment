class salad():
    
    def __init__(self):
        self.path = ''
        self.items = []
        self.numbes = []
    
    # should receive a path
    # should receive a list of salad items
    # should receive a list of number of salad items
    # should write a file with item_00.salad
    
    # input path, [tomato, lettuce], [2,3]
    # xxx/tomato_00.salad
    # xxx/tomato_01.salad
    # xxx/lettuce_00.salad
    # xxx/lettuce_01.salad
    # xxx/lettuce_02.salad 
    def write(self, path, salad, n_items):
        self.path = path
        print(self.path)
        
        assert len(salad) == len(n_items), "Length of items and numbers should be equal."
        os.makedirs(self.path, exist_ok=True)
        
        for k in range(len(salad)):
            print(salad[k], n_items[k])
            for j in range(n_items[k]):
                file_name = salad[k]+'{:0>2}'.format(j)+'.salad'
                print(os.path.join(self.path, file_name))
                f = open(os.path.join(self.path, file_name), 'w')
                f.close()

   
    # read the .salad files
    # return a dictionary with salad items and how many there are
    def read(self, path):
        flist = glob.glob(os.path.join(path, '*.salad'))
        a = []
        for file in flist:
            pattern = r'(\w+)(\d\d)'
            a.append(re.findall(pattern, file))
        
        a_list = list(chain(*a))
        
        # create a dictionary
        dct = {}

        for i in a_list:
            if i[0] in list(dct.keys()):
                dct[i[0]] += 1
            else:
                dct[i[0]] = 1
        
        return flist, dct
        
        