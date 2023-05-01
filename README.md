# Spotify Ads List


## Status:

[![Semgrep](https://github.com/Isaaker/Ghost_Simulator_ES/actions/workflows/semgrep.yml/badge.svg)](https://github.com/Isaaker/Ghost_Simulator_ES/actions/workflows/semgrep.yml)

## About

Spotify Ads List is a list of domains that includes all the domains from which Spotify Apps get audio ads, banners...

Blocking these domains is totally legal since the only thing you are doing is redirecting requests from these domains to 0.0.0.0.0 also known as nowhere.

Making the list cost me a lot of time but finally it seems to work, in case you find any false positive let me know by creating an Issue, also if you want to collaborate I invite you to create a fork of the repository.

I also recommend you to complement the list with some standard lists of ad domains, here are some options:

- https://github.com/blocklistproject/Lists
- https://github.com/topics/blocklist
- https://github.com/topics/adblock
- https://github.com/topics/adblock-list

## Avaible List Versions

The list is highly compatible, so here are the different versions so that you can use it with your Adblock of confidence:

**💡 Suggestion: To download the files use curl, wget... and the Raw URL**
 
| Name | Compatibility | Raw URL | File |
| -- | -- | -- | -- |
| Standard | Highly compatible, no particular system | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/standard_list.txt | https://github.com/Isaaker/Spotify-AdsList/blob/main/Lists/standard_list.txt
| Pi-hole | Compatible with pi-hole and other systems that do not require anything other than domains | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/pi-hole.txt | https://github.com/Isaaker/Spotify-AdsList/blob/main/Lists/pi-hole.txt
| Dnsmasq | Compatible with dnsmasq | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/dnsmasq.txt | https://github.com/Isaaker/Spotify-AdsList/blob/main/Lists/dnsmasq.txt
| Dnsmasq | Compatible with dnsmasq | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/adguard.txt | https://github.com/Isaaker/Spotify-AdsList/blob/main/Lists/adguard.txt

## License
The code is under **Creative Commons Attribution-ShareAlike 4.0 International Public License**, view the license at: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt

![Creative Commons Attribution-ShareAlike 4.0 International Public License Logo]([images/license]
