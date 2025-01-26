import tkinter as tk
from tkinter import messagebox, ttk
from modules.projet import Projet
from modules.tache import Tache
from modules.utilisateur import Utilisateur
from modules.gestion import GestionnaireDeProjets

class GestionnaireGUI:
    def __init__(self, gestionnaire):
        self.gestionnaire = gestionnaire

        # Créer la fenêtre principale
        self.root = tk.Tk()
        self.root.title("Gestionnaire de Projets")
        self.root.geometry("600x700")
        self.root.configure(bg="#f0f0f0")

        # Créer un notebook (onglets)
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Onglet pour les utilisateurs (ajouter, modifier, supprimer)
        self.onglet_utilisateurs = ttk.Frame(self.notebook)
        self.notebook.add(self.onglet_utilisateurs, text="Utilisateurs")
        self.creer_onglet_utilisateurs()

        # Onglet pour les projets (ajouter, modifier, supprimer)
        self.onglet_projets = ttk.Frame(self.notebook)
        self.notebook.add(self.onglet_projets, text="Projets")
        self.creer_onglet_projets()

        # Onglet pour les tâches (ajouter, modifier, supprimer)
        self.onglet_taches = ttk.Frame(self.notebook)
        self.notebook.add(self.onglet_taches, text="Tâches")
        self.creer_onglet_taches()

        # Onglet pour afficher les données
        self.onglet_afficher = ttk.Frame(self.notebook)
        self.notebook.add(self.onglet_afficher, text="Afficher Données")
        self.creer_onglet_afficher()

        # Démarrer la boucle principale de l'interface
        self.root.mainloop()

    def creer_onglet_utilisateurs(self):
        """Crée l'onglet pour gérer les utilisateurs."""
        frame = ttk.Frame(self.onglet_utilisateurs)
        frame.pack(padx=20, pady=20)

        # Section pour ajouter un utilisateur
        ttk.Label(frame, text="Ajouter un Utilisateur", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Nom:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.nom_utilisateur = ttk.Entry(frame, width=30)
        self.nom_utilisateur.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.email_utilisateur = ttk.Entry(frame, width=30)
        self.email_utilisateur.grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Ajouter Utilisateur", command=self.ajouter_utilisateur_gui, style="TButton").grid(row=3, column=0, columnspan=2, pady=10)

        # Section pour modifier un utilisateur
        ttk.Label(frame, text="Modifier un Utilisateur", font=("Arial", 14, "bold")).grid(row=4, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Utilisateur à modifier:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.utilisateur_modifier = ttk.Combobox(frame, values=[u.nom for u in self.gestionnaire.utilisateurs], width=27)
        self.utilisateur_modifier.grid(row=5, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Nouveau nom:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.nouveau_nom_utilisateur = ttk.Entry(frame, width=30)
        self.nouveau_nom_utilisateur.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Nouvel email:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.nouvel_email_utilisateur = ttk.Entry(frame, width=30)
        self.nouvel_email_utilisateur.grid(row=7, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Modifier Utilisateur", command=self.modifier_utilisateur_gui, style="TButton").grid(row=8, column=0, columnspan=2, pady=10)

        # Section pour supprimer un utilisateur
        ttk.Label(frame, text="Supprimer un Utilisateur", font=("Arial", 14, "bold")).grid(row=9, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Utilisateur à supprimer:").grid(row=10, column=0, padx=5, pady=5, sticky="e")
        self.utilisateur_supprimer = ttk.Combobox(frame, values=[u.nom for u in self.gestionnaire.utilisateurs], width=27)
        self.utilisateur_supprimer.grid(row=10, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Supprimer Utilisateur", command=self.supprimer_utilisateur_gui, style="TButton").grid(row=11, column=0, columnspan=2, pady=10)

    def creer_onglet_projets(self):
        """Crée l'onglet pour gérer les projets."""
        frame = ttk.Frame(self.onglet_projets)
        frame.pack(padx=20, pady=20)

        # Section pour ajouter un projet
        ttk.Label(frame, text="Ajouter un Projet", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Nom du projet:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.nom_projet = ttk.Entry(frame, width=30)
        self.nom_projet.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Description:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.description_projet = ttk.Entry(frame, width=30)
        self.description_projet.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Utilisateur:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.utilisateur_projet = ttk.Combobox(frame, values=[u.nom for u in self.gestionnaire.utilisateurs], width=27)
        self.utilisateur_projet.grid(row=3, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Ajouter Projet", command=self.ajouter_projet_gui, style="TButton").grid(row=4, column=0, columnspan=2, pady=10)

        # Section pour modifier un projet
        ttk.Label(frame, text="Modifier un Projet", font=("Arial", 14, "bold")).grid(row=5, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Projet à modifier:").grid(row=6, column=0, padx=5, pady=5, sticky="e")
        self.projet_modifier = ttk.Combobox(frame, values=[p.nom for p in self.gestionnaire.projets], width=27)
        self.projet_modifier.grid(row=6, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Nouveau nom:").grid(row=7, column=0, padx=5, pady=5, sticky="e")
        self.nouveau_nom_projet = ttk.Entry(frame, width=30)
        self.nouveau_nom_projet.grid(row=7, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Nouvelle description:").grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.nouvelle_description_projet = ttk.Entry(frame, width=30)
        self.nouvelle_description_projet.grid(row=8, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Modifier Projet", command=self.modifier_projet_gui, style="TButton").grid(row=9, column=0, columnspan=2, pady=10)

        # Section pour supprimer un projet
        ttk.Label(frame, text="Supprimer un Projet", font=("Arial", 14, "bold")).grid(row=10, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Projet à supprimer:").grid(row=11, column=0, padx=5, pady=5, sticky="e")
        self.projet_supprimer = ttk.Combobox(frame, values=[p.nom for p in self.gestionnaire.projets], width=27)
        self.projet_supprimer.grid(row=11, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Supprimer Projet", command=self.supprimer_projet_gui, style="TButton").grid(row=12, column=0, columnspan=2, pady=10)

    def creer_onglet_taches(self):
        """Crée l'onglet pour gérer les tâches."""
        frame = ttk.Frame(self.onglet_taches)
        frame.pack(padx=20, pady=20)

        # Section pour ajouter une tâche
        ttk.Label(frame, text="Ajouter une Tâche", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Titre:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.titre_tache = ttk.Entry(frame, width=30)
        self.titre_tache.grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Description:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.description_tache = ttk.Entry(frame, width=30)
        self.description_tache.grid(row=2, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Statut:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
        self.statut_tache = ttk.Combobox(frame, values=["à faire", "en cours", "terminé"], width=27)
        self.statut_tache.grid(row=3, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Utilisateur:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
        self.utilisateur_tache = ttk.Combobox(frame, values=[u.nom for u in self.gestionnaire.utilisateurs], width=27)
        self.utilisateur_tache.grid(row=4, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Projet:").grid(row=5, column=0, padx=5, pady=5, sticky="e")
        self.projet_tache = ttk.Combobox(frame, values=[p.nom for p in self.gestionnaire.projets], width=27)
        self.projet_tache.grid(row=5, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Ajouter Tâche", command=self.ajouter_tache_gui, style="TButton").grid(row=6, column=0, columnspan=2, pady=10)

        # Section pour modifier une tâche
        ttk.Label(frame, text="Modifier une Tâche", font=("Arial", 14, "bold")).grid(row=7, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Tâche à modifier:").grid(row=8, column=0, padx=5, pady=5, sticky="e")
        self.tache_modifier = ttk.Combobox(frame, values=[t.titre for p in self.gestionnaire.projets for t in p.taches], width=27)
        self.tache_modifier.grid(row=8, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Nouveau titre:").grid(row=9, column=0, padx=5, pady=5, sticky="e")
        self.nouveau_titre_tache = ttk.Entry(frame, width=30)
        self.nouveau_titre_tache.grid(row=9, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Nouvelle description:").grid(row=10, column=0, padx=5, pady=5, sticky="e")
        self.nouvelle_description_tache = ttk.Entry(frame, width=30)
        self.nouvelle_description_tache.grid(row=10, column=1, padx=5, pady=5)

        ttk.Label(frame, text="Nouveau statut:").grid(row=11, column=0, padx=5, pady=5, sticky="e")
        self.nouveau_statut_tache = ttk.Combobox(frame, values=["à faire", "en cours", "terminé"], width=27)
        self.nouveau_statut_tache.grid(row=11, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Modifier Tâche", command=self.modifier_tache_gui, style="TButton").grid(row=12, column=0, columnspan=2, pady=10)

        # Section pour supprimer une tâche
        ttk.Label(frame, text="Supprimer une Tâche", font=("Arial", 14, "bold")).grid(row=13, column=0, columnspan=2, pady=10)

        ttk.Label(frame, text="Tâche à supprimer:").grid(row=14, column=0, padx=5, pady=5, sticky="e")
        self.tache_supprimer = ttk.Combobox(frame, values=[t.titre for p in self.gestionnaire.projets for t in p.taches], width=27)
        self.tache_supprimer.grid(row=14, column=1, padx=5, pady=5)

        ttk.Button(frame, text="Supprimer Tâche", command=self.supprimer_tache_gui, style="TButton").grid(row=15, column=0, columnspan=2, pady=10)

    def creer_onglet_afficher(self):
        """Crée l'onglet pour afficher les données dans un tableau."""
        frame = ttk.Frame(self.onglet_afficher)
        frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Créer un Treeview avec des colonnes
        self.tree = ttk.Treeview(frame, columns=("Type", "Nom", "Description", "Utilisateur", "Statut"), show="headings")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Utilisateur", text="Utilisateur")
        self.tree.heading("Statut", text="Statut")

        # Ajuster la largeur des colonnes
        self.tree.column("Type", width=100)
        self.tree.column("Nom", width=150)
        self.tree.column("Description", width=200)
        self.tree.column("Utilisateur", width=150)
        self.tree.column("Statut", width=100)

        # Ajouter une barre de défilement
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Afficher le Treeview
        self.tree.pack(fill="both", expand=True)

        # Bouton pour rafraîchir les données
        ttk.Button(frame, text="Rafraîchir", command=self.afficher_donnees).pack(pady=10)

        # Afficher les données initiales
        self.afficher_donnees()

    def ajouter_utilisateur_gui(self):
        """Ajoute un utilisateur via l'interface graphique."""
        nom = self.nom_utilisateur.get()
        email = self.email_utilisateur.get()

        if not nom or not email:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
            return

        utilisateur = Utilisateur(nom, email)
        self.gestionnaire.ajouter_utilisateur(utilisateur)

        # Mettre à jour les combobox
        self.utilisateur_modifier["values"] = [u.nom for u in self.gestionnaire.utilisateurs]
        self.utilisateur_supprimer["values"] = [u.nom for u in self.gestionnaire.utilisateurs]
        self.utilisateur_projet["values"] = [u.nom for u in self.gestionnaire.utilisateurs]
        self.utilisateur_tache["values"] = [u.nom for u in self.gestionnaire.utilisateurs]

        # Effacer les champs
        self.nom_utilisateur.delete(0, tk.END)
        self.email_utilisateur.delete(0, tk.END)

    def modifier_utilisateur_gui(self):
        """Modifie un utilisateur via l'interface graphique."""
        nom_utilisateur = self.utilisateur_modifier.get()
        nouveau_nom = self.nouveau_nom_utilisateur.get()
        nouvel_email = self.nouvel_email_utilisateur.get()

        if not nom_utilisateur:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un utilisateur.")
            return

        self.gestionnaire.modifier_utilisateur(nom_utilisateur, nouveau_nom, nouvel_email)

        # Mettre à jour les combobox
        self.utilisateur_modifier["values"] = [u.nom for u in self.gestionnaire.utilisateurs]
        self.utilisateur_supprimer["values"] = [u.nom for u in self.gestionnaire.utilisateurs]
        self.utilisateur_projet["values"] = [u.nom for u in self.gestionnaire.utilisateurs]
        self.utilisateur_tache["values"] = [u.nom for u in self.gestionnaire.utilisateurs]

        # Effacer les champs
        self.nouveau_nom_utilisateur.delete(0, tk.END)
        self.nouvel_email_utilisateur.delete(0, tk.END)

    def supprimer_utilisateur_gui(self):
        """Supprime un utilisateur via l'interface graphique."""
        nom_utilisateur = self.utilisateur_supprimer.get()

        if not nom_utilisateur:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un utilisateur.")
            return

        self.gestionnaire.supprimer_utilisateur(nom_utilisateur)

        # Mettre à jour les combobox
        self.utilisateur_modifier["values"] = [u.nom for u in self.gestionnaire.utilisateurs]
        self.utilisateur_supprimer["values"] = [u.nom for u in self.gestionnaire.utilisateurs]
        self.utilisateur_projet["values"] = [u.nom for u in self.gestionnaire.utilisateurs]
        self.utilisateur_tache["values"] = [u.nom for u in self.gestionnaire.utilisateurs]

    def ajouter_projet_gui(self):
        """Ajoute un projet via l'interface graphique."""
        nom = self.nom_projet.get()
        description = self.description_projet.get()
        utilisateur_nom = self.utilisateur_projet.get()

        if not nom or not description or not utilisateur_nom:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
            return

        utilisateur = next((u for u in self.gestionnaire.utilisateurs if u.nom == utilisateur_nom), None)
        if not utilisateur:
            messagebox.showwarning("Erreur", "Utilisateur non trouvé.")
            return

        projet = Projet(nom, description, utilisateur)
        self.gestionnaire.ajouter_project(projet)

        # Mettre à jour les combobox
        self.projet_modifier["values"] = [p.nom for p in self.gestionnaire.projets]
        self.projet_supprimer["values"] = [p.nom for p in self.gestionnaire.projets]
        self.projet_tache["values"] = [p.nom for p in self.gestionnaire.projets]

        # Effacer les champs
        self.nom_projet.delete(0, tk.END)
        self.description_projet.delete(0, tk.END)
        self.utilisateur_projet.set("")

    def modifier_projet_gui(self):
        """Modifie un projet via l'interface graphique."""
        nom_projet = self.projet_modifier.get()
        nouveau_nom = self.nouveau_nom_projet.get()
        nouvelle_description = self.nouvelle_description_projet.get()

        if not nom_projet:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un projet.")
            return

        self.gestionnaire.modifier_projet(nom_projet, nouveau_nom, nouvelle_description)

        # Mettre à jour les combobox
        self.projet_modifier["values"] = [p.nom for p in self.gestionnaire.projets]
        self.projet_supprimer["values"] = [p.nom for p in self.gestionnaire.projets]
        self.projet_tache["values"] = [p.nom for p in self.gestionnaire.projets]

        # Effacer les champs
        self.nouveau_nom_projet.delete(0, tk.END)
        self.nouvelle_description_projet.delete(0, tk.END)

    def supprimer_projet_gui(self):
        """Supprime un projet via l'interface graphique."""
        nom_projet = self.projet_supprimer.get()

        if not nom_projet:
            messagebox.showwarning("Erreur", "Veuillez sélectionner un projet.")
            return

        self.gestionnaire.supprimer_projet(nom_projet)

        # Mettre à jour les combobox
        self.projet_modifier["values"] = [p.nom for p in self.gestionnaire.projets]
        self.projet_supprimer["values"] = [p.nom for p in self.gestionnaire.projets]
        self.projet_tache["values"] = [p.nom for p in self.gestionnaire.projets]

    def ajouter_tache_gui(self):
        """Ajoute une tâche via l'interface graphique."""
        titre = self.titre_tache.get()
        description = self.description_tache.get()
        statut = self.statut_tache.get()
        utilisateur_nom = self.utilisateur_tache.get()
        projet_nom = self.projet_tache.get()

        if not titre or not description or not statut or not utilisateur_nom or not projet_nom:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
            return

        utilisateur = next((u for u in self.gestionnaire.utilisateurs if u.nom == utilisateur_nom), None)
        projet = next((p for p in self.gestionnaire.projets if p.nom == projet_nom), None)

        if not utilisateur or not projet:
            messagebox.showwarning("Erreur", "Utilisateur ou projet non trouvé.")
            return

        tache = Tache(titre, description, statut, utilisateur)
        self.gestionnaire.ajouter_tache(projet, tache)

        # Effacer les champs
        self.titre_tache.delete(0, tk.END)
        self.description_tache.delete(0, tk.END)
        self.statut_tache.set("")
        self.utilisateur_tache.set("")
        self.projet_tache.set("")

    def modifier_tache_gui(self):
        """Modifie une tâche via l'interface graphique."""
        titre_tache = self.tache_modifier.get()
        nouveau_titre = self.nouveau_titre_tache.get()
        nouvelle_description = self.nouvelle_description_tache.get()
        nouveau_statut = self.nouveau_statut_tache.get()

        if not titre_tache:
            messagebox.showwarning("Erreur", "Veuillez sélectionner une tâche.")
            return

        self.gestionnaire.modifier_tache(titre_tache, nouveau_titre, nouvelle_description, nouveau_statut)

        # Mettre à jour les combobox
        self.tache_modifier["values"] = [t.titre for p in self.gestionnaire.projets for t in p.taches]
        self.tache_supprimer["values"] = [t.titre for p in self.gestionnaire.projets for t in p.taches]

        # Effacer les champs
        self.nouveau_titre_tache.delete(0, tk.END)
        self.nouvelle_description_tache.delete(0, tk.END)
        self.nouveau_statut_tache.set("")

    def supprimer_tache_gui(self):
        """Supprime une tâche via l'interface graphique."""
        titre_tache = self.tache_supprimer.get()

        if not titre_tache:
            messagebox.showwarning("Erreur", "Veuillez sélectionner une tâche.")
            return

        self.gestionnaire.supprimer_tache(titre_tache)

        # Mettre à jour les combobox
        self.tache_modifier["values"] = [t.titre for p in self.gestionnaire.projets for t in p.taches]
        self.tache_supprimer["values"] = [t.titre for p in self.gestionnaire.projets for t in p.taches]

    def afficher_donnees(self):
        """Affiche les données dans la zone de texte."""
        self.tree.delete(*self.tree.get_children())

        # Afficher les utilisateurs
        for u in self.gestionnaire.utilisateurs:
            self.tree.insert("", "end", values=("Utilisateur", u.nom, u.email, "", ""))

        # Afficher les projets
        for p in self.gestionnaire.projets:
            utilisateur_nom = p.utilisateur.nom if isinstance(p.utilisateur, Utilisateur) else p.utilisateur
            self.tree.insert("", "end", values=("Projet", p.nom, p.description, utilisateur_nom, ""))

            # Afficher les tâches du projet
            for t in p.taches:
                utilisateur_tache_nom = t.utilisateur.nom if isinstance(t.utilisateur, Utilisateur) else t.utilisateur
                self.tree.insert("", "end", values=("Tâche", t.titre, t.description, utilisateur_tache_nom, t.statut))

# Exemple d'utilisation
if __name__ == "__main__":
    gestionnaire = GestionnaireDeProjets()
    app = GestionnaireGUI(gestionnaire)