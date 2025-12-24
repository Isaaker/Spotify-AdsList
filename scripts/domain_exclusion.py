# This script checks if the domains of the blocklist-mixed match the domains of the domain_exclusion


print (r"""
   _____             __  _ ____         ___       __        __    _      __ 
  / ___/____  ____  / /_(_) __/_  __   /   | ____/ /____   / /   (_)____/ /_
  \__ \/ __ \/ __ \/ __/ / /_/ / / /  / /| |/ __  / ___/  / /   / / ___/ __/
 ___/ / /_/ / /_/ / /_/ / __/ /_/ /  / ___ / /_/ (__  )  / /___/ (__  ) /_  
/____/ .___/\____/\__/_/_/  \__, /  /_/  |_\__,_/____/  /_____/_/____/\__/  
    /_/                    /____/                                           
""")
print ("License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt")

def load_domains(file_path):
    try:
        with open(file_path, 'r') as file:
            # Read lines, strip whitespace, and convert to lowercase
            return set(line.strip().lower() for line in file if line.strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return set()

def check_whitelist_against_blacklist(whitelist_file, blacklist_file):
    whitelist = load_domains(whitelist_file)
    blacklist = load_domains(blacklist_file)

    # Find common domains
    common_domains = whitelist.intersection(blacklist)

    if common_domains:
        print("The following whitelisted domains are in the blacklist:")
        for domain in common_domains:
            print(f"- {domain}")
            print("Removing from blacklist...")
            # Remove the domain from the blacklist
            blacklist.remove(domain)
        # Write the updated blacklist back to the file
        with open(blacklist_file, 'w') as file:
            for domain in blacklist:
                file.write(f"{domain}\n")
    else:
        print("No whitelisted domains are in the blacklist.")

if __name__ == "__main__":
    try:
        workspace = os.environ.get('GITHUB_WORKSPACE')
        branch = os.environ.get('BRANCH_NAME')
        WHITELIST_FILE = f"{workspace}/{branch}/Lists/DOMAIN_EXCLUSION.txt"
        BLACKLIST_FILE = f"{workspace}/{branch}/Lists/BLACKLIST-mixed.txt"
    else:
        WHITELIST_FILE = "./Lists/DOMAIN_EXCLUSION.txt"
        BLACKLIST_FILE = "./Lists/BLACKLIST-mixed.txt"

    check_whitelist_against_blacklist(WHITELIST_FILE, BLACKLIST_FILE)