# PoroPy
An async python framework for communicating with the Riot API in python. 

Under heavy development so expect major changes in the upcomming time.

# Installation
To install Poro.py:
```
pip install git+https://github.com/Zachy24/poro.py
```
You will also need a RiotGames Api key which can be acquired from [here](https://developer.riotgames.com/)

# Quick Example
```py
from poro import Poro
import asyncio

api_key = "RGAPI-XXXX"

loop = asyncio.get_event_loop()

poro = Poro(api_key, loop=loop)


async def champion_rotations(region):
    return await poro.champion.rotations((region))


async def get_summoner(region, name):
    return await poro.summoner.by_name(region, name)


if __name__ == "__main__":
    region = "euw1"
    username = "SirGhostal"

    # Get the free to play champions in a given region.
    free_champions = loop.run_until_complete(champion_rotations(region))
    print(free_champions)

    # Load up summoner account information by region and username.
    summoner = loop.run_until_complete(get_summoner(region, username))
    print(summoner)
```

# Pipeline
    - Implement handlers to hook up your SQL database and limit the number of API Requests made.
    - Return pythonic objects instead of raw json data. More user friendly...
    - Update endpoints to v4.


# Communication 
For support and communication, feel free to contact us on our discord server:
https://discord.gg/SNNaN2a

