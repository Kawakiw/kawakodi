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
YOUTUBE_CHANNEL_IDI = "NormanFaitDesVideos"
YOUTUBE_CHANNEL_IDJ = "ElWadyAflam"
YOUTUBE_CHANNEL_IDK = "KarimAbdAziz"
YOUTUBE_CHANNEL_IDL = "ATLArabTorrents"
YOUTUBE_CHANNEL_IDM = "cinemaghrebia"
YOUTUBE_CHANNEL_IDN = "sbitarr36"
YOUTUBE_CHANNEL_IDO = "chartstopten"
YOUTUBE_CHANNEL_IDP = "hmdproduction"
YOUTUBE_CHANNEL_IDQ = "INERNETvideo"
YOUTUBE_CHANNEL_IDR = "Hadoukentheband"
YOUTUBE_CHANNEL_IDS = "ANDIMOCHKIL"
YOUTUBE_CHANNEL_IDT = "fouseyTUBE"
YOUTUBE_CHANNEL_IDU = "PrankvsPrank"
YOUTUBE_CHANNEL_IDV = "ExplosmEntertainment"
YOUTUBE_CHANNEL_IDW = "woopgang"
YOUTUBE_CHANNEL_IDX = "UCAL3JXZSzSm8AlZyD3nQdBA"
YOUTUBE_CHANNEL_IDY = "MagicofRahat"
YOUTUBE_CHANNEL_IDZ = "colinfurze"
YOUTUBE_CHANNEL_IDAA = "blackbenja11"
YOUTUBE_CHANNEL_IDAB = "UCklLTAOBRj4DdxTazOzP_lA"
YOUTUBE_CHANNEL_IDAC = "wardegasa"
YOUTUBE_CHANNEL_IDAD = "msadaghd"
YOUTUBE_CHANNEL_IDAE = "SimoSedraty"
YOUTUBE_CHANNEL_IDAB = "edbassmaster"

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
        title="Norman Fait Des Vidéos",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDI+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/norman.png',
        folder=True )

    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/elwady.jpg', 
        title="El Wady Aflam",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDJ+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/elwady.png',
        folder=True )	
    
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/karim.jpg', 
        title="Karim Abdaziz's channel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDK+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/karim.png',
        folder=True )	

    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/atlarab.jpg', 
        title="ATL ArabTorrent's channel",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDL+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/atlarab.png',
        folder=True )	

    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/cinemaghrebia.jpg', 
        title="Cinémaghrebia",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDM+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/cinemaghrebia.png',
        folder=True )

    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/sbitarr36.jpg', 
        title="Sbitarr 36",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDN+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/sbitarr36.png',
        folder=True )			
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/chartstop10.jpg', 
        title="Charts Top 10",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDO+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/chartstop10.png',
        folder=True )

    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/hmdprod.jpg', 
        title="HMD prod",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDP+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/hmdprod.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/inernet.jpg', 
        title="INERNET",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDQ+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/inernet.png',
        folder=True )

    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/paa.jpg', 
        title="People Are Awesome",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDR+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/paa.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/andimouchkil.jpg', 
        title="3endi Mouchkil",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDS+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/andimouchkil.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/fouseytube.jpg', 
        title="fouseyTUBE",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDT+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/fouseytube.png',
        folder=True )
		 
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/pvp.jpg', 
        title="PrankvsPrank",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDU+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/pvp.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/c&h.jpg', 
        title="Cyanide & Happiness",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDV+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/c&h.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/woopgang.jpg', 
        title="Le Woop",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDW+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/woopgang.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/primitivetechnology.jpg', 
        title="Primitive Technology",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDX+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/primitivetechnology.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/mor.jpg', 
        title="Magic Of Rahat",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDY+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/mor.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/Colinfurze.jpg', 
        title="Colinfurze",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDZ+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/Colinfurze.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/twinkieman.jpg', 
        title="Twinkie Man",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDAA+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/twinkieman.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/yif.jpg', 
        title="Yes it's funny!",
        url="plugin://plugin.video.youtube/channel/"+YOUTUBE_CHANNEL_IDAB+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/yif.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/wardega.jpg', 
        title="SA Wardega",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDAC+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/wardega.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/electroboom.jpg', 
        title="ElectroBOOM",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDAD+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/electroboom.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/simosedraty.jpg', 
        title="Simo Sedraty",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDAE+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/simosedraty.png',
        folder=True )
		
    plugintools.add_item( 
        fanart='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/fanarts/edbassmaster.jpg', 
        title="Ed Bassmaster",
        url="plugin://plugin.video.youtube/user/"+YOUTUBE_CHANNEL_IDAF+"/",
        thumbnail='https://raw.githubusercontent.com/Kawakiw/kawakodi/master/ressources/thumbnails/edbassmaster.png',
        folder=True )
		
run()