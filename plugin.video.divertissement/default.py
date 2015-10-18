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
YOUTUBE_CHANNEL_IDE = "UCsN_Ml220puJo9RFBHriAaw"
YOUTUBE_CHANNEL_IDF = "MOMOBOUSFIHA"
YOUTUBE_CHANNEL_IDG = "TheBlackmoussiba"
YOUTUBE_CHANNEL_IDH = "MonsieurDream"
YOUTUBE_CHANNEL_IDI = "NormalFaitDesVideos"



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
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/jfl.jpg', 
        title="Juste Pour Rire",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDA+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/jfl.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/comedia.jpg', 
        title="Comedia Al Oula",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDB+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/comedia.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/failarmy.jpg', 
        title="FailArmy",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDC+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/failarmy.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/jukinvideo.jpg', 
        title="JukinVideo",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDD+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/jukinvideo.png',
        folder=True )
	
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/darraj.jpg', 
        title="Darraj",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDE+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/darraj.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/momo.jpg', 
        title="Momo - Hitradio",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDF+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/momo.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/blackmossiba.jpg', 
        title="Black Mossiba",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDG+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/blackmossiba.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/cyprien.jpg', 
        title="Cyprien",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDH+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/cyprien.png',
        folder=True )
	
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/norman.jpg', 
        title="Normal Fait Des Vidéos",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDI+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/norman.png',
        folder=True )	

run()