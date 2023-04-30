#######################################################################################################
# TAINIX CHALLENGE : https://tainix.fr/challenge/Boucle-foreach
# CHALLENGE LV STARTER - "Boucle foreach"
# ENONCE : 
# Tu dois retourner la somme des valeurs supérieures ou égales à 5 comprises dans values.
#######################################################################################################
# @Author: HeapshotGG
# Date : 30 Avril 2023


# tableau contenant des entiers compris entre 1 et 10
values = [1, 2, 3, 10, 6, 9, 10, 5, 3, 2, 9, 1, 9, 1, 7, 4, 9, 10, 9, 9, 8, 6, 1, 4, 7]

# on initialise une variable result égale à 0
result = 0

# On parcours la liste et on additione i à la variable result.
for i in values:
    if i >= 5:
        result  = result  + i
    print(result)
        