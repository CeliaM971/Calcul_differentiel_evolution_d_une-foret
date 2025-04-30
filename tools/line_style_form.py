class Color:
    
    def __init__(self) :
        self._colors = { "blue" : "b" ,
                          "red" : "r" ,
                          "black" : "k" ,
                          "cyan" : "c" ,
                          "green" : "g" ,
                          "magenta" : "m" ,
                          "yellow" : "y" }

    # --
    # -- Public getters
    def blue(self):
        return self._colors["blue"]

    def red(self):
        return self._colors["red"]
    
    def black(self):
        return self._colors["black"]
        
    def cyan(self):
        return self._colors["cyan"]
        
    def green(self):
        return self._colors["green"]
        
    def magenta(self):
        return self._colors["magenta"]
        
    def yellow(self):
        return self._colors["yellow"]
        

class Form:
    def __init__(self):
        self._form = {
            "solid": "-",
            "dashed": "--", 
            "dotted": ":",
            "dashdot": "-."
        }
    
    def solid(self):
        return self._form["solid"]
    
    def dashed(self):
        return self._form["dashed"]
    
    def dotted(self):
        return self._form["dotted"]
    
    def dashdot(self):
        return self._form["dashdot"]
        

        
class LineStyle:
    
    def __init__(self, color,form):
        self._color = color
        self._form = form
        
    def __str__(self):
        msg = "Style de lignes : couleur = {} forme = {} = "
        msg = msg.format(self.get_color() , self.get_form())
        return msg
    
    def get_color(self):
        return self._color
    
    def set_color(self,value):
        self._color = value
        
    def get_form(self):
        return self._form
    
    def set_form(self,value):
        self._form = value
        
    def style_ligne(self):
        return self.get_color() + self.get_form()
   
