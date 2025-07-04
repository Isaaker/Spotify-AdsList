# Spotify Ads Whitelist

Created by: Isaaker

Revised: 28/6/25

Version: WHITELIST

Number of domains: 11

Read more: https://github.com/Isaaker/Spotify-AdsList

License: https://github.com/Isaaker/Spotify-AdsList/blob/main/LICENSE.txt

**WARNING: This list is not formatted in any special way and therefore cannot be downloaded and used as an input file, please add the domains manually.**

## Detailed list

| Domain | Explanation | What happens when it is blocked? |
| -- | -- | -- |
| login5.spotify.com | Spotify login domain | Unable to log in to Spotify no audio is played and many screens cannot be accessed |
| spclient.wg.spotify.com | Spotify domain providing music and controlling it | The player does not work, it is impossible to control the audio playback and this causes it to skip songs continuously and without stopping |
| open.spotify.com | In principle, I have not observed any adverse effect on the applications when blocking this domain, however, blocking it makes it impossible to access the spotify web platform | Unable to access the spotify web player |
| api-partner.spotify.com | This domain is the one that provides some of the main images of the app such as the home screen, the application will continue to play music but some screens may not work properly or may be inaccessible by displaying an error. | Problems displaying images |
| partners.wg.spotify.com | This domain is the one that provides some of the main images of the app such as the home screen, the application will continue to play music but some screens may not work properly or may be inaccessible by displaying an error. | Problems displaying images |
| api.spotify.com | Spotify main API |
| audio4-fa.scdn.co | Some platforms need this domain unlocked to get audio tracks from Spotify servers | Songs may not play on certain platforms |
| audio-fa.scdn.co | Some platforms need this domain unlocked to get audio tracks from Spotify servers | Songs may not play on certain platforms |
| seektables.scdn.co | Nest Mini devices can't properly cast towards using the Spotify mobile app |
| cast.scdn.co | Server for casting to google devices such as Google Nest | Unable to use Google Chromecast or Nest with Spotify |
| audio4-ak.spotifycdn.com | Problems with audio on Linux |
| pickasso.spotifycdn.com | This domains provides Covers, banners and images from the music and playlists | Missing images |
| mosaic.scdn.co | This domains provides Covers, banners and images from the music and playlists | Missing images |

## Specific paths for gew1-spclient.spotify.com

**For further info see: [#61](https://github.com/Isaaker/Spotify-AdsList/issues/61) [#68](https://github.com/Isaaker/Spotify-AdsList/issues/68)**

``
gew1-spclient.spotify.com/melody
gew1-spclient.spotify.com/connect-state
gew1-spclient.spotify.com/melody
gew1-spclient.spotify.com/connect-state
gew1-spclient.spotify.com/gabo-receiver-service
gew1-spclient.spotify.com/track-playback
api.spotify.com^$xhr
gew1-spclient.spotify.com/storage-resolve
gew1-spclient.spotify.com/widevine-licens`
``

## Plain List

- login5.spotify.com
- spclient.wg.spotify.com
- open.spotify.com
- api-partner.spotify.com
- partners.wg.spotify.com
- api.spotify.com
- audio4-fa.scdn.co
- audio-fa.scdn.co
- seektables.scdn.co
- cast.scdn.co
- audio4-ak.spotifycdn.com
- pickasso.spotifycdn.com
- mosaic.scdn.co