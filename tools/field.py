import numpy as np
import pylab as pl
from tools.line_style_form import Color

class Field :

    def __init__( self , col = Color() ):
        self._params = { "color":col.green() }

    # -
    # -- Public getters
    
    def get_color(self):
        return self._params["color"] 

    # -- Public setters
    
    def set_params(self,value):
        self._params = value

    # --
    # -- Public Methods
    def plot( self , modl , xaxis , yaxis ):
        xstr = xaxis.get_start()
        xend = xaxis.get_end()   
        xmsh = xaxis.get_size_subdiv()  

        ystr = yaxis.get_start()  
        yend = yaxis.get_end()    
        ymsh = yaxis.get_size_subdiv() 
    
        xgrid , ygrid = np.mgrid[xstr:xend:xmsh , ystr:yend:ymsh]
        xfield , yfield = modl.get_field(xgrid,ygrid)
        col_field = self.get_color()
        return pl.quiver(xgrid,ygrid,xfield,yfield,color = col_field)
        
   
