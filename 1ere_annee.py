import os
import time
import random


class PremiereAnnee:
    def __init__(self):
        self.os_type = str(os.uname().sysname)
        if self.os_type != "Darwin" and self.os_type != "Linux":
            question = "Cet Os n\\'est pas encore supporté, désolé!"
            self.question(question)
            exit()

    def dire(self, string):
        commande = ""
        if self.os_type == "Darwin":
            commande = "say " + string
        elif self.os_type == "Linux":
            #commande = "espeak -vfr+f2 \"" + string + "\""
            commande = "espeak-ng -s 125 -vmb/mb-fr1 \"" + string + "\""

        os.system(commande)

    def question(self, question):
        print(question)
        self.dire(question)

    def question_reponse(self, question):
        self.dire(question)
        return input(question)

    def choix_hasard(self, possibilites, minimum, maximum):
        return possibilites[random.randint(minimum, maximum)]

    def demander_nom(self):
        question = "Quel est ton prénom?"
        self.nom = self.question_reponse(question)
        bonjour = "bonjour" + self.nom
        self.dire(bonjour)

    def quitter(self):
        fin = "Beau travail " + self.nom + " et à la prochaine!"
        print(fin)
        self.dire(fin)
        time.sleep(1)
        exit()

    def valider_action(self, touche):
        if touche != "q":
            return True
        else:
            return False

    def lire_reponse(self, type_reponse, reponse):
        touche = self.question_reponse("\"Enter\" pour continuer ou \"q\" pour quittter")
        if self.valider_action(touche):
            self.dire("le {0} était".format(type_reponse))
            self.dire(reponse)
            touche = self.question_reponse("\"Enter\" pour continuer ou \"q\" pour quittter")
            if self.valider_action(touche):
                return True
            else:
                return self.quitter()
        else:
            return self.quitter()

    def afficher_reponse(self, type_reponse, reponse):
        touche = self.question_reponse("\"Enter\" pour continuer ou \"q\" pour quittter")
        if self.valider_action(touche):
            self.dire("le {0} {1} s\\\'écrit comme ceci:".format(type_reponse, reponse))
            print("====> \033[92m {0} \033[0m <====".format(reponse))
            touche = self.question_reponse("\"Enter\" pour continuer ou \"q\" pour quittter")
            if self.valider_action(touche):
                return True
            else:
                return self.quitter()
        else:
            return self.quitter()

