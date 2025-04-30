import numpy as np
import matplotlib . pyplot as plt
from scipy.integrate import odeint

from tools.field import Field

class PhaseDiag:
    
    def __init__(self,title = " Portrait des phases " , figsize =(10 , 6) ):
        self._title = title
        self._figsize = figsize

    def __str__( self ):
        return self._title

    # -- Public getters
    
    def get_title(self):
        return self._title
        
    def get_figsize(self):
        return self._figsize

    # -- Public setters
    
    def set_title(self,value):
        self._title = value
        
    def set_figsize(self,value):
        self._figsize = value

    # -- Public methods
    def portrait(self , modl , cndszr , xaxis , yaxis , taxis , exprtpng = False , showfield = True ):

        # -- Preparer graphique
        fig , phases = plt.subplots(figsize = self.get_figsize())

        # -- Parametrage graphique globaux
        plt.xlim( xaxis.get_start() , xaxis.get_end() )
        plt.ylim( yaxis.get_start() , yaxis.get_end() )

        # -- Parametrage repere
        phases.grid( True )
        phases.set_title( self.get_title() )
        phases.set( xlabel = xaxis.get_label() , ylabel = yaxis.get_label() )

        # -- Calcul des trajectoires
        tdisc = np.linspace( taxis.get_start() , taxis.get_end() , taxis.get_size_subdiv() )

        cndszero = cndszr.get_cnds()
        for cnd in cndszero :
            cnd0 = cnd.get_coords()
            trj = odeint( modl.get_rhs() , cnd0 , tdisc )
            phases.plot( trj[:,0],trj[:,1],cnd.get_style() )

        # -- Champ des gradients
        if showfield :
            field = Field()
            field.plot( modl , xaxis , yaxis )

        plt.show(block=True)

        if exprtpng :
            figname = self.get_title() + ".png"
            figname = figname.replace( "" , "_" )
            fig.savefig( figname )
