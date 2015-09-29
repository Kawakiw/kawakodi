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

addonID = 'plugin.video.musique'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_IDA = "UC-9-kyTW8ZkZNDHQJ6FgpwQ"
YOUTUBE_CHANNEL_IDB = "UCE80FOXpJydkkMo-BYoJdEg"
YOUTUBE_CHANNEL_IDC = "UCCIPrrom6DIftcrInjeMvsQ"
YOUTUBE_CHANNEL_IDD = "UCYYsyo5ekR-2Nw10s4mj3pQ"
YOUTUBE_CHANNEL_IDE = "UCUnSTiCHiHgZA9NQUG6lZkQ"
YOUTUBE_CHANNEL_IDF = "UCkkGN2n-fAmGhTFJOXvdIJw"
YOUTUBE_CHANNEL_IDG = "UCDQ_5Wcc54n1_GrAzf05uWQ"
YOUTUBE_CHANNEL_IDH = "UCsFaF_3y_L__y8kWAIEhv1w"

# Entry point
def run():
    plugintools.log("musique.run")
    
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
    plugintools.log("musique.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Playlists Youtube",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDA+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Pop",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDB+"/",
        thumbnail=icon,
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Électronique",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDC+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Latino-américaine",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDD+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Hip-hop",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDE+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Orientale",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDF+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Asiatique",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDG+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Soul",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDH+"/",
        thumbnail=icon,
        folder=True )

run()