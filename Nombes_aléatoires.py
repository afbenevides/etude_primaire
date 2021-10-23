import random
from gtts import gTTS
import os
import time
import subprocess


# gtts setup
language = "fr"


def dire(string):
    commande = "say "+string
    os.system(commande)

question = "Quel est ton prénom?"
dire(question)
nom = input(question)
bonjour = "bonjour "+nom
dire(bonjour)
time.sleep(1)

# variable du nombre minimum
minimum = 0

#vaiable du nombre maximal
maximum = 40

print(minimum, maximum)
commentaire = "Nombre entre " + str(minimum) + " et " + str(maximum)
dire(commentaire)
while 1:
    nombre = random.randint(minimum, maximum)
    print(nom, "quel est ce nombre ?  ====> ", '\033[92m', nombre, '\033[0m', " <====")
    touche = input("Presser n'importe quelle touche pour continuer ou  \"q\" pour quittter")
    if touche!="q":
        dire(str(nombre))
    else:
        fin = "Beau travail " + nom + " et à la prochaine!"
        print(fin)
        dire(fin)
        time.sleep(1)
        break

