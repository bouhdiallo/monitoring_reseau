import socket
import threading
import json
import queue
from database import insert_metrics
from gui import update_graph, root  # root = Tk() de gui.py

# Adresse IP et port
HOST = "0.0.0.0"
PORT = 5000

# Queue pour passer les données au thread Tkinter
data_queue = queue.Queue()

# Thread pour gérer un client
def handle_client(conn, addr):
    try:
        data = conn.recv(4096).decode()
        metrics = json.loads(data)
        insert_metrics(metrics)

        # Envoi des données à la queue pour GUI
        data_queue.put(metrics)

        print("Data received from", metrics["node"])

    except Exception as e:
        print("Error:", e)
    finally:
        conn.close()

# Fonction qui met à jour le GUI depuis le thread principal
def gui_update():
    while not data_queue.empty():
        metrics = data_queue.get()
        cpu = metrics["cpu"]
        memory = metrics["memory"]
        update_graph(cpu, memory)
    root.after(1000, gui_update)  # rappel toutes les 1s

# Lancement du serveur
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(100)
    print("Server running on port", PORT)

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

if __name__ == "__main__":
    # Démarrer la mise à jour GUI
    root.after(1000, gui_update)

    # Démarrer le serveur dans un thread séparé pour ne pas bloquer Tkinter
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Lancer Tkinter dans le thread principal
    root.mainloop()