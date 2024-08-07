# This script copy the domains to the different adblock formats
print ("""
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

# Get the domains to block
time.sleep(1)
print ("Obtaining the domains to block...")
with open("/home/runner/work/Spotify-AdsList/Spotify-AdsList/Developer/Lists/BLACKLIST.txt", "r") as master_blocklist:
    block_domains = master_blocklist.readlines()

# Generate the new adblock files
time.sleep(1)
print (f"\n")
print ("Generating new adblock files")
print ("----------------------------")

current_time = strftime("%Y-%m-%d", gmtime())
sum_domains = len(block_domains)

#Generate the AdGuard blocklist
time.sleep(1)
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

with open("/home/runner/work/Spotify-AdsList/Spotify-AdsList/Developer/Lists/adguard.txt", "w") as adguard:
    adguard.write(header)
    for domain in block_domains:
        adguard.write(f"||{domain.rstrip()}^\n")

print ("AdGuard file generated")

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

with open("/home/runner/work/Spotify-AdsList/Spotify-AdsList/Developer/Lists/pi-hole.txt", "w") as pihole:
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

with open("/home/runner/work/Spotify-AdsList/Spotify-AdsList/Developer/Lists/standard_list.txt", "w") as standard_list:
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

with open("/home/runner/work/Spotify-AdsList/Spotify-AdsList/Developer/Lists/dnsmasq.txt", "w") as dnsmasq:
    dnsmasq.write(header)
    for domain in block_domains:
        dnsmasq.write(f"server=/{domain.rstrip()}/\n")

print ("Dnsmasq file generated")

print ("----------------------------")
print ("End of the conversion")
