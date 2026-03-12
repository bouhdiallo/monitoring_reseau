# monitoring_reseau
Système de surveillance de réseau distribué en Python

## Architecture

Client (Agent) -> TCP Socket -> Server -> Database -> GUI

## Fonctionnalités

- Collecte CPU / RAM / Disk
- Envoi des métriques via TCP
- Serveur multi-thread
- Stockage base de données MySQL
- Graphiques CPU et RAM

## Installation

Installer dépendances :

pip install -r requirements.txt

## Lancer le serveur

cd server
python server.py

## Lancer un client

cd client
python agent.py

## Lancer l'interface graphique

cd server
python gui.py

Fin du projet 
