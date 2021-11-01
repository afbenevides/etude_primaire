#importer la librairie random (pour accès à random.randomint()
import random

# Une variable sert à garder une valeur en mémoire pour l'utiliser plus tard
# Pour assigner du texte à la variable écrire ==>  nom_variable = "texte"
variable1 = "Bonjour"

# Pour assigner un nombre entier à la variable écrire ==>  nom_variable = le_nombre
variable2 = 34

# Pour afficher le résultat d'une ou des variables ==> print(variables_voulues)
print(variable1, variable2)

# Pour choisir un nombre aléatoire, utiliser la fonction random.randint(min,max)
# note: pour avoir accès à random.randint, il faut importé la librairie random

print(random.randint(1,100))