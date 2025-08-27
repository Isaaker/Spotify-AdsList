# This script copy the domains to the different adblock formats
print (r"""
   _____             __  _ ____         ___       __        __    _      __ 
  / ___/____  ____  / /_(_) __/_  __   /   | ____/ /____   / /   (_)____/ /_
  \__ \/ __ \/ __ \/ __/ / /_/ / / /  / /| |/ __  / ___/  / /   / / ___/ __/
 ___/ / /_/ / /_/ / /_/ / __/ /_/ /  / ___ / /_/ (__  )  / /___/ (__  ) /_  
/____/ .___/\____/\__/_/_/  \__, /  /_/  |_\__,_/____/  /_____/_/____/\__/  
    /_/                    /____/                                           
""")
print ("License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt")

#Import libraries
import time
from time import gmtime, strftime
import os

# Get the domains to block
workspace = os.environ.get('GITHUB_WORKSPACE')
branch = os.environ.get('BRANCH_NAME')
files_path = f"{workspace}/{branch}/Lists/"
print ("Obtaining the domains to block...")
with open(f"{files_path}/BLACKLIST-mixed.txt", "r") as master_blocklist:
    block_domains = master_blocklist.readlines()

# Generate the new adblock files
print (f"\n")
print ("Generating new adblock files")
print ("----------------------------")

current_time = strftime("%Y-%m-%d", gmtime())
sum_domains = len(block_domains)

#Generate the AdGuard blocklist
print ("Generating the AdGuard file...")
header = f"""#######################################################################################
##### Spotify Ads Blacklist                                                        ####
##### Created by: Isaaker                                                          ####
##### Updated: {current_time} (GMT)                                                    ####
#######################################################################################
##### Version: Adguard                                                             ####
##### Number of domains: {sum_domains}                                                      ####
#######################################################################################
##### Read more: https://github.com/Isaaker/Spotify-AdsList                        ####
##### License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt    ####
#######################################################################################

"""

with open(f"{files_path}/adguard-mixed.txt", "w") as adguard:
    adguard.write(header)
    for domain in block_domains:
        adguard.write(f"||{domain.rstrip()}^\n")


print ("AdGuard files generated")

#Generate the Pi-hole blocklist
print ("Generating the Pi-hole file...")
header = f"""#######################################################################################
##### Spotify Ads Blacklist                                                        ####
##### Created by: Isaaker                                                          ####
##### Updated: {current_time} (GMT)                                                    ####
#######################################################################################
##### Version: pi-hole                                                             ####
##### Number of domains: {sum_domains}                                                      ####
#######################################################################################
##### Read more: https://github.com/Isaaker/Spotify-AdsList                        ####
##### License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt    ####
#######################################################################################

"""

with open(f"{files_path}/pi-hole-mixed.txt", "w") as pihole:
    pihole.write(header)
    for domain in block_domains:
        pihole.write(domain)

print ("Pi-Hole file generated")

#Generate the standard_list blocklist
print ("Generating the Standard list file...")
header = f"""#######################################################################################
##### Spotify Ads Blacklist                                                        ####
##### Created by: Isaaker                                                          ####
##### Updated: {current_time} (GMT)                                                    ####
#######################################################################################
##### Version: Standard                                                            ####
##### Number of domains: {sum_domains}                                                      ####
#######################################################################################
##### Read more: https://github.com/Isaaker/Spotify-AdsList                        ####
##### License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt    ####
#######################################################################################

"""

with open(f"{files_path}/standard_list-mixed.txt", "w") as standard_list:
    standard_list.write(header)
    for domain in block_domains:
        standard_list.write(f"0.0.0.0 {domain}")

print ("Standard list file generated")

#Generate the Dnsmasq blocklist
print ("Generating the Dnsmasq file...")
header = f"""#######################################################################################
##### Spotify Ads Blacklist                                                        ####
##### Created by: Isaaker                                                          ####
##### Updated: {current_time} (GMT)                                                    ####
#######################################################################################
##### Version: dnsmasq                                                             ####
##### Number of domains: {sum_domains}                                                      ####
#######################################################################################
##### Read more: https://github.com/Isaaker/Spotify-AdsList                        ####
##### License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt    ####
#######################################################################################

"""

with open(f"{files_path}/dnsmasq-mixed.txt", "w") as dnsmasq:
    dnsmasq.write(header)
    for domain in block_domains:
        dnsmasq.write(f"server=/{domain.rstrip()}/\n")

print ("Dnsmasq file generated")

#Generate the ABP blocklist
print ("Generating the ABP file...")
header = f"""
[Adblock Plus 7.1]
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!! Spotify Ads Blacklist                                                        !!!!
!!!!! Created by: Isaaker                                                          !!!!
!!!!! Updated: {current_time} (GMT)                                                    !!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!! Version: ABP                                                                 !!!!
!!!!! Number of domains: {sum_domains}                                                      !!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!! Read more: https://github.com/Isaaker/Spotify-AdsList                        !!!!
!!!!! License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt    !!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

"""

with open(f"{files_path}/abp-mixed.txt", "w") as abp:
    abp.write(header)
    for domain in block_domains:
        abp.write(domain)

print ("ABP file generated")

print ("----------------------------")
print ("End of the conversion")
