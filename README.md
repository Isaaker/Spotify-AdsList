# Spotify Ads List

![Spotify-AdsList Logo](https://github.com/Isaaker/Spotify-AdsList/raw/main/docs/images/spotify_ads_list_logo.png)

## Workflows

|Name|Type|Status|
|--|--|--|
|Build Blocklist|Build|[![Build Blocklist](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/build_blocklist.yml/badge.svg)](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/build_blocklist.yml)|
|Deploy Mkdocs|Deploy|[![Deploy Mkdocs](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/deploy_gh-pages.yml/badge.svg)](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/deploy_gh-pages.yml)
|SAST GitLeaks|Security|[![SAST GitLeaks](https://github.com/Isaaker/piscinadeentropia/actions/workflows/sast-gitleaks.yml/badge.svg)](https://github.com/Isaaker/piscinadeentropia/actions/workflows/sast-gitleaks.yml)|
|SAST Semgrep|Security|[![SAST Semgrep](https://github.com/Isaaker/Ghost_Simulator_ES/actions/workflows/semgrep.yml/badge.svg)](https://github.com/Isaaker/Ghost_Simulator_ES/actions/workflows/semgrep.yml)|

## About

![maintained - yes](https://img.shields.io/badge/maintained-yes-blue)[![Contributions - Welcome](https://img.shields.io/badge/contributions-welcome-blue)](https://spotify.piscinadeentropia.es/docs_contributing/)

Spotify Ads List is a list of domains that includes all the domains from which Spotify Apps get audio ads, banners...

Blocking these domains is totally legal since the only thing you are doing is redirecting requests from these domains to 0.0.0.0 also known as nowhere.

Making the list cost me a lot of time but finally it seems to work, in case you find any false positive let me know by creating an Issue, also if you want to collaborate I invite you to create a fork of the repository.

I also recommend you to complement the list with some standard lists of ad domains, here are some options:

- https://github.com/blocklistproject/Lists
- https://github.com/topics/blocklist
- https://github.com/topics/adblock
- https://github.com/topics/adblock-list

**[Learn more about Spotify Ads List](https://spotify.piscinadeentropia.es)**

**[Now if you have questions you can ask throught Discussions 💬](https://github.com/Isaaker/Spotify-AdsList/discussions)**

## Installation

**To install, please [read our installation tutorial](https://spotify.piscinadeentropia.es/installation)**

## List Versions

The list is highly compatible, so here are the different versions so that you can use it with your Adblock of confidence:

**💡 Suggestion: To download the files use curl, wget... and the Raw URL**
 
| Name | Compatibility | Raw URL | Raw URL+ADS | File |
| -- | -- | -- | -- | -- |
| Standard | Highly compatible, no particular system | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/standard_list.txt | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/standard_list-mixed.txt | https://github.com/Isaaker/Spotify-AdsList/blob/main/Lists/standard_list.txt |
| Pi-hole | Compatible with pi-hole and other systems that do not require anything other than domains | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/pi-hole.txt | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/pi-hole-mixed.txt | https://github.com/Isaaker/Spotify-AdsList/blob/main/Lists/pi-hole.txt |
| Dnsmasq | Compatible with dnsmasq | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/dnsmasq.txt | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/dnsmasq-mixed.txt | https://github.com/Isaaker/Spotify-AdsList/blob/main/Lists/dnsmasq.txt |
| Adguard | Compatible with adguard & uBlock Origin | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/adguard.txt | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/adguard-mixed.txt | https://github.com/Isaaker/Spotify-AdsList/blob/main/Lists/adguard.txt |
| ABP | Compatible with AdBlock Plus | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/abp.txt | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/abp-mixed.txt | https://github.com/Isaaker/Spotify-AdsList/blob/main/Lists/abp.txt |

**To suscribe with uBlock Origin read the installation documentation -> [Add to uBlock](https://spotify.piscinadeentropia.es/installation)**

**To suscribe with ABP you can use -> [this link](https://subscribe.adblockplus.org/?location=https%3A%2F%2Fraw.githubusercontent.com%2FIsaaker%2FSpotify-AdsList%2Fmain%2FLists%2Fabp.txt&title=SpotifyAdsList)**


## Whitelist

In order for Spotify to function properly, a short list of domains needs to be added to its whitelist to prevent redirects from blocked to non-blocked domains from being cut off.

See the Whitelist [here](https://github.com/Isaaker/Spotify-AdsList/blob/main/Lists/WHITELIST.md)

## Testing

Here you can find all the tests made, their date and more details.

| Platform | Device | OS & Version | Browser & Version (If applicable) | Date | Status | List Type | Reported by |
| -- | -- | -- | -- | -- | -- | -- | -- |
| Web App | Mac | MacOS (14.2.1) | Safari (17.2.1) | 27/1/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | pihole | @isaaker |
| Web App | Mac | MacOS (14.2.1) | Firefox (122.0) | 27/1/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | pihole | @isaaker |
| Web App | Virtual Machine| Debian 12 | Firefox ESR (115.3.0esr)| 27/1/24 | ![Static Badge](https://img.shields.io/badge/Status-ERROR-red?logo=spotify) | pihole | @isaaker |
| Web App | Virtual Machine | Debian 12 | Chromium (121.0.6167.85)| 27/1/24 | ![Static Badge](https://img.shields.io/badge/Status-ERROR-red?logo=spotify) | pihole | @isaaker |
| App | Mac | MacOS (14.5) | - | 4/7/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | pihole | @isaaker |
| App | iPhone | iOS (17.5.1) | - | 4/7/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | pihole | @isaaker |
| App | Google Pixel 4a | Android 13 | - | 20/4/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | adguard | @mfjt |
| App | Linux Laptop | Fedora Workstation 40 | - | 22/4/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | adguard | @SudoVanilla |
| App | Mac | MacOS (14.5) | - | 23/6/24 | ![Static Badge](https://img.shields.io/badge/Status-Unknow-yellow?logo=spotify) | adguard | @y2kviv |
| App | Mi 9T | LineageOS 21 | - | 26/6/24 | ![Static Badge](https://img.shields.io/badge/Status-ERROR-red?logo=spotify) | pihole | @MW-SAND |
| App | Windows Laptop | Windows 11 (10.0.22631) | - | 26/6/24 | ![Static Badge](https://img.shields.io/badge/Status-ERROR-red?logo=spotify) | pihole | @MW-SAND |
| Web App | Windows Computer | Windows (22H2 19045.4170) | Chrome (126.0.6478.127 (64 bits)) | 29/6/24 | ![Static Badge](https://img.shields.io/badge/Status-ERROR-red?logo=spotify) | ublock origin | @AlkBek |

**If you have tested the list, please create a issue with type "Testing" to add more tested devices. [Add new tested device](https://github.com/Isaaker/Spotify-AdsList/issues/new?assignees=&labels=Testing&projects=&template=testing.yml&title=New+Testing+Device%3A+%5BDevice+Name%5D+%2F+%5BDevice+OS%26Version%5D)**

## License
The code is under **Creative Commons Attribution-ShareAlike 4.0 International Public License**, view the [license here](https://spotify.piscinadeentropia.es/license)

![Creative Commons Attribution-ShareAlike 4.0 International Public License Logo](https://github.com/Isaaker/Spotify-AdsList/raw/main/docs/images/License-Image.jpeg)

## Contributing

To learn more about how to contribute to this repository, I recommend you read [CONTRIBUTING.md](https://spotify.piscinadeentropia.es/contributing)
