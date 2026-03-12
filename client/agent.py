# Importation des bibliothéques necessaires au bon fonctionnement de mon projet
import socket
import json
import time
import psutil
import platform


# Adresse IP du serveur de supervision auquel l'agent doit envoyer les métriques
SERVER_IP = "127.0.0.1"

# Port réseau utilisé par le serveur pour écouter les connexions des agents
SERVER_PORT = 5000

# Identifiant unique du nœud (machine) récupéré automatiquement grâce au nom de la machine
NODE_ID = platform.node()


# Définition de la fonction collect_metrics qui collecte toutes les métriques système de la machine 
def collect_metrics():

    # Récupération du pourcentage d'utilisation du CPU (interval=1 signifie que la mesure est calculée sur 1 seconde)
    cpu = psutil.cpu_percent(interval=1)

    # Récupération du pourcentage de mémoire RAM utilisée
    memory = psutil.virtual_memory().percent

    # Récupération du pourcentage d'utilisation du disque
    disk = psutil.disk_usage('/').percent

    # Calcul du temps de fonctionnement de la machine (uptime)
    # On soustrait le temps de démarrage du système au temps actuel
    uptime = int(time.time() - psutil.boot_time())

    # Dictionnaire représentant l'état de certains services(les valeurs sont similés)
    services = {

        "http": "OK",

        "ssh": "OK",

        "ftp": "OFF",

        "chrome": "ON",

        "firefox": "ON",

        "vlc": "OFF"
    }

    # Dictionnaire représentant l'état de certains ports réseau
    ports = {

        "22": "OPEN",

        "80": "OPEN",

        "443": "OPEN",

        "3306": "CLOSED"
    }

    # Création d'un dictionnaire contenant toutes les métriques collectées
    data = {

        "node": NODE_ID,

        "os": platform.system(),

        "cpu": cpu,

        "memory": memory,

        "disk": disk,

        "uptime": uptime,

        "services": services,

        "ports": ports,

        "timestamp": time.time()
    }

    # Retourner les métriques collectées
    return data


# Définition de la fonction send_data qui est responsable  de l'envoi des métriques au serveur de supervision
def send_data():

    # Boucle infinie permettant d'envoyer les données
    # périodiquement au serveur
    while True:

        # Bloc try pour gérer les erreurs de connexion réseau
        try:

            # Appel de la fonction collect_metrics pour récupérer les données système
            metrics = collect_metrics()

            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            client.connect((SERVER_IP, SERVER_PORT))

            message = json.dumps(metrics)

            client.send(message.encode())

            client.close()

            print("Metrics sent:", metrics)

        # Gestion des erreurs si la connexion échoue
        except Exception as e:

            # Affichage du message d'erreur
            print("Connection error:", e)

        # Pause de 5 secondes avant la prochaine collecte et envoi
        time.sleep(5)

# Cette condition permet d'exécuter la fonction send_data
if __name__ == "__main__":

    # Lancement de l'agent de monitoring
    send_data()