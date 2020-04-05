sites = [
    "https://www.seneweb.com/", 
    "https://emedia.sn/", 
    "https://covidsn.com/", 
    "https://xarala.tech/"
] * 100

import concurrent.futures
import requests
import threading
import time

thread_local = threading.local() # Ensemble des processus (pas si vrai que ça)

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def get(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Taille du contenu = {len(response.content)} - Source = {url}")

start = time.time()
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    executor.map(get, sites)
duration = time.time() - start
print(f"Contenu télécharger en {duration} secondes")