from rich import print


class Attaque:
    def __init__(self, nom, type_attaque, categorie, precision, puissance, pp):
        self.nom = nom
        self.type_attaque = type_attaque
        self.categorie = categorie
        self.precision = precision
        self.puissance = puissance
        self.pp = pp

    def calculer_degats(self, attaquant, attaque_cible):
        stab = 1
        if self.type_attaque in attaquant.types:  # Vérification du STAB
            stab = 1.5

        if self.categorie == "physique":
            attaque = attaquant.attaque
            defense = attaque_cible.defense
        elif self.categorie == "speciale":
            attaque = attaquant.attaque_speciale
            defense = attaque_cible.defense_speciale
        elif self.categorie == "statut":
            return 0

        degats = (((((2 * attaquant.niveau) / 5) + 2) * self.puissance * (attaque / defense)) / 50 + 2) * stab

        # Si les dégâts sont inférieurs ou égaux à zéro, renvoyer 0
        if degats <= 0:
            return 0
        else:
            return int(degats)

    def afficher(self):
        info = f"Nom: {self.nom}\nType: {self.type_attaque}\nCatégorie: {self.categorie}\nPrécision: {self.precision}\nPuissance: {self.puissance}\nPP: {self.pp}"
        print(info)


