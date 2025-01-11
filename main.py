import time
import requests  # Utilisé pour HTTP 1.1 et 2.0
import httpx  # Nécessaire pour HTTP 2.0
import aiohttp  # Pour le client HTTP 3.0
import asyncio

import urllib3

from core import CoreManager


# Utiliser pour supprimer les avertissements suite à la desactivation du SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Fonction pour mesurer le temps de téléchargement avec HTTP 1.1
def download_http11(url):
    start_time = time.time()
    response = requests.get(url, verify=False)
    elapsed_time = time.time() - start_time

    if response.status_code == 200:
        print(f"HTTP 1.1 - Fichier téléchargé en {elapsed_time:.2f} secondes, taille: {len(response.content)} octets.")
    else:
        print(f"HTTP 1.1 - Échec du téléchargement, code de statut: {response.status_code}")

    return elapsed_time

# Fonction pour mesurer le temps de téléchargement avec HTTP 2.0
def download_http20(url):
    with httpx.Client(http2=True, verify=False) as client:
        start_time = time.time()
        try:
            response = client.get(url)
            elapsed_time = time.time() - start_time

            if response.status_code == 200:
                print(f"HTTP 2.0 - Fichier téléchargé en {elapsed_time:.2f} secondes, taille: {len(response.content)} octets.")
            else:
                print(f"HTTP 2.0 - Échec du téléchargement, code de statut: {response.status_code}")
        except httpx.HTTPError as e:
            print(f"HTTP 2.0 - Erreur lors du téléchargement : {e}")

    return elapsed_time



# Fonction pour mesurer le temps de téléchargement avec HTTP 3.0
async def download_http30(url):
    start_time = time.time()

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        try:
            async with session.get(url) as response:
                content = await response.read()
                elapsed_time = time.time() - start_time
                print(f"HTTP 3.0 - Fichier téléchargé en {elapsed_time:.2f} secondes, taille: {len(content)} octets.")
        except Exception as e:
            print(f"HTTP 3.0 - Échec du téléchargement, erreur: {e}")

    return elapsed_time


if __name__ == "__main__":

    url = "https://www.djamo.com/ci/"

    protocols = ["HTTP 1.1", "HTTP 2.0", "HTTP 3.0"]


    print("\n--- Test avec HTTP 1.1 ---")
    time_http_1 = download_http11(url)

    print("\n--- Test avec HTTP 2.0 ---")
    time_http_2 = download_http20(url)

    print("\n--- Test avec HTTP 3.0 ---")
    time_http_3 = asyncio.run(download_http30(url))

    # Stock des différents temps écoulé pour la construction du graph
    times = [time_http_1, time_http_2, time_http_3]

    graph = CoreManager(protocols,times)
    graph.traceGraph()