import socket
import json
import threading
import random
import time

HOST = "127.0.0.1"
PORT = 5000

def simulate_client(node_id):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))

        # Générer des métriques aléatoires
        metrics = {
            "node": f"client_{node_id}",
            "cpu": random.randint(0, 100),
            "memory": random.randint(0, 100)
        }

        data = json.dumps(metrics).encode()
        client_socket.sendall(data)
        client_socket.close()
        print(f"Client {node_id} sent data.")

    except Exception as e:
        print(f"Client {node_id} error:", e)

# Fonction pour lancer N clients en parallèle
def launch_clients(n):
    threads = []
    for i in range(1, n+1):
        t = threading.Thread(target=simulate_client, args=(i,))
        threads.append(t)
        t.start()
        time.sleep(0.05)  # léger délai pour ne pas saturer instantanément

    for t in threads:
        t.join()

if __name__ == "__main__":
    n_clients = int(input("Nombre de clients à simuler : "))
    launch_clients(n_clients)