from random import choice

def jeu():
    print("Bienvenue sur la roulette française. Les règles sont simples : c'est comme une roulette russe, mais avec quelques objets. Amusez-vous bien !")

    vie_ordi = 6
    vie_joueur = 6
    protection = False         # Casque
    double_degats = False      # Couteau
    passer_tour_ordi = False   # Menottes

    while vie_joueur > 0 and vie_ordi > 0:
        print()
        afficher_etat(vie_ordi, vie_joueur)
        print()

        action = input("Que voulez-vous faire ? (Tirer, Utiliser un objet) ").strip().capitalize()

        if action == "Tirer":
            cible = demander_cible()
            if cible == "ordinateur":
                vie_ordi = tirer_sur_cible("ordinateur", vie_ordi, double_degats)
            elif cible == "joueur":
                vie_joueur = tirer_sur_cible("joueur", vie_joueur, double_degats, protection)
                protection = False  # Le casque ne protège qu'une fois
            double_degats = False  # Effet du couteau consommé après le tir

        elif action == "Utiliser un objet":
            objet, effet = utiliser_objet()
            if objet == "Pansement":
                if vie_joueur < 6:
                    vie_joueur += 1
                    print("Vous avez regagné une vie.")
                else:
                    print("Vous avez déjà toutes vos vies.")
            elif objet == "Casque":
                protection = True
            elif objet == "Couteau":
                double_degats = True
            elif objet == "Menottes":
                passer_tour_ordi = True
            elif objet == "Lunettes":
                if balle_presente():
                    print("Lunettes : Une balle est présente dans le canon.")
                else:
                    print("Lunettes : Aucune balle n'est présente.")
            # Si l'objet permet un tir direct :
            if effet:
                cible = demander_cible()
                if cible == "ordinateur":
                    vie_ordi = tirer_sur_cible("ordinateur", vie_ordi, double_degats)
                elif cible == "joueur":
                    vie_joueur = tirer_sur_cible("joueur", vie_joueur, double_degats, protection)
                    protection = False
                double_degats = False  # Couteau ne dure qu’un tir

        else:
            print("Action invalide.")

        # Tour de l'ordinateur
        if vie_joueur > 0 and vie_ordi > 0 and not passer_tour_ordi:
            print("\nTour de l'ordinateur...")
            if balle_presente():
                if protection:
                    print("L'ordinateur a tiré sur vous mais vous aviez un casque. Vous êtes protégé !")
                    protection = False
                else:
                    vie_joueur -= 1
                    print("L'ordinateur a tiré sur vous et une balle était dans le canon. Vous perdez une vie.")
            else:
                print("L'ordinateur a tiré sur vous mais aucune balle n'était dans le canon. Ouf !")
        elif passer_tour_ordi:
            print("\nLes menottes ont empêché l'ordinateur de jouer ce tour.")
            passer_tour_ordi = False  # Réinitialiser l'effet des menottes

    print()
    afficher_etat(vie_ordi, vie_joueur)
    if vie_ordi <= 0:
        print("🎉 Bravo ! Vous avez gagné.")
    else:
        print("💀 Dommage ! L'ordinateur a gagné.")


def balle_presente():
    return choice([True, False])


def tirer_sur_cible(cible, vie_cible, double=False, protege=False):
    if balle_presente():
        degats = 2 if double else 1
        if protege:
            print(f"Vous avez tiré sur {cible} mais il/elle était protégé(e) ! Pas de dégâts.")
        else:
            vie_cible -= degats
            print(f"Balle dans le canon ! {cible.capitalize()} perd {degats} vie(s).")
    else:
        print(f"Aucune balle dans le canon. {cible.capitalize()} est sauf.")
    return vie_cible


def demander_cible():
    while True:
        cible = input("Sur qui voulez-vous tirer ? (ordinateur, joueur) ").strip().lower()
        if cible in ["ordinateur", "joueur"]:
            return cible
        else:
            print("Cible invalide. Veuillez choisir 'ordinateur' ou 'joueur'.")


def utiliser_objet():
    print("Objets disponibles : Casque, Lunettes, Pansement, Couteau, Menottes")
    objet = input("Quel objet voulez-vous utiliser ? ").strip().capitalize()
    effet = False

    if objet == "Casque":
        print("Vous avez utilisé un casque. Vous serez protégé contre la prochaine balle.")
    elif objet == "Lunettes":
        effet = False  # Ne déclenche pas de tir
    elif objet == "Pansement":
        effet = False
    elif objet == "Couteau":
        print("Vous avez utilisé un couteau. Votre prochain tir fera double dégâts.")
        effet = True
    elif objet == "Menottes":
        print("Vous avez menotté l'ordinateur. Il ne jouera pas ce tour.")
        effet = False
    else:
        print("Objet invalide.")
        return utiliser_objet()

    return objet, effet


def afficher_etat(vie_ordi, vie_joueur):
    print(f"Vie de l'ordinateur : {'❤' * vie_ordi} ({vie_ordi})")
    print(f"Votre vie           : {'❤' * vie_joueur} ({vie_joueur})")


# Lancer le jeu
jeu()

