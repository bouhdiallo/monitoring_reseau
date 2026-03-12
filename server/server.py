import socket
import threading
import json
from database import insert_metrics  # Fonction pour insérer les données dans la base
from gui import update_graph         # Fonction pour mettre à jour le graphique de l'interface

# Adresse IP et port sur lesquels le serveur écoute
HOST = "0.0.0.0"  # Écoute sur toutes les interfaces réseau disponibles
PORT = 5000       # Port TCP choisi pour la réception des données


#  Gère la communication avec un client unique. Reçoit des données JSON, les insère en base et met à jour le graphique.
def handle_client(conn, addr):

    try:
        # Réception des données du client (taille max 4096 octets)
        data = conn.recv(4096).decode()

        # Conversion des données JSON en dictionnaire Python
        metrics = json.loads(data)

        # Insertion des métriques dans la base de données
        insert_metrics(metrics)

        # Extraction des métriques CPU et mémoire pour mise à jour graphique
        cpu = metrics["cpu"]
        memory = metrics["memory"]
        update_graph(cpu, memory)

        # Affichage d'un message pour indiquer la réception réussie
        print("Data received from", metrics["node"])

    except Exception as e:
        # Gestion des erreurs éventuelles
        print("Error:", e)

    finally:
        # Fermeture de la connexion client
        conn.close()

#  Démarre le serveur TCP qui écoute les clients et crée un thread pour chacun
def start_server():
    
    # Création d'un socket TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Liaison du socket à l'adresse et port définis
    server.bind((HOST, PORT))

    # Écoute jusqu'à 100 connexions simultanées en file d'attente
    server.listen(100)

    print("Server running on port", PORT)

    while True:
        # Acceptation d'une nouvelle connexion
        conn, addr = server.accept()

        # Création d'un thread pour gérer le client
        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr)
        )
        thread.start()


if __name__ == "__main__":
    # Lancement du serveur si ce fichier est exécuté directement
    start_server()