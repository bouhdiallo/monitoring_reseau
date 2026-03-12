# ============================================================
# Module : database.py
# ============================================================
# Ce fichier gère la connexion à la base de données MySQL
# et l'enregistrement des métriques envoyées par les agents
# du système de supervision réseau.
# ============================================================


# Importation du bibliothèque permettant à Python de se connecter à une base MySQL 
import mysql.connector


# Cette fonction permet d'établir une connexion avec la base de données "supervision"
def get_connection():

    # Création de la connexion à la base de données
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="supervision"
    )

    # Retourne l'objet de connexion
    return connection



# Cette fonction permet d'insérer les métriques d'une machine dans la table "nodes".
#
# Le paramètre "data" contient les informations envoyées par l'agent (CPU, mémoire, disque, uptime, etc.).
def insert_metrics(data):

    # Création d'une connexion à la base de données 
    conn = get_connection()

    # Création d'un curseur permettant d'exécuter des requêtes SQL
    cursor = conn.cursor()

    # Requête SQL permettant d'insérer les données dans la table nodes
    query = """
    INSERT INTO nodes (node_name, os, cpu, memory, disk, uptime)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    # Création d'un tuple contenant les valeurs (provenant du dictionnaire "data") à insérer
    values = (
        data["node"],     
        data["os"],       
        data["cpu"],    
        data["memory"],   
        data["disk"],     
        data["uptime"]    
    )

    # Exécution de la requête SQL avec les valeurs
    cursor.execute(query, values)

    # Validation de l'insertion dans la base de données
    conn.commit()

    # Fermeture du curseur pour libérer les ressources
    cursor.close()

    # Fermeture de la connexion à la base de données
    conn.close()