class MotsEtiquettes(PremiereAnnee):
    def __init__(self, nom):
        super().__init__()
        self.nom = nom
        self.dictionnaire_list = dict()

        #####################
        self.liste_A = ["à",
                        "en",
                        "soi",
                        "par",
                        "avec",
                        "dans",
                        "vous",
                        "plus",
                        "et",
                        "ta"]
        self.liste_B = ["aller",
                        "elle",
                        "pour",
                        "autre",
                        "des",
                        "bien",
                        "si",
                        "sur",
                        "aux",
                        "lui"]
        self.liste_C = ["se",
                        "cette",
                        "moi",
                        "où",
                        "jour",
                        "dire",
                        "le",
                        "tous",
                        "ne",
                        "qui"]
        self.liste_D = ["pas",
                        "leur",
                        "un",
                        "que",
                        "être",
                        "tu",
                        "pomme",
                        "ils",
                        "du",
                        "mon"]
        self.liste_E = ["elles",
                        "de",
                        "t'",
                        "tout",
                        "vouloir",
                        "vos",
                        "sans",
                        "ces",
                        "au",
                        "la"]
        self.liste_F = ["toi",
                        "faire",
                        "ce",
                        "il",
                        "son",
                        "uns",
                        "y",
                        "je",
                        "d'",
                        "mais"]
        self.liste_G = ["donner",
                        "prendre",
                        "ma",
                        "une",
                        "par",
                        "sa",
                        "te",
                        "n'est",
                        "qu'il",
                        "ses"]
        self.liste_H = ["avoir",
                        "tes",
                        "me",
                        "ton",
                        "c'est",
                        "les",
                        "j'ai",
                        "cet",
                        "votre",
                        "venir"]
        self.liste_I = ["l'",
                        "savoir",
                        "m'",
                        "pouvoir",
                        "unes",
                        "leurs",
                        "mes"]

        self.dictionnaire_list["A"] = self.liste_A
        self.dictionnaire_list["B"] = self.liste_B
        self.dictionnaire_list["C"] = self.liste_C
        self.dictionnaire_list["D"] = self.liste_D
        self.dictionnaire_list["E"] = self.liste_E
        self.dictionnaire_list["F"] = self.liste_F
        self.dictionnaire_list["G"] = self.liste_G
        self.dictionnaire_list["H"] = self.liste_H
        self.dictionnaire_list["I"] = self.liste_I
        print("=======================================================================================================")
        parole = "Les listes disponibles sont:"
        print(parole)
        self.dire(parole)
        for key in self.dictionnaire_list:
            print("Liste", key, " --> ", self.dictionnaire_list[key])
        print("=======================================================================================================")
        #####################

        question = "Quelles listes veux tu pratiquer?"
        listes = self.question_reponse(question)

        self.dire("Les listes choisies sont les")

        self.valids = list()
        for character in listes.upper():
            if character.isalpha():
                if character in self.dictionnaire_list.keys():
                    self.valids.append(character)
                else:
                    print("La liste", character, "n\'existe pas")
                    exit()
        for each in self.valids:
            print(str(each))
            self.dire(str(each))

        self.liste_de_mots = list()
        for each in self.valids:
            for word in self.dictionnaire_list[each]:
                self.liste_de_mots.append(word)

        maximum = len(self.liste_de_mots)
        nombre_mots = self.nom + ", tu as choisi " + str(maximum) + " mots"
        print(nombre_mots)
        self.dire(nombre_mots)
        time.sleep(1)

        sortie = True
        while sortie:
            sortie = self.lire_un_mot_etiquette()

    def lire_un_mot_etiquette(self):
        mot = self.choix_hasard(self.liste_de_mots, 0, len(self.liste_de_mots) - 1)
        self.question("{0} quel est ce mot ?".format(self.nom))
        print("====> \033[92m {0} \033[0m <====".format(mot))
        return self.lire_reponse("mot", mot)

class Nombres_aleatoires(PremiereAnnee):
    def __init__(self, nom):
        super().__init__()
        self.nom = nom

        # variable du nombre minimum
        question = "À partir de quel nombre veux-tu pratiquer ta lecture des nombres?"
        minimum = int(self.question_reponse(question))

        # variable du nombre maximal
        question = "Jusqu\\'à quel nombre veux-tu pratiquer ta lecture des nombres?"
        maximum = int(self.question_reponse(question))

        print(minimum, maximum)
        commentaire = "Nombre entre " + str(minimum) + " et " + str(maximum)
        self.dire(commentaire)
        sortie = True
        while sortie:
            nombre = random.randint(minimum, maximum)
            self.question("{0} quel est ce nombre ?".format(self.nom))
            print("====> \033[92m {0} \033[0m <====".format(nombre))
            sortie = self.lire_reponse("nombre", str(nombre))

