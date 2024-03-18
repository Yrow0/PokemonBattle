from random import shuffle

from Attaque import Attaque
from Joueur import Joueur
from Pokemon import Pokemon


class Jeu:
    def __init__(self):
        self.joueurs = []

    def creer_joueur(self, num_joueur):
        nom_joueur = input(f"Joueur {num_joueur}, veuillez saisir votre nom : ")
        argent = 1000  # Argent initial
        joueur = Joueur(nom_joueur, argent)
        joueur.choisir_pokemon(self.generer_liste_pokemons())
        self.joueurs.append(joueur)

    def jouer(self):
        # Création des joueurs
        for i in range(1, 3):
            self.creer_joueur(i)

        # Début du jeu
        joueur1, joueur2 = self.joueurs
        print("Le jeu commence !")

        for round_num in range(1, 4):
            print(f"\nRound {round_num}")
            joueur1_pokemon = joueur1.recuperer_pokemon(round_num)
            joueur2_pokemon = joueur2.recuperer_pokemon(round_num)
            print(f"{joueur1.nom} envoie {joueur1_pokemon.nom}!")
            print(f"{joueur2.nom} envoie {joueur2_pokemon.nom}!")

            while not joueur1_pokemon.est_ko() and not joueur2_pokemon.est_ko():
                if joueur1_pokemon.vitesse > joueur2_pokemon.vitesse:
                    attaque_joueur1 = joueur1.choisir_attaque(joueur1_pokemon)
                    joueur1_pokemon.attaquer(joueur2_pokemon, attaque_joueur1)
                    if joueur2_pokemon.est_ko():
                        break
                    attaque_joueur2 = joueur2.choisir_attaque(joueur2_pokemon)
                    joueur2_pokemon.attaquer(joueur1_pokemon, attaque_joueur2)
                else:
                    attaque_joueur2 = joueur2.choisir_attaque(joueur2_pokemon)
                    joueur2_pokemon.attaquer(joueur1_pokemon, attaque_joueur2)
                    if joueur1_pokemon.est_ko():
                        break
                    attaque_joueur1 = joueur1.choisir_attaque(joueur1_pokemon)
                    joueur1_pokemon.attaquer(joueur2_pokemon, attaque_joueur1)

            if joueur1_pokemon.est_ko():
                print(f"{joueur1.nom} n'a plus de Pokémon ! {joueur2.nom} gagne le round {round_num}.")
                joueur2.manche_gagnee += 1
            elif joueur2_pokemon.est_ko():
                print(f"{joueur2.nom} n'a plus de Pokémon ! {joueur1.nom} gagne le round {round_num}.")
                joueur1.manche_gagnee += 1
            else:
                print("Les deux Pokémon ne peuvent plus se battre ! Match nul.")

        # Détermination du vainqueur
        if joueur1.manche_gagnee >= 2:
            print(f"\n{joueur1.nom} remporte la partie !")
        elif joueur2.manche_gagnee >= 2:
            print(f"\n{joueur2.nom} remporte la partie !")
        else:
            print("Match nul !")

        # Demande de rejouer
        rejouer = input("Voulez-vous rejouer ? (oui/non) : ")
        if rejouer.lower() == "oui":
            self.jouer()


    def generer_liste_pokemons(self):
        # Générer une liste de Pokémon à acheter
        pokemons = {
            "Bulbizarre": {
                "types": ["plante", "poison"],
                "pv": 45,
                "attaque": 49,
                "defense": 49,
                "attaque_speciale": 65,
                "defense_speciale": 65,
                "vitesse": 45,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Tranch'Herbe", "plante", "physique", 95, 55, 25),
                    ("Vampigraine", "plante", "speciale", 90, 0, 10),
                    ("Fouet Lianes", "plante", "physique", 100, 45, 15)
                ]
            },
            "Herbizarre": {
                "types": ["plante", "poison"],
                "pv": 60,
                "attaque": 62,
                "defense": 63,
                "attaque_speciale": 80,
                "defense_speciale": 80,
                "vitesse": 60,
                "attaques": [
                    ("Vive-Attaque", "normal", "physique", 100, 40, 30),
                    ("Rafale Feuilles", "plante", "speciale", 90, 55, 20),
                    ("Croissance", "normal", "statut", 0, 0, 20),
                    ("Mega-Sangsue", "plante", "speciale", 100, 75, 10)
                ]
            },
            "Salamèche": {
                "types": ["feu"],
                "pv": 39,
                "attaque": 52,
                "defense": 43,
                "attaque_speciale": 60,
                "defense_speciale": 50,
                "vitesse": 65,
                "attaques": [
                    ("Griffe", "normal", "physique", 100, 40, 35),
                    ("Flammèche", "feu", "speciale", 100, 40, 25),
                    ("Danse Flamme", "feu", "physique", 100, 50, 20),
                    ("Crocs Feu", "feu", "physique", 100, 65, 15)
                ]
            },
            "Carapuce": {
                "types": ["eau"],
                "pv": 44,
                "attaque": 48,
                "defense": 65,
                "attaque_speciale": 50,
                "defense_speciale": 64,
                "vitesse": 43,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Pistolet à O", "eau", "speciale", 100, 40, 25),
                    ("Pistolet à O", "eau", "speciale", 100, 40, 25),
                    ("Hydrocanon", "eau", "speciale", 80, 110, 5)
                ]
            },
            "Aspicot": {
                "types": ["insecte", "poison"],
                "pv": 40,
                "attaque": 35,
                "defense": 30,
                "attaque_speciale": 20,
                "defense_speciale": 20,
                "vitesse": 50,
                "attaques": [
                    ("Dard-Venin", "poison", "physique", 100, 15, 35),
                    ("Griffe", "normal", "physique", 100, 40, 35),
                    ("Picpic", "normal", "physique", 100, 35, 30),
                    ("Toxic", "poison", "statut", 90, 0, 10)
                ]
            },
            "Roucool": {
                "types": ["normal", "vol"],
                "pv": 40,
                "attaque": 45,
                "defense": 40,
                "attaque_speciale": 35,
                "defense_speciale": 35,
                "vitesse": 56,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Tornade", "vol", "speciale", 100, 40, 35),
                    ("Cru-Aile", "vol", "physique", 95, 60, 20),
                    ("Reflet", "normal", "statut", 0, 0, 15)
                ]
            },
            "Rattata": {
                "types": ["normal"],
                "pv": 30,
                "attaque": 56,
                "defense": 35,
                "attaque_speciale": 25,
                "defense_speciale": 35,
                "vitesse": 72,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Mimi-Queue", "normal", "statut", 100, 0, 30),
                    ("Coup d'Boule", "normal", "physique", 100, 70, 15),
                    ("Vive-Attaque", "normal", "physique", 100, 40, 30)
                ]
            },
            "Piafabec": {
                "types": ["normal", "vol"],
                "pv": 40,
                "attaque": 60,
                "defense": 30,
                "attaque_speciale": 31,
                "defense_speciale": 31,
                "vitesse": 70,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Bec Vrille", "normal", "physique", 100, 35, 35),
                    ("Picpic", "normal", "physique", 100, 35, 30),
                    ("Jet de Sable", "sol", "statut", 100, 0, 15)
                ]
            },
            "Abo": {
                "types": ["poison"],
                "pv": 35,
                "attaque": 60,
                "defense": 44,
                "attaque_speciale": 40,
                "defense_speciale": 54,
                "vitesse": 55,
                "attaques": [
                    ("Acide", "poison", "speciale", 100, 40, 30),
                    ("Vive-Attaque", "normal", "physique", 100, 40, 30),
                    ("Morsure", "normal", "physique", 100, 60, 25),
                    ("Bombsmog", "poison", "speciale", 100, 65, 20)
                ]
            },
            "Pikachu": {
                "types": ["électrique"],
                "pv": 35,
                "attaque": 55,
                "defense": 30,
                "attaque_speciale": 50,
                "defense_speciale": 40,
                "vitesse": 90,
                "attaques": [
                    ("Vive-Attaque", "normal", "physique", 100, 40, 30),
                    ("Fatal-Foudre", "électrique", "speciale", 70, 120, 5),
                    ("Tonnerre", "électrique", "speciale", 100, 95, 15),
                    ("Eclair", "électrique", "speciale", 100, 40, 30)
                ]
            },
            "Sabelette": {
                "types": ["sol"],
                "pv": 50,
                "attaque": 75,
                "defense": 85,
                "attaque_speciale": 30,
                "defense_speciale": 30,
                "vitesse": 40,
                "attaques": [
                    ("Griffe", "normal", "physique", 100, 40, 35),
                    ("Jet de Sable", "sol", "statut", 100, 0, 15),
                    ("Crocs Feu", "feu", "physique", 100, 65, 15),
                    ("Tunnel", "sol", "statut", 100, 0, 10)
                ]
            },
            "Racaillou": {
                "types": ["roche", "sol"],
                "pv": 40,
                "attaque": 80,
                "defense": 100,
                "attaque_speciale": 30,
                "defense_speciale": 30,
                "vitesse": 20,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Jet-Pierres", "roche", "physique", 90, 50, 15),
                    ("Mimi-Queue", "normal", "statut", 100, 0, 30),
                    ("Jet de Sable", "sol", "statut", 100, 0, 15)
                ]
            },
            "Nidoran♀": {
                "types": ["poison"],
                "pv": 55,
                "attaque": 47,
                "defense": 52,
                "attaque_speciale": 40,
                "defense_speciale": 40,
                "vitesse": 41,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Dard-Venin", "poison", "physique", 100, 15, 35),
                    ("Mimi-Queue", "normal", "statut", 100, 0, 30),
                    ("Groz'Yeux", "normal", "statut", 100, 0, 30)
                ]
            },
            "Nidoran♂": {
                "types": ["poison"],
                "pv": 46,
                "attaque": 57,
                "defense": 40,
                "attaque_speciale": 40,
                "defense_speciale": 40,
                "vitesse": 50,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Griffe", "normal", "physique", 100, 40, 35),
                    ("Mimi-Queue", "normal", "statut", 100, 0, 30),
                    ("Groz'Yeux", "normal", "statut", 100, 0, 30)
                ]
            },
            "Mélofée": {
                "types": ["fée"],
                "pv": 70,
                "attaque": 45,
                "defense": 48,
                "attaque_speciale": 60,
                "defense_speciale": 65,
                "vitesse": 35,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Eclats Magiques", "fée", "speciale", 100, 40, 25),
                    ("Métronome", "normal", "statut", 0, 0, 10),
                    ("Doux Parfum", "normal", "statut", 100, 0, 20)
                ]
            },
            "Goupix": {
                "types": ["feu"],
                "pv": 38,
                "attaque": 41,
                "defense": 40,
                "attaque_speciale": 50,
                "defense_speciale": 65,
                "vitesse": 65,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Flammèche", "feu", "speciale", 100, 40, 25),
                    ("Griffe", "normal", "physique", 100, 40, 35),
                    ("Hypnose", "psy", "statut", 60, 0, 20)
                ]
            },
            "Rondoudou": {
                "types": ["normal", "fée"],
                "pv": 115,
                "attaque": 45,
                "defense": 20,
                "attaque_speciale": 45,
                "defense_speciale": 25,
                "vitesse": 20,
                "attaques": [
                    ("Métronome", "normal", "statut", 0, 0, 10),
                    ("Vive-Attaque", "normal", "physique", 100, 40, 30),
                    ("Doux Parfum", "normal", "statut", 100, 0, 20),
                    ("Lire-Esprit", "psy", "statut", 100, 0, 25)
                ]
            },
            "Nosferapti": {
                "types": ["poison", "vol"],
                "pv": 40,
                "attaque": 45,
                "defense": 35,
                "attaque_speciale": 30,
                "defense_speciale": 40,
                "vitesse": 55,
                "attaques": [
                    ("Acide", "poison", "speciale", 100, 40, 30),
                    ("Griffe", "normal", "physique", 100, 40, 35),
                    ("Tranch'Air", "vol", "physique", 95, 55, 25),
                    ("Pics Toxik", "poison", "physique", 100, 15, 20)
                ]
            },
            "Mystherbe": {
                "types": ["plante", "poison"],
                "pv": 45,
                "attaque": 50,
                "defense": 55,
                "attaque_speciale": 75,
                "defense_speciale": 65,
                "vitesse": 30,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Poudre Dodo", "plante", "statut", 75, 0, 15),
                    ("Poudre Toxik", "poison", "statut", 75, 0, 35),
                    ("Para-Spore", "normal", "statut", 100, 0, 30)
                ]
            },
            "Ptitard": {
                "types": ["eau"],
                "pv": 40,
                "attaque": 50,
                "defense": 40,
                "attaque_speciale": 40,
                "defense_speciale": 40,
                "vitesse": 90,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Pistolet à O", "eau", "speciale", 100, 40, 25),
                    ("Hydrocanon", "eau", "speciale", 80, 110, 5),
                    ("Tourniquet", "eau", "physique", 100, 15, 20)
                ]
            },
            "Tadmorv": {
                "types": ["poison"],
                "pv": 80,
                "attaque": 80,
                "defense": 50,
                "attaque_speciale": 40,
                "defense_speciale": 50,
                "vitesse": 25,
                "attaques": [
                    ("Acide", "poison", "speciale", 100, 40, 30),
                    ("Bombsmog", "poison", "speciale", 100, 65, 20),
                    ("Toxic", "poison", "statut", 90, 0, 10),
                    ("Détritus", "poison", "physique", 100, 65, 20)
                ]
            },
            "Kokiyas": {
                "types": ["eau"],
                "pv": 30,
                "attaque": 65,
                "defense": 100,
                "attaque_speciale": 45,
                "defense_speciale": 25,
                "vitesse": 40,
                "attaques": [
                    ("Charge", "normal", "physique", 100, 40, 35),
                    ("Pistolet à O", "eau", "speciale", 100, 40, 25),
                    ("Vibraqua", "eau", "speciale", 100, 60, 20),
                    ("Jet de Sable", "sol", "statut", 100, 0, 15)
                ]
            }
        }
        liste_pokemons = []
        for nom, data in pokemons.items():
            pokemon = Pokemon(nom, 100, data["types"][0], data["types"][1] if len(data["types"]) > 1 else None,
                              data["pv"], 50, data["attaque"], data["defense"], data["attaque_speciale"],
                              data["defense_speciale"], data["vitesse"])
            for attaque_data in data["attaques"]:
                nom_attaque, type_attaque, categorie, precision, puissance, pp = attaque_data
                attaque = Attaque(nom_attaque, type_attaque, categorie, precision, puissance, pp)
                pokemon.ajouter_attaque(attaque)
            liste_pokemons.append(pokemon)

        return liste_pokemons


# Programme principal
if __name__ == "__main__":
    jeu = Jeu()
    jeu.jouer()



