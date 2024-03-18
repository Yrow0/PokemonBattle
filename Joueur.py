from rich import print
from rich.console import Console
from rich.table import Table

from Pokemon import Pokemon

console = Console()

class Joueur:
    def __init__(self, nom, argent=0):
        self.nom = nom
        self.manche_gagnee = 0
        self.argent = argent
        self.pokemons = []

    def choisir_pokemon(self, liste_pokemons):
        print(f"{self.nom}, choisissez vos 3 Pokémon :")
        for i, pokemon in enumerate(liste_pokemons, start=1):
            console.print(f"{i}. {pokemon.nom}")
        choix = input("Entrez les numéros de vos 3 Pokémon séparés par des espaces : ")
        choix = choix.split()
        for num in choix:
            num = int(num)
            self.ajouter_pokemon(liste_pokemons[num - 1])

    def ajouter_pokemon(self, pokemon):
        self.pokemons.append(pokemon)

    def choisir_attaque(self, pokemon):
        print(f"{self.nom}, choisissez l'attaque pour {pokemon.nom} :")
        pokemon.afficher_attaques()
        choix = input("Entrez le numéro de l'attaque choisie : ")
        return pokemon.attaques[int(choix) - 1]

    def recuperer_pokemon(self, numero):
        return self.pokemons[numero - 1]

    def afficher_pokemons(self):
        for pokemon in self.pokemons:
            pokemon.afficher()

    def afficher(self):
        table = Table(title="Informations de " + self.nom)
        table.add_column("Propriété", justify="center")
        table.add_column("Valeur", justify="center")

        table.add_row("Nom", self.nom)
        table.add_row("Manche gagnée", str(self.manche_gagnee))
        table.add_row("Argent", str(self.argent))

        console.print(table)
