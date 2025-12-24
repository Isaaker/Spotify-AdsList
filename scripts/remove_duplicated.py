# This script delete duplicated domains
print (r"""
   _____             __  _ ____         ___       __        __    _      __ 
  / ___/____  ____  / /_(_) __/_  __   /   | ____/ /____   / /   (_)____/ /_
  \__ \/ __ \/ __ \/ __/ / /_/ / / /  / /| |/ __  / ___/  / /   / / ___/ __/
 ___/ / /_/ / /_/ / /_/ / __/ /_/ /  / ___ / /_/ (__  )  / /___/ (__  ) /_  
/____/ .___/\____/\__/_/_/  \__, /  /_/  |_\__,_/____/  /_____/_/____/\__/  
    /_/                    /____/                                           
""")
print ("License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt")

import os
try:
    workspace = os.environ.get('GITHUB_WORKSPACE')
    branch = os.environ.get('BRANCH_NAME')
    file = f"{workspace}/{branch}/Lists/BLACKLIST.txt"
except:
    file = f"./Lists/BLACKLIST.txt"

# Open the file and generate a list with that

print ("Obtaining the domains...")
with open(file, "r") as master_blocklist:
    block_domains = master_blocklist.readlines()

# Remove duplicated domains

clean_blocklist = list(set(block_domains))

# Rewrite the file
with open(file, "w") as master_blocklist:
    for domain in clean_blocklist:
        master_blocklist.write(domain)

print ("Duplicated lines deleted sucesfully")
