# Ce module permet de surveiller l'état des machines (nodes) dans le systeme de supervision reseau
#
# Il vérifie régulièrement si une machine envoie toujours
# ses métriques. Si une machine ne répond plus pendant un
# certain temps, une alerte est affichée.


# Importation du module time pour gérer le temps et calculer les intervalles entre les messages des agents
import time


# Dictionnaire qui stocke le dernier moment où chaque

nodes_last_seen = {}


# Temps maximum (en secondes) avant de considérer qu'une machine est hors ligne (DOWN)
TIMEOUT = 90



# Cette fonction est appelée chaque fois qu'un agent envoie
# des métriques au serveur.
#
# Elle met à jour le temps du dernier message reçu pour la machine concernée.

def update_node(node):

    # Enregistrer le moment actuel comme dernier contact de la machine
    nodes_last_seen[node] = time.time()


# Cette fonction vérifie en continu si les machines
# envoient toujours leurs métriques.
#
# Si une machine ne répond pas pendant plus de TIMEOUT
# secondes, une alerte est affichée.

def check_nodes():

    # Boucle infinie pour vérifier les machines en permanence
    while True:

        # Récupération du temps actuel
        now = time.time()

        # Parcours de toutes les machines enregistrées
        for node in nodes_last_seen:

            # Vérifier si le temps écoulé depuis le dernier
            # message dépasse le TIMEOUT
            if now - nodes_last_seen[node] > TIMEOUT:

                # Affichage d'une alerte indiquant que
                # la machine ne répond plus
                print("ALERT:", node, "is DOWN")

        # Pause de 10 secondes avant la prochaine vérification
        time.sleep(10)