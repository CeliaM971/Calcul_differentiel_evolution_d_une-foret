# Calcul-differentiel_evolution-d-une-foret

# Modélisation de l'évolution d'une forêt et de son humus

Ce projet modélise l'évolution d'une forêt et de son humus à l'aide d'un système de deux équations différentielles. Nous étudions les points critiques de ce système ainsi que leur stabilité.

Deux approches distinctes ont été implémentées :

## Version 1 : Méthode de Runge-Kutta 4 sur un notebook jupyter

Le fichier `Système_Foret_Humus_runge_kutta.ipynb` contient une implémentation simple de la simulation.  
Aucune manipulation particulière n'est nécessaire :  
👉 Il suffit d'exécuter les cellules dans l'ordre pour visualiser les résultats.

## Version 2 : Programmation orientée objet

Cette version est organisée en plusieurs modules.  
Pour l'utiliser :

1. Ouvrir `main.py`.
2. Modifier les **conditions initiales** et/ou les **paramètres** du système selon vos besoins:
     - Pour observer le comportement proche de la solution H2, nous avons utilisé un axe des x entre 0 et 0.05 et deux conditions initiales H(0)=0.017 et H(0)=0.018
     - Pour observer le comportement proche de la solution H1, nous avons utilisé un axe des x entre 0.00038 et 0.00052 et deux conditions initiales H(0)=4.10^(-4) et H(0)=5.10^(-4)
4. Exécuter le script pour observer l'évolution du système.

## 📊 Visualisations

Les deux versions génèrent des graphiques permettant d’observer :

- L’évolution temporelle de la biomasse forestière et de l’humus (seulement pour le notebook jupyter)
- Les portraits de phase
- Les champs de gradient (seulement pour le code en POO)
- La convergence (ou non) vers les points critiques.

## ⚙️ Prérequis

- Python 3.x
- `matplotlib`, `numpy`, `scipy` (et `jupyter` si vous utilisez la version Notebook)


Ce projet a été réalisé dans le cadre d’un cours de calcul différentiel et de programmation python.
