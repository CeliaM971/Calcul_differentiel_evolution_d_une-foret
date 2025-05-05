import functools
from modls.autonomous_sys import AutonomSys

class LotkaVolterra(AutonomSys) :

    def __init__(self,epsi,kapp,title):
        super().__init__(title)
        self._epsilon = epsi
        self._kappa = kapp

    def __str__(self):
        msg = " Lotka Volterra 1 : epsilon = {} kappa = {} (titre : {})"
        msg = msg.format(self.get_epsilon() , self.get_kappa(), self.get_title() )
        return msg

    # --
    # -- Public Methods
    def get_rhs(self):
        return functools.partial(self._rhs)

    def get_field(self,x,y):
        epsilon = self.get_epsilon()
        kappa = self.get_kappa()

        f = x * (( x - epsilon ) * (1. - (1./ kappa ) * x ) / ( x + epsilon ) - y )
        g = y * ( x - 1)
        return [f,g]

    # --
    # -- Public getters
    
    def get_epsilon(self):
        return self._epsilon
        
    def get_kappa(self):
        return self._kappa
        
    def get_title(self):
        return self._title

    # --
    # -- Public setters
    
    def set_epsilon(self,value):
        self._epsilon = value
        
    def set_kappa(self,value):
        self._kappa = value
        
    def set_title(self,value):
        self._title = value

    # --
    # -- Private Methods
    def _rhs( self , z , t ) :
        epsilon = self.get_epsilon()
        kappa = self.get_kappa()

        x = z[0]
        y = z[1]
        dxdt = x * (( x - epsilon ) * (1. - (1./ kappa ) * x ) / ( x + epsilon ) - y )
        dydt = y * ( x - 1)
        return [dxdt,dydt]
