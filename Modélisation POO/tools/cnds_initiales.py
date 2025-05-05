class Initial:
    
    def __init__(self, coords, line_style):
        self._coords = coords  
        self._params = {
            "color": line_style.get_color(),
            "form": line_style.get_form()
        }

    # -- Public getters
    def get_coords(self):
        return self._coords

    def get_color(self):
        return self._params["color"]

   # -- Public setters
    def set_color(self, color):
        self._params["color"] = color

    def set_form(self, form):
        self._params["form"] = form
        
    def get_form(self):
        return self._params["form"]

    def get_style(self):
        return f"{self.get_color()}{self.get_form()}"


class Initials:
    
    def __init__(self):
        self._initials = []  # Liste d'objets Initial

    # -- Méthodes d'accès --
    def get_cnds(self):  
        return self._initials

    def get_coords_list(self):
        return [init.get_coords() for init in self._initials]
        
    # -- Public setters   
    
    def set_initials(self, new_initials):
        if all(isinstance(item, Initial) for item in new_initials):
            self._initials = new_initials
        else:
            raise TypeError("Tous les éléments doivent être des instances de Initial")
        
    def append(self, coords, line_style):
        """Ajoute une nouvelle condition initiale"""
        new_initial = Initial(coords, line_style)
        self._initials.append(new_initial)

    def generate_from_lists(self, x_list, y_list, line_style):
        """Générer des conditions initiales à partir de la donnée des listes des coordonnées et du style de la trajectoire"""
        for x in x_list:
            for y in y_list:
                self.append((x, y), line_style)

