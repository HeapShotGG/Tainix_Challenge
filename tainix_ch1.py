#######################################################################################################
#TAINIX CHALLENGE : https://tainix.fr/challenge/Utilisation-d-une-fonction
# CHALLENGE LV STARTER - "UTILISATION D'UNE FONCTION"
# ENONCE : 
# Tu dois retourner une chaine de caractère contenant toutes les valeurs qui sont  des Multiple de 3.
#######################################################################################################
#@Author: HeapshotGG
# Date : 30 Avril 2023

# Value est un tableau qui contient une vingtaine de valeur entières comprise entre 10 et 100 

values = [57, 87, 71, 91, 65, 64, 25, 98, 47, 10, 11, 89, 59, 93, 40, 70, 32, 66, 85, 82, 99, 97, 18, 77, 47, 26, 37, 30, 12]

# renvoi une liste des nombre multiple de 3 
values_multiple_by_3 = [value for value in values if value % 3 == 0]

# On transforme le tableau en une chaine de caractères
values_multiple_by_3 = "".join(str(values_multiple_by_3))

# On supprime les espaces dans la chaine de caractère.

values_multiple_by_3 = values_multiple_by_3.strip()
print(values_multiple_by_3)

# on remplace les "," par des "-" 

values_multiple_by_3 = values_multiple_by_3.replace(" ", "")
values_multiple_by_3 = values_multiple_by_3.replace(",","-")

# On affiche la chaine de caractères

print(values_multiple_by_3)








