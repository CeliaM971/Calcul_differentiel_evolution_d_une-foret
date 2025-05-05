class Axis:

    def __init__(self, start, end, size_subdiv,label):
        self._start = start
        self._end = end
        self._size_subdiv = size_subdiv
        self._label = label
        
    def __str__(self):
        msg = " Axes : start = {} end = {} nombre_subdivisions = {} label = {}"
        msg = msg.format(self.get_start() , self.get_end() , self.get_size_subdiv,self.get_label() )
    
    def get_start(self):
        return self._start
        
    def set_start(self,value):
        self._start = value
        
    def get_end(self):
        return self._end
    
    def set_end(self,value):
        self._end = value
    
    def get_size_subdiv(self):
        return self._size_subdiv
    
    def set_size_subdiv(self,value):
        self._size_subdiv = value
        
    def get_label(self):
        return self._label
    
    def set_label(self,value):
        self._label = value
    


