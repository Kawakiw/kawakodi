# -*- coding: utf-8 -*-
#------------------------------------------------------------
# http://www.youtube.com/user/elearning
#------------------------------------------------------------
# License: GPL (http://www.gnu.org/licenses/gpl-3.0.html)
# Based on code from youtube addon
#------------------------------------------------------------

import os
import sys
import plugintools
import xbmc,xbmcaddon
from addon.common.addon import Addon

addonID = 'plugin.video.elearning'
addon = Addon(addonID, sys.argv)
local = xbmcaddon.Addon(id=addonID)
icon = local.getAddonInfo('icon')

YOUTUBE_CHANNEL_IDA = "kezakoo1"
YOUTUBE_CHANNEL_IDB = "UCFS0eRHTcchOpM-FCck7pGA"
YOUTUBE_CHANNEL_IDC = "TheOpenClassrooms"
YOUTUBE_CHANNEL_IDD = "MITNewsOffice"
YOUTUBE_CHANNEL_IDE = "YaleCourses"


# Entry point
def run():
    plugintools.log("elearning.run")
    
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
    plugintools.log("elearning.main_list "+repr(params))

    plugintools.add_item( 
        #action="", 
        title="Kezakoo",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDA+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Polyglot",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDB+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        #action="", 
        title="Les Classes Ouvertes",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDC+"/",
        thumbnail=icon,
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/mit.jpg', 
        title="Massachusetts Institute of Technology (MIT)",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDD+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/mit.png',
        folder=True )
	
    plugintools.add_item( 
        #action="", 
        title="Yale University",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDE+"/",
        thumbnail=icon,
        folder=True )

run()