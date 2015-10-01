# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/UCyQ8x-6EL1hQbvUfFB8MEfg
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.infoactu'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_IDA = "UCyQ8x-6EL1hQbvUfFB8MEfg"
YOUTUBE_CHANNEL_IDB = "2MTV"
YOUTUBE_CHANNEL_IDC = "medi1TV"
YOUTUBE_CHANNEL_IDD = "BFMTV"
YOUTUBE_CHANNEL_IDE = "LaChaineTechno"
YOUTUBE_CHANNEL_IDF = "euronewsfr"
YOUTUBE_CHANNEL_IDG = "france24"
#YOUTUBE_CHANNEL_IDH = "UC-9-kyTW8ZkZNDHQJ6FgpwQ"

# Entry point
def run():
    plugintools.log("infoactu.run")
    
    # Get params
    params = plugintools.get_params()
    
    if params.get("action") is None:
        main_list(params)
    else:
        action = params.get("action")
        exec action+"(params)"
    
    plugintools.close_item_list()

# Main menu
def main_list(params):
    plugintools.log("infoactu.main_list "+repr(params))

    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/telquel.jpg', 
        title="TelQuel",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDA+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/telquel.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/2m.jpg', 
        title="2M",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDB+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/2m.png',
        folder=True )
	
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/medi1tv.jpg', 
        title="Medi 1 TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDC+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/medi1tv.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/bfmtv.jpg', 
        title="BFM TV",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDD+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/bfmtv.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/01net.jpg', 
        title="01net TV - La Chaine Techno",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDE+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/01net.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/euronews.jpg', 
        title="Euronews",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDF+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/euronews.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/france24.jpg', 
        title="France 24",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDG+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/france24.png',
        folder=True )
		
    #plugintools.add_item( 
    #    #action="", 
    #    title="Musique",
    #    url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDH+"/",
    #    thumbnail=icon,
    #    folder=True )

run()