class Survey_Point:
    '''represents a single survey point with elevation calculation and status'''
    
    def __init__(self,label,backsight,foresight,distance,initial_elev):
        '''Create a survey point'''

        self.__label = label
        self.__distance = distance
        self.__backsight = backsight
        self.__foresight = foresight

        heightdiffer = backsight - foresight
        initial_elev += heightdiffer
        stats = self.predict_status(heightdiffer)

        self.__heightdiff =  heightdiffer
        self.__elevation = initial_elev
        self.__status = stats

    def predict_status(self,hegithdiffer):
        '''Decide if the point is RISE, FALL, or FLAT'''
        if hegithdiffer > 0:
            return "RISE"
        elif hegithdiffer < 0:
            return "FALL"
        else:
            return "FLAT"

    def to_dict(self):
        '''Convert point data to a dict for tables''' 
        return {
            "POINT NUMBER":self.__label,
            "BACKSIGHT":self.__backsight,
            "FORESIGHT":self.__foresight,
            "DISTANCE (m)":self.__distance,
            "HEIGHT DIFFERENCE":self.__heightdiff,
            "ELEVATION (AMSL)":self.__elevation,
            "STATUS":self.__status
        }
        
    '''property'''
    @property
    def elevation(self):
        return self.__elevation 
    @property
    def label(self):
        return self.__label 
    @property
    def heightdiff(self):
        return self.__heightdiff
    @property
    def status(self):
        return self.__status 