class Dictee(PremiereAnnee):
    def __init__(self, nom):
        super().__init__()
        self.nom = nom
        self.dictionnaire_list = dict()

        #####################
        self.liste_A = ["à",
                        "en",
                        "soi",
                        "par",
                        "avec",
                        "dans",
                        "vous",
                        "plus",
                        "et",
                        "ta"]
        self.liste_B = ["aller",
                        "elle",
                        "pour",
                        "autre",
                        "des",
                        "bien",
                        "si",
                        "sur",
                        "aux",
                        "lui"]
        self.liste_C = ["se",
                        "cette",
                        "moi",
                        "où",
                        "jour",
                        "dire",
                        "le",
                        "tous",
                        "ne",
                        "qui"]
        self.liste_D = ["pas",
                        "leur",
                        "un",
                        "que",
                        "être",
                        "tu",
                        "pomme",
                        "ils",
                        "du",
                        "mon"]
        self.liste_E = ["elles",
                        "de",
                        "t'",
                        "tout",
                        "vouloir",
                        "vos",
                        "sans",
                        "ces",
                        "au",
                        "la"]
        self.liste_F = ["toi",
                        "faire",
                        "ce",
                        "il",
                        "son",
                        "uns",
                        "y",
                        "je",
                        "d'",
                        "mais"]
        self.liste_G = ["donner",
                        "prendre",
                        "ma",
                        "une",
                        "par",
                        "sa",
                        "te",
                        "n'est",
                        "qu'il",
                        "ses"]
        self.liste_H = ["avoir",
                        "tes",
                        "me",
                        "ton",
                        "c'est",
                        "les",
                        "j'ai",
                        "cet",
                        "votre",
                        "venir"]
        self.liste_I = ["l'",
                        "savoir",
                        "m'",
                        "pouvoir",
                        "unes",
                        "leurs",
                        "mes"]

        self.dictionnaire_list["A"] = self.liste_A
        self.dictionnaire_list["B"] = self.liste_B
        self.dictionnaire_list["C"] = self.liste_C
        self.dictionnaire_list["D"] = self.liste_D
        self.dictionnaire_list["E"] = self.liste_E
        self.dictionnaire_list["F"] = self.liste_F
        self.dictionnaire_list["G"] = self.liste_G
        self.dictionnaire_list["H"] = self.liste_H
        self.dictionnaire_list["I"] = self.liste_I
        print("=======================================================================================================")
        parole = "Les listes disponibles sont:"
        print(parole)
        self.dire(parole)
        for key in self.dictionnaire_list:
            print("Liste", key, " --> ", self.dictionnaire_list[key])
        print("=======================================================================================================")
        #####################

        question = "Quelles listes veux tu pratiquer?"
        listes = self.question_reponse(question)

        self.dire("Les listes choisies sont les")

        self.valids = list()
        for character in listes.upper():
            if character.isalpha():
                if character in self.dictionnaire_list.keys():
                    self.valids.append(character)
                else:
                    print("La liste", character, "n\'existe pas")
                    exit()
        for each in self.valids:
            print(str(each))
            self.dire(str(each))

        self.liste_de_mots = list()
        for each in self.valids:
            for word in self.dictionnaire_list[each]:
                self.liste_de_mots.append(word)

        maximum = len(self.liste_de_mots)
        nombre_mots = self.nom + ", tu as choisi " + str(maximum) + " mots"
        print(nombre_mots)
        self.dire(nombre_mots)
        time.sleep(1)

        sortie = True
        while sortie:
            sortie = self.lire_un_mot_dictee()

    def lire_un_mot_dictee(self):
        mot = self.choix_hasard(self.liste_de_mots, 0, len(self.liste_de_mots) - 1)
        self.question("{0} écrit le mot".format(self.nom))
        time.sleep(0.5)
        self.dire(mot)
        time.sleep(5)
        self.dire(mot)
        time.sleep(5)
        self.dire(mot)
        return self.afficher_reponse("mot", mot)

class Dictee_nombres_aleatoires(PremiereAnnee):
    def __init__(self, nom):
        super().__init__()
        self.nom = nom

        # variable du nombre minimum
        question = "À partir de quel nombre veux-tu pratiquer ta dictée des nombres?"
        minimum = int(self.question_reponse(question))

        # variable du nombre maximal
        question = "Jusqu\\'à quel nombre veux-tu pratiquer ta dictée des nombres?"
        maximum = int(self.question_reponse(question))

        print(minimum, maximum)
        commentaire = "Nombre entre " + str(minimum) + " et " + str(maximum)
        self.dire(commentaire)
        sortie = True
        while sortie:
            nombre = random.randint(minimum, maximum)
            self.question("{0} écrit le nombre: ".format(self.nom))
            time.sleep(0.5)
            self.dire(str(nombre))
            time.sleep(2)
            self.dire(str(nombre))
            time.sleep(2)
            self.dire(str(nombre))
            sortie = self.afficher_reponse("nombre", str(nombre))

#programme = MotsEtiquettes()
programme = PremiereAnnee()
programme.demander_nom()

print("A - Mots étiquettes")
print("B - Nombres aléatoires")
print("C - Dictée")
print("D - Dictée de nombres aléatoires")
question = "Quelle activité veux-tu faire? "
reponse = programme.question_reponse(question)

if reponse.upper() == "A":
    MotsEtiquettes(programme.nom)
elif reponse.upper() == "B":
    Nombres_aleatoires(programme.nom)
elif reponse.upper() == "C":
    Dictee(programme.nom)
elif reponse.upper() == "D":
    Dictee_nombres_aleatoires(programme.nom)
else:
    question = ("Désolé, votre choix est non valide")
    programme.question(question)