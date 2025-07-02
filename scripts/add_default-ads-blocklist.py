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
import subprocess

result = subprocess.run(["pwd"], capture_output=True, text=True)
current_directory = result.stdout.strip()

if "/home/runner/" in current_directory:
    workspace = os.environ.get('GITHUB_WORKSPACE')
    branch = os.environ.get('BRANCH_NAME')
    file = f"{workspace}/{branch}/Lists/BLACKLIST-mixed.txt"
    blocklist = f"{workspace}/{branch}/Lists/BLACKLIST.txt"
    default_blocklist = f"{workspace}/{branch}/Lists/default_ad_blocklist.txt"
else:
    file = f"{current_directory}/Lists/BLACKLIST-mixed.txt"
    blocklist = f"{current_directory}/Lists/BLACKLIST.txt"
    default_blocklist = f"{current_directory}/Lists/default_ad_blocklist.txt"


# Download ads default list from The Blocklist Project


print("Downloading default blocklist...")
default_blocklist_url = "https://blocklistproject.github.io/Lists/alt-version/ads-nl.txt"
response = requests.get(default_blocklist_url)

if response.status_code == 200:
    with open(default_blocklist, 'wb') as default_blocklist_write:
        default_blocklist_write.write(response.content)
    print("Successfully downloaded")
else:
    print("Error downloading file")
    exit(1)

# Clean comments on the default blocklist file
print("Cleaning comments from the default blocklist...")
with open(default_blocklist, "r") as default_blocklist_read:
    default_blocklist_lines = [
        line.strip() for line in default_blocklist_read
        if line.strip() and not line.startswith("#") and not line.startswith("!")
    ]

with open(default_blocklist, "w") as default_blocklist_write:
    for line in default_blocklist_lines:
        default_blocklist_write.write(line + "\n")

# Leer ambas listas (la principal y la descargada)
with open(blocklist, "r") as blocklist_1:
    master_blocklist = set(line.strip() for line in blocklist_1 if line.strip())

with open(default_blocklist, "r") as default_blocklist_1:
    default_blocklist_lines = set(line.strip() for line in default_blocklist_1 if line.strip())

# Unir ambas listas y eliminar duplicados
combined_blocklist = sorted(master_blocklist.union(default_blocklist_lines))

# Guardar la lista combinada en el archivo mixto
with open(file, 'w') as file_write:
    for line in combined_blocklist:
        file_write.write(line + "\n")

print("Default blocklist added successfully")

