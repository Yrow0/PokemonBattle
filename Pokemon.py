from rich.console import Console
from rich.table import Table

from Attaque import Attaque

console = Console()

class Pokemon:
    def __init__(self, nom, prix, type1, type2, points_de_vie, niveau, attaque, attaque_speciale, defense, defense_speciale, vitesse):
        self.nom = nom
        self.prix = prix
        self.types = [type1, type2]
        self.points_de_vie = points_de_vie
        self.niveau = niveau
        self.attaque = attaque
        self.attaque_speciale = attaque_speciale
        self.defense = defense
        self.defense_speciale = defense_speciale
        self.vitesse = vitesse
        self.attaques = []

    def ajouter_attaque(self, attaque):
        self.attaques.append(attaque)

    def attaquer(self, pokemon_cible, attaque_utilisee):
        degats = attaque_utilisee.calculer_degats(self, pokemon_cible)
        pokemon_cible.points_de_vie -= degats
        console.print(f"{self.nom} utilise {attaque_utilisee.nom} sur {pokemon_cible.nom} et inflige {degats} dégâts!")

    def est_ko(self):
        return self.points_de_vie <= 0

    def afficher_attaques(self):
        table = Table(title="Attaques de " + self.nom)
        table.add_column("Nom", justify="center")
        table.add_column("Type", justify="center")
        table.add_column("Catégorie", justify="center")
        table.add_column("Précision", justify="center")
        table.add_column("Puissance", justify="center")
        table.add_column("PP", justify="center")

        for attaque in self.attaques:
            table.add_row(attaque.nom, attaque.type_attaque, attaque.categorie, str(attaque.precision), str(attaque.puissance), str(attaque.pp))

        console.print(table)

    def afficher(self):
        table = Table(title="Informations de " + self.nom)
        table.add_column("Propriété", justify="center")
        table.add_column("Valeur", justify="center")

        table.add_row("Nom", self.nom)
        table.add_row("Type(s)", '/'.join(self.types))
        table.add_row("Points de vie", str(self.points_de_vie))
        table.add_row("Niveau", str(self.niveau))
        table.add_row("Attaque", str(self.attaque))
        table.add_row("Attaque spéciale", str(self.attaque_speciale))
        table.add_row("Défense", str(self.defense))
        table.add_row("Défense spéciale", str(self.defense_speciale))
        table.add_row("Vitesse", str(self.vitesse))

        console.print(table)

# Exemple d'utilisation :
if __name__ == "__main__":
    # Création d'une attaque
    attaque_eclair_croix = Attaque("Éclair Croix", "électrique", "physique", 85, 100, 10)

    # Création d'un Pokémon
    types_pikachu = ["électrique"]
    pikachu = Pokemon("Pikachu", 100, types_pikachu, 50, 10, 40, 50, 30, 30, 60)

    # Ajout de l'attaque au Pokémon
    pikachu.ajouter_attaque(attaque_eclair_croix)

    # Affichage des informations du Pokémon
    pikachu.afficher()
