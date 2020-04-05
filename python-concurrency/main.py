sites = [
    "https://www.seneweb.com/", 
    "https://emedia.sn/", 
    "https://covidsn.com/", 
    "https://xarala.tech/"
] * 15

import multiprocessing
import time
import requests

session = None

def init():
    global session
    if not session:
        session = requests.Session()

def get(url):
    with session.get(url) as response:
        process_name = multiprocessing.current_process().name
        print(f"La processus {process_name} renvoi un contenu de taille {len(response.content)} de l'url {url}")

def get_all(sites):
    with multiprocessing.Pool(initializer=init) as pool:
        pool.map(get, sites)

start = time.time()
get_all(sites)
duration = time.time() - start
print(f"Contenu téléchargé en {duration} s")
