# This script adds a default blocklist to the actual one with generic ad domains


### DOES NOT WORK - STILL UNDER DEVELOPMENT ###


print ("""
   _____             __  _ ____         ___       __        __    _      __ 
  / ___/____  ____  / /_(_) __/_  __   /   | ____/ /____   / /   (_)____/ /_
  \__ \/ __ \/ __ \/ __/ / /_/ / / /  / /| |/ __  / ___/  / /   / / ___/ __/
 ___/ / /_/ / /_/ / /_/ / __/ /_/ /  / ___ / /_/ (__  )  / /___/ (__  ) /_  
/____/ .___/\____/\__/_/_/  \__, /  /_/  |_\__,_/____/  /_____/_/____/\__/  
    /_/                    /____/                                           
""")
print ("License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt")

import os
import requests
workspace = os.environ.get('GITHUB_WORKSPACE')
branch = os.environ.get('BRANCH_NAME')
file = f"{workspace}/{branch}/Lists/BLACKLIST-mixed.txt"
blocklist = f"{workspace}/{branch}/Lists/BLACKLIST.txt"
default_blocklist = f"{workspace}/{branch}/Lists/default_ad_blocklist.txt"

# Download ads default list from The Blocklist Project

print ("Downloading default blocklist...")
default_blocklist_url = "https://blocklistproject.github.io/Lists/alt-version/ads-nl.txt"
response = requests.get(default_blocklist_url)

if response.status_code == 200:
    # Abrir un archivo en modo de escritura binaria
    with open(default_blocklist, 'wb') as default_blocklist_write:
        default_blocklist_write.write(response.content)
    print("Sucesfully downloaded")
else:
    print(f"Error downloading file")
    exit(1)

with open(file, 'wb') as file_write:
    with open(blocklist, "r") as blocklist_1:
        master_blocklist = blocklist_1.readlines()
    with open(blocklist, "r") as blocklist_1:
        master_blocklist = blocklist_1.readlines()

print ("Duplicated lines deleted sucesfully")