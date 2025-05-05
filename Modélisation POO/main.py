# --
# -- Hacene Ouzia , Sorbonne Universite
# -- Copyright ( c ) 2020.

from tools.axis import Axis
from tools.cnds_initiales import Initials
from tools.line_style_form import LineStyle , Color , Form
from tools.phase_diag import PhaseDiag
from modls.projet_foret import Projetforet


def main() :
	# --
	# -- Le modele
	delta , a , b , c , m = 0., 0.031 , 8*(10**(-6)), 1.13, 0.027
	mdl_foret = Projetforet( delta , a , b, c, m, " Système projet forêt " )

	# --
	# -- Les axes
	xaxis = Axis(0. , 0.05 , 15j, "x")
	yaxis = Axis( 0, 0.03 , 15j, "y" )
	taxis = Axis(0 , 20000 ,1000000, "t")

	# --
	# -- Couleurs et formes
	col = Color()
	frm = Form()
	red_solid = LineStyle( col.red(), frm.solid() )
	ble_dhdot = LineStyle( col.blue() , frm.dashdot() )

	# --
	# -- Conditions initiales
	cnds = Initials()
	cnds.append((0.018,0.01),ble_dhdot )
	cnds.append((0.017,0.02),red_solid )
  
	
	# --
	# -- Portrait des phases
	phases = PhaseDiag( mdl_foret.get_title() )
	phases.portrait( mdl_foret , cnds , xaxis , yaxis , taxis )


if __name__ == '__main__':
    main()

