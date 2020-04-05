# Introduction à la concurrence avec des exemples en Python

## Concurrence & Parallelisme

| Type                                 	| Stratégie                                                                     	| Procésseurs 	|
|--------------------------------------	|-------------------------------------------------------------------------------	|-------------	|
| Pre-emptive multitasking (threading) 	| Le système d'exploitation décide quand basculer les tâches externes à Python. 	| 1           	|
| Cooperative multitasking (asyncio)   	| Les tâches décident quand abandonner le contrôle.                             	| 1           	|
| Multiprocessing (multiprocessing)    	| Les processus s'exécutent tous en même temps sur des processeurs différents.  	| Plusieurs   	|


## I/O-Bound / CPU-Bound

| I/O-Bound Process                                                                                                                           	| CPU-Bound Process                                                                       	|
|---------------------------------------------------------------------------------------------------------------------------------------------	|-----------------------------------------------------------------------------------------	|
| Votre programme passe la plupart de son temps à parler à un périphérique lent, comme une connexion réseau, un disque dur ou une imprimante. 	| Votre programme passe la plupart de son temps à effectuer des opérations CPU.           	|
| L'accélérer implique de chevaucher le temps passé à attendre ces appareils.                                                                 	| L'accélérer implique de trouver des moyens de faire plus de calculs dans le même temps. 	|