class AutonomSys:
    
    def __init__(self, title):
        self._title = title
    
    def __str__(self):
        return f"Système autonome: {self._title}"
    
    def get_title(self):
        return self._title
        
    def set_title(self, value):
        self._title = value
        
    # -- Méthodes à implémenter par les classes filles --
    def get_rhs(self):
        """Retourne le second membre du système"""
        raise NotImplementedError("Méthode abstraite")
        
    def get_field(self, x, y):
        """Retourne le champ de vecteurs"""
        raise NotImplementedError("Méthode abstraite")


