sites = [
    "https://www.seneweb.com/", 
    "https://emedia.sn/", 
    "https://covidsn.com/", 
    "https://xarala.tech/"
] * 100

import asyncio
import time
import aiohttp


async def get(session, url):
    async with session.get(url) as response:
        print(f"Taille du contenu = {response.status} - Source = {url}")

async def get_all(sites):
    async with aiohttp.ClientSession() as session:
        processes = []
        for site in sites:
            process = asyncio.ensure_future(get(session, site))
            processes.append(process)
        await asyncio.gather(*processes, return_exceptions=True)


start_time = time.time()
asyncio.get_event_loop().run_until_complete(get_all(sites))
duration = time.time() - start_time
print(f"Contenu téléchargé en {duration} s")
