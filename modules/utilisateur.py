class Utilisateur:
    """
    Classe représentant un utilisateur.
    Attributs:
        nom (str): Le nom de l'utilisateur.
        email (str): L'email de l'utilisateur.
    """
    def __init__(self, nom, email):
        self.nom = nom
        self.email = email

    def __str__(self):
        return f"Utilisateur: {self.nom}, Email: {self.email}"