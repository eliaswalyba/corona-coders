sites = [
    "https://www.seneweb.com/", 
    "https://emedia.sn/", 
    "https://covidsn.com/", 
    "https://xarala.tech/"
] * 100

import requests # pip install requests
import time

def get(url, session):
    with session.get(url) as response:
        print(f"Taille du contenu = {len(response.content)} - Origin = {url}")

start = time.time()
with requests.Session() as session:
    for site in sites:
        get(site, session)
duration = time.time() - start
print(f"Tout le contenu a pris {duration} pour se téléchager")