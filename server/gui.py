
# Ce module crée une interface graphique permettant
# d'afficher en temps réel les métriques CPU et mémoire
# envoyées par les agents du système de supervision.
#
# L'interface utilise Tkinter pour la fenêtre graphique
# et Matplotlib pour afficher les graphiques.



# Importation de la bibliothèque Tkinter pour créer l'interface graphique
import tkinter as tk

# Importation du composant permettant d'intégrer un graphique Matplotlib dans Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Importation de l'objet Figure utilisé pour créer les graphiques
from matplotlib.figure import Figure


# Liste utilisée pour stocker l'historique des valeurs CPU
cpu_data = []

# Liste utilisée pour stocker l'historique des valeurs de mémoire RAM
mem_data = []


# Création de la fenêtre principale de l'application
root = tk.Tk()

# Définition du titre de la fenêtre
root.title("Dashboard pour le monitorer le reseau")


# Création d'une figure Matplotlib avec une taille spécifique
figure = Figure(figsize=(6,4))

# Ajout d'une zone de graphique (subplot) dans la figure
# 111 signifie : 1 ligne, 1 colonne, premier graphique
ax = figure.add_subplot(111)


# Intégration du graphique Matplotlib dans la fenêtre Tkinter
canvas = FigureCanvasTkAgg(figure, root)

# Affichage du graphique dans la fenêtre
canvas.get_tk_widget().pack()


# Création d'un label indiquant l'état du serveur de monitoring
status = tk.Label(
    root,
    text="Server monitoring running",
    font=("Arial",12)
)

# Affichage du label dans la fenêtre
status.pack()


# Cette fonction met à jour le graphique avec les nouvelles
# valeurs CPU et mémoire reçues du serveur.
def update_graph(cpu, mem):

    # Ajout de la nouvelle valeur CPU dans la liste
    cpu_data.append(cpu)

    # Ajout de la nouvelle valeur mémoire dans la liste
    mem_data.append(mem)

    # Limitation de l'historique des données à 20 valeurs
    # afin d'éviter que la liste devienne trop grande
    if len(cpu_data) > 20:

        # Suppression de la première valeur (la plus ancienne)
        cpu_data.pop(0)

        # Suppression de la première valeur mémoire
        mem_data.pop(0)


    # Effacement du graphique actuel
    ax.clear()

    # Dessin de la courbe CPU
    ax.plot(cpu_data, label="CPU %")

    # Dessin de la courbe mémoire
    ax.plot(mem_data, label="Memory %")

    # Affichage de la légende du graphique
    ax.legend()

    # Rafraîchissement du graphique dans l'interface
    canvas.draw()


# Cette fonction lance l'interface graphique
# et démarre la boucle principale de Tkinter.
def start_gui():

    # Lancement de la boucle principale de l'interface graphique
    root.mainloop()