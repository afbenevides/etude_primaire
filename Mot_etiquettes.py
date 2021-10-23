import random
from gtts import gTTS
import os
import time
import subprocess


# gtts setup
language = "fr"


def dire(string):
    commande = "say " + string
    os.system(commande)


dictionnaire_list = dict()

#####################
liste_A = ["à",
           "en",
           "soi",
           "par",
           "avec",
           "dans",
           "vous",
           "plus",
           "et",
           "ta"]
liste_B = ["aller",
           "elle",
           "pour",
           "autre",
           "des",
           "bien",
           "si",
           "sur",
           "aux",
           "lui"]
liste_C = ["se",
           "cette",
           "moi",
           "où",
           "jour",
           "dire",
           "le",
           "tous",
           "ne",
           "qui"]
liste_D = ["pas",
           "leur",
           "un",
           "que",
           "être",
           "tu",
           "pomme",
           "ils",
           "du",
           "mon"]
liste_E = ["elles",
           "de",
           "t'",
           "tout",
           "vouloir",
           "vos",
           "sans",
           "ces",
           "au",
           "la"]
liste_F = ["toi",
           "faire",
           "ce",
           "il",
           "son",
           "uns",
           "y",
           "je",
           "d'",
           "mais"]
liste_G = ["donner",
           "prendre",
           "ma",
           "une",
           "par",
           "sa",
           "te",
           "n'est",
           "qu'il",
           "ses"]
liste_H = ["avoir",
           "tes",
           "me",
           "ton",
           "c'est",
           "les",
           "j'ai",
           "cet",
           "votre",
           "venir"]
liste_I = ["l'",
           "savoir",
           "m'",
           "pouvoir",
           "unes",
           "leurs",
           "mes"]

dictionnaire_list["A"] = liste_A
dictionnaire_list["B"] = liste_B
dictionnaire_list["C"] = liste_C
dictionnaire_list["D"] = liste_D
dictionnaire_list["E"] = liste_E
dictionnaire_list["F"] = liste_F
dictionnaire_list["G"] = liste_G
dictionnaire_list["H"] = liste_H
dictionnaire_list["I"] = liste_I
print("=======================================================================================================")
for key in dictionnaire_list:
    print("Liste", key, " --> ", dictionnaire_list[key])
print("=======================================================================================================")
#####################

question = "Quel est ton prénom?"
dire(question)
nom = input(question)
bonjour = "bonjour"+nom
dire(bonjour)


question = "Quelles listes veux tu pratiquer?"
dire(question)
listes = input(question)

dire("Les listes choisies sont les")


valids = list()
for character in listes.upper():
    if character.isalpha():
        if character in dictionnaire_list.keys():
            valids.append(character)
        else:
            print("La liste", character, "n'existe pas")
            exit()
for each in valids:
    print(str(each))
    dire(str(each))

liste_de_mots = list()
for each in valids:
    for word in dictionnaire_list[each]:
        liste_de_mots.append(word)


minimum = 0
maximum = len(liste_de_mots)

nombre_mots = nom + ", tu as choisi " + str(maximum) + " mots"
print(nombre_mots)
dire(nombre_mots)
time.sleep(1)

while 1:
    mot = liste_de_mots[random.randint(minimum, maximum - 1)]
    print(nom, "quel est ce mot ?  ====> ", '\033[92m', mot ,'\033[0m', " <====")
    touche = input("Presser n'importe quelle touche pour entendre le mot ou  \"q\" pour quittter")
    if touche != "q":
        dire("le mot était")
        dire(mot)
        touche = input("Presser n'importe quelle touche pour continuer ou  \"q\" pour quittter")
        if touche != "q":
            pass
        else:
            fin = "Beau travail " + nom + " et à la prochaine!"
            print(fin)
            dire(fin)
            time.sleep(1)
            break

    else:
        fin = "Beau travail " + nom + " et à la prochaine!"
        print(fin)
        dire(fin)
        time.sleep(1)
        break
