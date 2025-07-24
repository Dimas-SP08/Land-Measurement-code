class Survey_CTRL:
    '''Controler to manage survey workflow'''

    def __init__(self):
        
        '''Initialize the controler'''
        self.ascii=97 # 'a' in ASCII
        self.data = []
        self.point_group_index=1

    def set_initial(self,amsl,point):
        '''Set initial survey parameters'''
        self.amsl= amsl
        self.point = point

    def add_point(self):
        '''Generate labels for points'''
        label1 = f'P{self.point_group_index}-{chr(self.ascii)}'
        label2 = f'P{self.point_group_index}-{chr(self.ascii + 1)}'
        label  = f'{label1} → {label2}'
        return label,label1,label2


    def calculate_mid_thread(self,top_thread,mid_thread,bottom_thread):
        '''Calculate mid thread from top and bottom thread'''
        if top_thread != 0 and bottom_thread != 0:                       
            result_mid_thread = (top_thread + bottom_thread) / 2
            return result_mid_thread
        else:
            return mid_thread

        
    def get_table(self):
        '''Convert all survey points to a list of dicts'''
        return [pt.to_dict() for pt in self.data]