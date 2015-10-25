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
YOUTUBE_CHANNEL_IDH = "ChefAhmadAllCooking"



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
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/marmiton.jpg', 
        title="Marmiton",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDA+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/marmiton.png',
        folder=True )
	
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/fitnessblender.jpg', 
        title="Fitness Blender",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDB+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/fitnessblender.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/doctissimo.jpg', 
        title="Doctissimo",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDC+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/doctissimo.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/elle.jpg', 
        title="ELLE",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDD+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/elle.png',
        folder=True )
	
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/be.jpg', 
        title="Be",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDE+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/be.png',
        folder=True )
	
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/latelierdeschefs.jpg', 
        title="L'atelier Des Chefs",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDF+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/latelierdeschefs.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/aufeminin.jpg', 
        title="Au Féminin",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDG+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/aufeminin.png',
        folder=True 
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/chefahmad.jpg', 
        title="Chef Ahmad ",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDH+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/chefahmad.png',
        folder=True )

run()