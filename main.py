import time
import requests  # Utilisé pour HTTP 1.1 et 2.0
import httpx  # Nécessaire pour HTTP 2.0
import aiohttp  # Pour le client HTTP 3.0
import asyncio
from bs4 import BeautifulSoup
import urllib3
from core import CoreManager


# Utiliser pour supprimer les avertissements suite à la desactivation du SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Extraction de tout les liens d'une page
def get_all_links(url):
    try:
        response = requests.get(url, verify=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        # Filtrer pour les URLs absolues et éviter les répétitions
        links = list(set([link if link.startswith('http') else url + link for link in links]))
        return links
    except Exception as e:
        print(f"Erreur lors de l'extraction des liens : {e}")
        return []


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
    elapsed_time = 0
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
    elapsed_time = 0

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        try:
            async with session.get(url) as response:
                content = await response.read()
                elapsed_time = time.time() - start_time
                print(f"HTTP 3.0 - Fichier téléchargé en {elapsed_time:.2f} secondes, taille: {len(content)} octets.")
        except Exception as e:
            print(f"HTTP 3.0 - Échec du téléchargement, erreur: {e}")

    return elapsed_time

async def measure_http30_performance(links):
    tasks = [download_http30(link) for link in links]
    return await asyncio.gather(*tasks)

# Fonction principale pour mesurer les performances pour toutes les pages
def measure_performance(url):
    links = get_all_links(url)
    if not links:
        print("Aucun lien trouvé.")
        return

    print("\n--- Test avec HTTP 1.1 ---")
    total_time_http1 = sum(download_http11(link) for link in links)

    print("\n--- Test avec HTTP 2.0 ---")
    total_time_http2 = sum(download_http20(link) for link in links)

    print("\n--- Test avec HTTP 3.0 ---")
    try:
        total_time_http3_list = asyncio.run(measure_http30_performance(links))
        total_time_http3 = sum(total_time_http3_list)
    except Exception as e:
        print(f"Erreur avec HTTP 3.0 : {e}")
        total_time_http3 = float('inf')

    # Résultats globaux
    print("\nRésultats globaux :")
    print(f"Temps total avec HTTP 1.1 : {total_time_http1:.2f} secondes")
    print(f"Temps total avec HTTP 2.0 : {total_time_http2:.2f} secondes")
    print(f"Temps total avec HTTP 3.0 : {total_time_http3:.2f} secondes")

    return [total_time_http1, total_time_http2, total_time_http3]

if __name__ == "__main__":

    url = "https://www.djamo.com/ci/"
    timers = measure_performance(url)

    protocols = ["HTTP 1.1", "HTTP 2.0", "HTTP 3.0"]

    graph = CoreManager(protocols,timers)
    #graph.traceGraph()