import functools
from modls.autonomous_sys import AutonomSys

class Projetforet(AutonomSys) :

    def __init__(self,delta,a,b,c,m,title):
        super().__init__(title)
        self._delta = delta
        self._a = a
        self._b = b
        self._c = c
        self._m = m

    def __str__(self):
        msg = " Lotka Volterra 1 : delta = {} a = {}  b = {} c = {} m = {} (titre : {})"
        msg = msg.format(self.get_delta() , self.get_a(), self.get_b(), self.get_c(), self.get_m(), self.get_title() )
        return msg

    # --
    # -- Public Methods
    def get_rhs(self):
        return functools.partial(self._rhs)


    def get_field(self,x,y):
        delta = self.get_delta()
        a = self.get_a()
        b = self.get_b()
        c = self.get_c()
        m = self.get_m()
        
        # x = h et y = f dans notre sujet
        f = -((a*x*y)/(b+c*x+x**2)) + (1-delta)*m*y
        g = ((a*x*y)/(b+c*x+x**2)) - m*y
        return [f,g]

    # --
    # -- Public getters
    
    def get_delta(self):
        return self._delta
        
    def get_a(self):
        return self._a
        
    def get_b(self):
        return self._b
        
    def get_c(self):
        return self._c
        
    def get_m(self):
        return self._m
        
    def get_title(self):
        return self._title

    # --
    # -- Public setters
    
    def set_delta(self,value):
        self._delta = value
        
    def set_a(self,value):
        self._a = value
        
    def set_b(self,value):
        self._b = value
        
    def set_c(self,value):
        self._c = value
        
    def set_m(self,value):
        self._m = value
        
    def set_title(self,value):
        self._title = value

    # --
    # -- Private Methods
    def _rhs( self , z , t ) :
        delta = self.get_delta()
        a = self.get_a()
        b = self.get_b()
        c = self.get_c()
        m = self.get_m()

        x = z[0]
        y = z[1]
        dxdt = -((a*x*y)/(b+c*x+x**2)) + (1-delta)*m*y
        dydt = ((a*x*y)/(b+c*x+x**2)) - m*y
        return [dxdt,dydt]
