from modules.projet import Projet
from modules.tache import Tache
from modules.utilisateur import Utilisateur
import json

class GestionnaireDeProjets :

    def __init__(self, fichier_data="data/data.json"):
        self.fichier_data = fichier_data
        self.projets = []
        self.utilisateurs = []
        self.charger_donnee()

    def charger_donnee(self):
        """Charge les données depuis le fichier JSON."""
        try:
            with open(self.fichier_data, "r", encoding="utf-8") as f:
                data = json.load(f)

                # Charger les utilisateurs
                for u in data.get("users", []):
                    utilisateur = Utilisateur(u["nom"], u["email"])
                    self.utilisateurs.append(utilisateur)

                # Charger les projets
                for p in data.get("projets", []):
                    projet = Projet(p["nom"], p["description"], p["user"])

                    # Charger les tâches
                    for t in p.get("taches", []):
                        tache = Tache(t["titre"], t["description"], t["statut"], t["user"])
                        projet.taches.append(tache)

                    self.projets.append(projet)

                print("Données chargées avec succès.")
        except FileNotFoundError:
            print(f"Fichier '{self.fichier_data}' non trouvé. Création d'un nouveau fichier.")
            self.sauvegarder_donnee()  # Crée un fichier JSON vide
        except json.JSONDecodeError:
            print(f"Erreur de décodage JSON dans le fichier '{self.fichier_data}'.")
        except Exception as e:
            print(f"Erreur inattendue lors du chargement: {e}")

    def sauvegarder_donnee(self):
        """Sauvegarde les données dans le fichier JSON."""
        data = {
            "users": [{"nom": u.nom, "email": u.email} for u in self.utilisateurs],
            "projets": [
                {
                    "nom": p.nom,
                    "description": p.description,
                    "user": p.utilisateur.nom if isinstance(p.utilisateur, Utilisateur) else p.utilisateur,
                    "taches": [
                        {
                            "titre": t.titre,
                            "description": t.description,
                            "statut": t.statut,
                            "user": t.utilisateur.nom if isinstance(t.utilisateur, Utilisateur) else t.utilisateur
                        }
                        for t in p.taches
                    ]
                }
                for p in self.projets
            ]
        }

        try:
            with open(self.fichier_data, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print("Données sauvegardées avec succès.")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde des données : {e}")

    

    def ajouter_utilisateur(self,user):
        """
        Ajoute un utilisateur et sauvegarde automatiquement les données.
        
        :param nom: Nom de l'utilisateur.
        :param email: Email de l'utilisateur.
        """
        # Vérifier si l'utilisateur existe déjà
        if any(u.nom == user.nom for u in self.utilisateurs):
            print(f"L'utilisateur '{user.nom}' existe déjà.")
            return

        # Ajouter l'utilisateur
        self.utilisateurs.append(user)
        print(f"Utilisateur ajouté : {user.nom} ({user.email})")

        # Sauvegarder les données
        self.sauvegarder_donnee()

    def modifier_utilisateur(self, nom_utilisateur, nouveau_nom=None, nouvel_email=None):
        """
    Modifie les informations d'un utilisateur existant.
    
    :param nom_utilisateur: Nom de l'utilisateur à modifier.
    :param nouveau_nom: Nouveau nom de l'utilisateur (optionnel).
    :param nouvel_email: Nouvel email de l'utilisateur (optionnel).
        """
        # Trouver l'utilisateur correspondant
        utilisateur_trouve = next((u for u in self.utilisateurs if u.nom == nom_utilisateur), None)
    
        if not utilisateur_trouve:
            print(f"Utilisateur '{nom_utilisateur}' non trouvé.")
            return

        # Modifier le nom de l'utilisateur si un nouveau nom est fourni
        if nouveau_nom:
            utilisateur_trouve.nom = nouveau_nom
            print(f"Nom de l'utilisateur '{nom_utilisateur}' modifié en '{nouveau_nom}'.")

        # Modifier l'email de l'utilisateur si un nouvel email est fourni
        if nouvel_email:
            utilisateur_trouve.email = nouvel_email
            print(f"Email de l'utilisateur '{nom_utilisateur}' modifié en '{nouvel_email}'.")

        # Sauvegarder les données
        self.sauvegarder_donnee()
        
    def supprimer_utilisateur(self, nom_utilisateur):
        """
    Supprime un utilisateur existant.
    
    :param nom_utilisateur: Nom de l'utilisateur à supprimer.
        """
        # Trouver l'utilisateur correspondant
        utilisateur_trouve = next((u for u in self.utilisateurs if u.nom == nom_utilisateur), None)
    
        if not utilisateur_trouve:
            print(f"Utilisateur '{nom_utilisateur}' non trouvé.")
            return

        # Supprimer l'utilisateur
        self.utilisateurs.remove(utilisateur_trouve)
        print(f"Utilisateur '{nom_utilisateur}' supprimé.")

    # Mettre à jour les projets et tâches associés
        for projet in self.projets:
            if projet.utilisateur == nom_utilisateur:
                projet.utilisateur = None  # Ou réaffecter à un autre utilisateur
            for tache in projet.taches:
                if tache.utilisateur == nom_utilisateur:
                    tache.utilisateur = None  # Ou réaffecter à un autre utilisateur

    # Sauvegarder les données
        self.sauvegarder_donnee()

    def ajouter_tache(self,projet,tache):
        for p in self.projets :
            if p.nom == projet.nom :
                p.ajouter_tache(tache)
                print("ajouter tache")
                # Sauvegarder les données
                self.sauvegarder_donnee()

    def ajouter_project(self,projet):
        
        if any(projet.nom == p.nom for p in self.projets):
            print(f"Projet {projet.nom} existe déjà.")
            return
        
        self.projets.append(projet)
        print(f"project ajoute : f{projet.nom}")
        # Sauvegarder les données
        self.sauvegarder_donnee()


    def modifier_projet(self, nom_projet, nouveau_nom=None, nouvelle_description=None):
        """
    Modifie les informations d'un projet existant.
    
    :param nom_projet: Nom du projet à modifier.
    :param nouveau_nom: Nouveau nom du projet (optionnel).
    :param nouvelle_description: Nouvelle description du projet (optionnel).
        """
    # Trouver le projet correspondant
        projet_trouve = next((p for p in self.projets if p.nom == nom_projet), None)
    
        if not projet_trouve:
            print(f"Projet '{nom_projet}' non trouvé.")
            return

        # Modifier le nom du projet si un nouveau nom est fourni
        if nouveau_nom:
            projet_trouve.nom = nouveau_nom
            print(f"Nom du projet '{nom_projet}' modifié en '{nouveau_nom}'.")

        # Modifier la description du projet si une nouvelle description est fournie
        if nouvelle_description:
            projet_trouve.description = nouvelle_description
            print(f"Description du projet '{nom_projet}' modifiée.")

        # Sauvegarder les données
        self.sauvegarder_donnee()

    def supprimer_projet(self, nom_projet):
        """
        Supprime un projet existant.
    
        :param nom_projet: Nom du projet à supprimer.
        """
        # Trouver le projet correspondant
        projet_trouve = next((p for p in self.projets if p.nom == nom_projet), None)
    
        if not projet_trouve:
            print(f"Projet '{nom_projet}' non trouvé.")
            return

    # Supprimer le projet
        self.projets.remove(projet_trouve)
        print(f"Projet '{nom_projet}' supprimé.")

    # Sauvegarder les données
        self.sauvegarder_donnee()



    def modifier_tache(self, titre_tache, nouveau_titre=None, nouvelle_description=None, nouveau_statut=None):
        """
    Modifie les informations d'une tâche existante.
    
    :param titre_tache: Titre de la tâche à modifier.
    :param nouveau_titre: Nouveau titre de la tâche (optionnel).
    :param nouvelle_description: Nouvelle description de la tâche (optionnel).
    :param nouveau_statut: Nouveau statut de la tâche (optionnel).
        """
    # Trouver la tâche correspondante
        for projet in self.projets:
            for tache in projet.taches:
                if tache.titre == titre_tache:
                    # Modifier le titre de la tâche si un nouveau titre est fourni
                    if nouveau_titre:
                        tache.titre = nouveau_titre
                        print(f"Titre de la tâche '{titre_tache}' modifié en '{nouveau_titre}'.")

                # Modifier la description de la tâche si une nouvelle description est fournie
                    if nouvelle_description:
                        tache.description = nouvelle_description
                        print(f"Description de la tâche '{titre_tache}' modifiée.")

                    # Modifier le statut de la tâche si un nouveau statut est fourni
                    if nouveau_statut:
                        tache.statut = nouveau_statut
                        print(f"Statut de la tâche '{titre_tache}' modifié en '{nouveau_statut}'.")

                    # Sauvegarder les données
                    self.sauvegarder_donnee()
                    return

        print(f"Tâche '{titre_tache}' non trouvée.")

    
    def supprimer_tache(self, titre_tache):
        """
    Supprime une tâche existante.
    
    :param titre_tache: Titre de la tâche à supprimer.
        """
        # Trouver la tâche correspondante
        for projet in self.projets:
            for tache in projet.taches:
                if tache.titre == titre_tache:
                    # Supprimer la tâche
                    projet.taches.remove(tache)
                    print(f"Tâche '{titre_tache}' supprimée.")

                    # Sauvegarder les données
                    self.sauvegarder_donnee()
                    return

        print(f"Tâche '{titre_tache}' non trouvée.")