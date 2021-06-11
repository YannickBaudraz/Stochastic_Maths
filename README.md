# Processus stochastiques

Bonjour

## How to utiliser le programme

Lancez le fichier stochastic.exe

### How ça fonctionne

#### Entrés utilisateurs

Le programme va vous demander trois entrées :

1. Le capital
    - Il doit être un nombre entier
    - S'il n'arrive pas a convertir en nombre entier, le capital sera de 10
1. La probabilité de chance de gagner
    - Il faut mettre un chiffre à virgule et utiliser un point comme virgule (0.5 et non 0,5) !
    - Si c'est un nombre entier, le programme le verra comme 100% de chance de gagner
    - S'il n'arrive pas à convertir en chiffre à virgules, le probabilité sera de 0.5 (50%)
1. Le nombre maximum d'essais
    - Il doit être un nombre entier
    - S'il n'arrive pas a convertir en nombre entier, le nombre d'essais max sera de 5

Vous pouvez ne rien mettre, cela va utiliser les valeurs par défaut.

#### L'algorithme

Tant que le capital n'est pas en dessous de 0.05 (5 centimes) et que le nombre d'essais maximum n'est pas atteint, il va
continuer de jouer pour devenir riche.

La mise à chaque jeu dépend de la probabilité de gagner. Chaque mise en jeu correspond au capital actuel, multiplié par
la probabilité de chance de gagner -> c · p.

Exemple :

- On commence avec 10 avec une probabilité de 30%, on va donc miser 3.- - et sûrement perdre :).
- On a donc perdu 3.- et il nous reste 7.-.
- On rejoue, mais cette fois-ci, on mise 2.10 (30% de 7.-). On gagne !
- On a donc gagné 2.10 et on a maintenant 9.10 (7.- + 2.10).
- Etc, etc...

Ensuite le graphique s'affiche quand c'est fini avec, dans la console, un tableau qui représente le capital à chaque
début de jeu.

Ah, et c'est en Python.
