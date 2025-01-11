import matplotlib.pyplot as plt


class CoreManager:
    """
    Classe dédiée à la génération de graphiques.
    """

    def __init__(self, protocols, times):
        """
        Initialisation des données nécessaires pour le graphique.

        :param protocols: Liste des versions de protocoles HTTP (ex. ["HTTP 1.1", "HTTP 2.0", "HTTP 3.0"]).
        :param times: Liste des temps de téléchargement correspondants (en secondes).
        """
        if len(protocols) != len(times):
            raise ValueError("Les listes 'protocols' et 'times' doivent avoir la même longueur.")

        self.protocols = protocols
        self.times = times

    def traceGraph(self, title="Comparaison des performances HTTP", filename=None, colors=None):
        """
        Génère un graphique en barres comparant les performances des protocoles.

        :param title: Titre du graphique.
        :param filename: Nom du fichier pour sauvegarder le graphique (optionnel).
        :param colors: Liste des couleurs pour les barres (optionnel).
        """
        if colors is None:
            colors = ['blue', 'green', 'orange']

        fig, ax = plt.subplots(figsize=(8, 6))

        # Création des barres
        ax.bar(self.protocols, self.times, color=colors, width=0.6)

        # Ajouter des annotations
        for i, time in enumerate(self.times):
            ax.text(i, time + 0.02, f"{time:.2f} s", ha='center', fontsize=10)

        # Personnalisation du graphique
        ax.set_title(title, fontsize=14)
        ax.set_xlabel("Versions HTTP", fontsize=12)
        ax.set_ylabel("Temps de téléchargement (secondes)", fontsize=12)
        ax.set_ylim(0, max(self.times) + 0.2)
        ax.grid(axis='y', linestyle='--', alpha=0.7)

        # Sauvegarde ou affichage du graphique
        if filename:
            plt.savefig(filename, format='png')
            print(f"Graphique sauvegardé sous le nom : {filename}")
        else:
            plt.show()
