from modules.tache import Tache
from modules.utilisateur import Utilisateur

class Projet:
    """
    Classe représentant un projet.
    Attributs:
        nom (str): Le nom du projet.
        description (str): La description du projet.
        taches (list): Liste des tâches du projet.
        utilisateur (Utilisateur): L'utilisateur responsable du projet.
    """
    def __init__(self, nom, description, utilisateur:Utilisateur):
        self.nom = nom
        self.description = description
        self.taches = []
        self.utilisateur = utilisateur

    def ajouter_tache(self, tache):
        if isinstance(tache, Tache):
            self.taches.append(tache)
        else:
            raise ValueError("L'objet doit être une instance de Tache")

    def __str__(self):
        return f"Projet: {self.nom}, Description: {self.description}, Tâches: {len(self.taches)}"