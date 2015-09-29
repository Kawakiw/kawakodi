# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/bienetreOfficiel
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.bienetre'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_IDA = "MarmitonOfficiel"
YOUTUBE_CHANNEL_IDB = "FitnessBlender"
YOUTUBE_CHANNEL_IDC = "Doctissimo"
YOUTUBE_CHANNEL_IDD = "ELLEfr"
YOUTUBE_CHANNEL_IDE = "be"
YOUTUBE_CHANNEL_IDF = "atelierdeschefs"
YOUTUBE_CHANNEL_IDG = "AuFemininBeaute"



# Entry point
def run():
    plugintools.log("bienetre.run")
    
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
    plugintools.log("bienetre.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Marmiton",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDA+"/",
        thumbnail=icon,
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Fitness Blender",
        url="plugin://plugin.video.youtube/show/"+YOUTUBE_CHANNEL_IDB+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Doctissimo",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDC+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="ELLE",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDD+"/",
        thumbnail=icon,
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Be",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDE+"/",
        thumbnail=icon,
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="L'atelier Des Chefs",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDF+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Au Féminin",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDG+"/",
        thumbnail=icon,
        folder=True )

run()