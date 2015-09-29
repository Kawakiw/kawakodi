# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/JustForLaughsTV
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.divertissement'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_IDA = "JustForLaughsTV"
YOUTUBE_CHANNEL_IDB = "comediatvtube"
YOUTUBE_CHANNEL_IDC = "failarmy"
YOUTUBE_CHANNEL_IDD = "JukinVideoDotCom"




# Entry point
def run():
    plugintools.log("divertissement.run")
    
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
    plugintools.log("divertissement.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Juste Pour Rire",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDA+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Comedia Al Oula",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDB+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="FailArmy",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDC+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="JukinVideo",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDD+"/",
        thumbnail=icon,
        folder=True )

run()