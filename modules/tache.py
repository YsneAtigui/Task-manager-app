class Tache:
    """
    Classe représentant une tâche.
    Attributs:
        titre (str): Le titre de la tâche.
        description (str): La description de la tâche.
        statut (str): Le statut de la tâche (à faire, en cours, terminé).
        utilisateur (Utilisateur): L'utilisateur assigné à la tâche.
    """
    def __init__(self, titre, description, statut="à faire", utilisateur=None):
        self.titre = titre
        self.description = description
        self.statut = statut
        self.utilisateur = utilisateur

    def __str__(self):
        return f"Tâche: {self.titre}, Statut: {self.statut}, Assignée à: {self.utilisateur.nom}"