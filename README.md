# Spotify Ads List

![Spotify-AdsList Logo](https://github.com/Isaaker/Spotify-AdsList/raw/main/docs/images/spotify_ads_list_logo.png)

## ℹ️ Project Archived

Thank you to everyone who used, tested, reported issues, and contributed to this project.

This repository has been archived and is no longer actively maintained. Archive date: March 30, 2026.

What this means

- The repository is read-only: new issues and pull requests will not be accepted.
- The website and repository will remain publicly accessible for an indefinite period, but availability is not guaranteed.
- All repository contents and associated materials remain under the same license: **Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)**.
- No license changes are allowed under any circumstances.
- Per the license terms, changes to the project are not permitted; any redistribution must preserve the project as-is, include the same license, and provide attribution.

Maintainers, transfers, and contributor access

- Repository ownership will remain with me (Isaaker). I will not transfer ownership.
- If you wish to assume maintenance responsibilities, you may be added as a collaborator with write access; however, repository ownership will remain mine.
- To request collaborator access, email isaaker@piscinadeentropia.es with:
  1. Your GitHub username or organization.
  2. A brief plan for maintenance (scope and frequency).
  3. Any relevant contact or verification info.
- Requests are reviewed in order received; response time may be up to two weeks.
- Adding a collaborator does not imply transfer of ownership or the right to change the license.

Support and reporting

- For critical security issues, email isaaker@piscinadeentropia.es and include “SECURITY” in the subject line.
- For questions or archival-related requests (e.g., build artifacts, archives, or historical data), email the same address.

Additional notes

- CI, deployment hooks, and automated services have been disabled; builds or live demos may no longer run.
- Package registry entries, third-party services, or external integrations referenced by the project may be removed or break over time.
- The project’s issue history, pull requests, and discussions remain as a historical record but will not be acted upon.

License and attribution

- License: **Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)** — no changes permitted.
- Redistribution must preserve the license, the content as-is, and provide attribution to the original author.

Contact

- Maintainer: Isaaker
- Email: isaaker@piscinadeentropia.es

## Workflows

|Name|Type|Status|
|--|--|--|
|Build Blocklist|Build|[![Build Blocklist](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/build_blocklist.yml/badge.svg)](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/build_blocklist.yml)|
|Deploy Mkdocs|Deploy|[![MkDocs Deploy Cloudflare](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/deploy_cloudflare.yml/badge.svg)](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/deploy_cloudflare.yml)|
|SAST GitLeaks|Security|[![SAST GitLeaks](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/sast-gitleaks.yml/badge.svg)](https://github.com/Isaaker/piscinadeentropia/actions/workflows/sast-gitleaks.yml)|
|SAST Semgrep|Security|[![SAST Semgrep](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/sast-semgrep.yml/badge.svg)](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/sast-semgrep.yml)|
|Dependabot|Security|[![Dependabot Updates](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/dependabot/dependabot-updates/badge.svg)](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/dependabot/dependabot-updates)|
|CodeQL|Security|[![CodeQL Advanced](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/codeql.yml/badge.svg)](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/codeql.yml)|
|Bandit|Security|[![Bandit](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/bandit.yml/badge.svg)](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/bandit.yml)|
|Automatic Dependency Submission|Security|[![Automatic Dependency Submission](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/dependency-graph/auto-submission/badge.svg)](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/dependency-graph/auto-submission)|
| Mark stale issues and pull requests | Repo Managament |[![Mark stale issues and pull requests](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/stale.yml/badge.svg)](https://github.com/Isaaker/Spotify-AdsList/actions/workflows/stale.yml)|

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

**[Now if you have questions you can ask through Discussions 💬](https://github.com/Isaaker/Spotify-AdsList/discussions)**

## Installation

<a href="https://spotify.piscinadeentropia.es/docs_interactive_install"><img src="https://github.com/user-attachments/assets/09664079-daee-4abd-a58b-3283b978ce92"></img></a>


**To install, you can also [read our installation tutorial](https://spotify.piscinadeentropia.es/installation)**

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

See the Whitelist [here](https://spotify.piscinadeentropia.es/docs_whitelist/)

## Testing

Here you can find all the tests made, their date and more details.

| Platform | Device | OS & Version | Browser & Version (If applicable) | Date | Status | List Type | Reported by |
| -- | -- | -- | -- | -- | -- | -- | -- |
| Web App | Mac | MacOS (14.2.1) | Safari (17.2.1) | 27/1/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | pihole | @isaaker |
| Web App | Mac | MacOS (14.2.1) | Firefox (122.0) | 27/1/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | pihole | @isaaker |
| App | Virtual Machine| Debian 13 | - | 18/12/25 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | adguard | @isaaker |
| App | Mac | MacOS (14.5) | - | 4/7/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | pihole | @isaaker |
| App | iPhone | iOS (17.5.1) | - | 4/7/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | pihole | @isaaker |
| App | Google Pixel 4a | Android 13 | - | 20/4/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | adguard | @mfjt |
| App | Linux Laptop | Fedora Workstation 40 | - | 22/4/24 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | adguard | @SudoVanilla |
| App | Mac | MacOS (14.5) | - | 23/6/24 | ![Static Badge](https://img.shields.io/badge/Status-Unknow-yellow?logo=spotify) | adguard | @y2kviv |
| App | Mi 9T | LineageOS 21 | - | 26/6/24 | ![Static Badge](https://img.shields.io/badge/Status-ERROR-red?logo=spotify) | pihole | @MW-SAND |
| App | Windows Laptop | Windows 11 (10.0.22631) | - | 26/6/24 | ![Static Badge](https://img.shields.io/badge/Status-ERROR-red?logo=spotify) | pihole | @MW-SAND |
| Web App | Windows Computer | Windows (22H2 19045.4170) | Chrome (126.0.6478.127 (64 bits)) | 29/6/24 | ![Static Badge](https://img.shields.io/badge/Status-ERROR-red?logo=spotify) | ublock origin | @AlkBek |
| App | Desktop | Manjaro Zetar 25.0.10 | - | 03/11/2025 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | Adguard | @Dashboy1998 |
| App | 1+9 Pro | Android 14 | - | 10/12/2025 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | Standard (DNSNet) | @BedBug2479 |
| Other | Cloudflare | N/A | - | 15/12/25 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | Standard (With pihole or firewall via Cloudflare) | @n0w33d |
| App | Linux desktop x86_64 | Linux 6.6.121, EndeavourOS, GNOME 49 | - | 21/01/2026 | ![Static Badge](https://img.shields.io/badge/Status-OK-green?logo=spotify) | pihole | @duartemtorres |

**If you have tested the list, please create a issue with type "Testing" to add more tested devices. [Add new tested device](https://github.com/Isaaker/Spotify-AdsList/issues/new?assignees=&labels=Testing&projects=&template=testing.yml&title=New+Testing+Device%3A+%5BDevice+Name%5D+%2F+%5BDevice+OS%26Version%5D)**

## License
The code is under **Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International**, view the [license here](https://spotify.piscinadeentropia.es/docs_license/)

You are free to:

- **Share** — copy and redistribute the material in any medium or format.  
  The licensor cannot revoke these freedoms as long as you follow the license terms.

Under the following terms:

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
- **NonCommercial** — You may not use the material for commercial purposes.
- **NoDerivatives** — If you remix, transform, or build upon the material, you may not distribute the modified material.
- **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.


## Contributing

To learn more about how to contribute to this repository, I recommend you read [CONTRIBUTING.md](https://spotify.piscinadeentropia.es/contributing)
