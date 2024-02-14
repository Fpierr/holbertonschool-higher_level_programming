#!/usr/bin/python3
# Définir deux listes avec des valeurs identiques
liste1 = [1, 2, 3]
liste2 = [1, 2, 3]

# Imprimer les adresses mémoire des objets
print("Adresse mémoire de liste1:", id(liste1))
print("Adresse mémoire de liste2:", id(liste2))

# Vérifier si les variables pointent vers le même objet en mémoire
print("liste1 is liste2:", liste1 is liste2)
