# Spotify Ads List Tutorial

![Spotify Block Tutorial Logo](../images/tutorial.gif)

Spotify Ads List is quick and easy to install, all you need is a compatible adblocker, an internet connection and the Spotify website or app.

To install Spotify Ads List you can follow this steps:

## 1. Check compatibility

Spotify Ads List is compatible with all major ad blockers, both open-source and paid.

The currently supported adblockers are:
- Standard (Compatible with multiple adblockers and can also be used with the hosts file.)
- [Pi-Hole](https://pi-hole.net)
- [Dnsmasq](https://dnsmasq.org/doc.html)
- [Adguard](https://adguard.com/es/welcome.html)
- [uBlock Origin](https://ublockorigin.com)

**Being a simple and very backward compatible list, if your adblocker is not included above, you can ask us to include it and if necessary to generate a custom list layout for it.**

## 2. Find the right list format

Spotify Ads List is available in diferents formats to make it compatible with all the adblockers listed in the step 1. 

Here is a table to find the right format for your adblcoker:

| Adblocker | List Format |
| -- | -- |
| Pi-Hole | Pi-hole	|
| Dnsmasq | Dnsmasq |
| Adguard | Adguard |
| uBlock Origin | Adguard |
| Standard (with hosts file or adblockers that supports 0.0.0.0 entry) | Standard |

**Being a simple and very backward compatible list, if your adblocker is not included above, you can ask us to include it and if necessary to generate a custom list layout for it.**

## 3. (Optional) Setup your adblocker & Spotify

If you have not yet installed and started using your adblocker, I recommend that you do so first and, if possible, learn the basics of how it works. This will help you when installing Spotify Ads List.

Also, you must have installed Spotify (in case you are going to use it as an application) and created a Spotify account to use it, as Spotify Ads List does not perform these actions.

### Setup your adblocker

Below, you can find a series of basic guides on how to install and use your adblocker:

- Standard (Compatible with multiple adblockers and can also be used with the hosts file.)
- [Pi-Hole](https://docs.pi-hole.net/main/basic-install/)
- [Dnsmasq](https://dnsmasq.org/doc.html)
- [Adguard](https://adguard.com/kb/general/how-to-install/)
- [uBlock Origin](https://github.com/gorhill/uBlock?tab=readme-ov-file#installation)

### Setup Spotify

To start using Spotify you can use the web app or download the app for your OS:

- [Spotify Web App](https://open.spotify.com)
- [Download Spotify](https://www.spotify.com/en/download/)

## 4. Add Spotify Ads List to your adblocker

To add Spotify Ads List to your adblocker you will need to make use of a raw file that will be synced directly from our GitHub repository. To do this, simply copy the link and enter it in the appropriate field to add it to your adblocker (Or use the link in the case of uBlock Origin):

# Standard adblockers

| Adblocker | Raw URL | How to add this? |
| -- | -- | -- |
| Standard | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/standard_list.txt | Not applicable, unless you want to use the hosts file. In that case, [read this](https://nordvpn.com/es/blog/use-hosts-file-block-ads-malware/) |
| Pi-hole | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/pi-hole.txt | Not official documentation for this, go to the Web UI, in the left bar click on "Adlists", enter the raw url and click "Add" |
| Dnsmasq | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/dnsmasq.txt | There is not much official documentation, perhaps [this will help](https://dnsmasq.org/docs/dnsmasq-man.html) |
| Adguard | https://raw.githubusercontent.com/Isaaker/Spotify-AdsList/main/Lists/adguard.txt | [Read this](https://adguard.com/kb/) |

### Browser adblockers

#### uBlock Origin

| Browser | Add from link |
| -- | -- |
| Firefox | moz-extension://c396fed9-d8f8-4a6c-95a0-80773fa36d8a/asset-viewer.html?url=https%3A%2F%2Fraw.githubusercontent.com%2Fisaaker%2FSpotify-AdsList%2Fmain%2FLists%2Fadguard.txt&title=Spotify-AdsList&subscribe=1 |
| Chrome / Chromium | chrome-extension://cjpalhdlnbpafiamejdnhcphjbkeiagm/asset-viewer.html?url=https%3A%2F%2Fraw.githubusercontent.com%2Fisaaker%2FSpotify-AdsList%2Fmain%2FLists%2Fadguard.txt&title=Spotify-AdsList&subscribe=1 |

[You can also make this manually with the adguard raw URL](https://github.com/gorhill/uBlock/wiki/Dashboard:-Filter-lists#3rd-party-filter-lists)

## 5. Add Spotify Ads List whitelist to your adblocker

A whitelist is a list that lets your adblocker know which domains should not be blocked. Although usually these domains are not added to the list directly, many times some domains that are on the list (blocked) redirect legitimate requests to these domains (not blocked) via a CNAME and these requests are blocked before being redirected because it is a blocked domain. Therefore, the list will help you to ensure that legitimate requests can continue their course correctly.

To add the whitelist to your adblocker, you have to enter this domains manually in the whitelist area:

- login5.spotify.com
- spclient.wg.spotify.com
- open.spotify.com
- api-partner.spotify.com

You can find more help about how to add this on this links:

| Adblocker | Link |
|--|--|
| Standard | This is not possible in the hosts file, for other methods please consult your adblocker documentation |
| Pi-hole | [Read this](https://discourse.pi-hole.net/t/how-do-i-whitelist-or-blacklist-a-domain/244), you can also make this form the Web UI > Domains |
| Dnsmasq | Not docs of this available |
| Adguard | [Read this](https://github.com/AdguardTeam/AdGuardHome/discussions/3771) |
| uBlock Origin | [Read this](https://github.com/gorhill/uBlock/wiki/How-to-whitelist-a-web-site/745c6f01e1f88db8184bb27f48bbdd8a21b48a90) |

## 6. What can I do now?

Now the installation of the list should be complete, but you can still do more things:

- [Support my work by giving a star to my repository and/or creating a fork on GitHub](https://github.com/Isaaker/Spotify-AdsList)
- [Continue reading the documentation](spotify.piscinadeentropia.es)
- [Report false positives or contribute in our repository](https://github.com/Isaaker/Spotify-AdsList/issues)
- [Add more adlists](./why_add_more_blocklists)