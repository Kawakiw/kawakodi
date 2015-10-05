#-*- coding: utf-8 -*-
#Venom.
from resources.lib.config import cConfig
from resources.lib.gui.hoster import cHosterGui
from resources.lib.handler.rechercheHandler import cRechercheHandler
from resources.lib.handler.hosterHandler import cHosterHandler
from resources.lib.gui.gui import cGui
from resources.lib.favourite import cFav
from resources.lib.gui.guiElement import cGuiElement
from resources.lib.handler.inputParameterHandler import cInputParameterHandler
from resources.lib.handler.outputParameterHandler import cOutputParameterHandler
from resources.lib.handler.requestHandler import cRequestHandler
from resources.lib.parser import cParser
from resources.lib.util import cUtil
import urllib, unicodedata, re
import xbmcgui
import xbmc

try:    import json
except: import simplejson as json

SITE_IDENTIFIER = 'themoviedb_org'
SITE_NAME = 'TheMovieDB (beta)'
SITE_DESC = 'Base de données video.'

#doc de l'api http://docs.themoviedb.apiary.io/

URL_MAIN = 'https://api.themoviedb.org/'

API_KEY = '92ab39516970ab9d86396866456ec9b6'
API_VERS = '3'
API_URL = URL_MAIN+API_VERS

POSTER_URL = 'https://image.tmdb.org/t/p/w396/'
#FANART_URL = 'https://image.tmdb.org/t/p/w780/'
FANART_URL = 'https://image.tmdb.org/t/p/w1280/'
#FANART_URL = 'https://image.tmdb.org/t/p/original/'


#https://api.themoviedb.org/3/movie/popular?api_key=92ab39516970ab9d86396866456ec9b6


def load():
    oGui = cGui()
    
    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
    # oGui.addDir(SITE_IDENTIFIER, 'showSearch', 'Recherche', 'search.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', API_URL+'/movie/popular')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Films Populaires', 'comments.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', API_URL+'/movie/now_playing')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Films en salle', 'films.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', API_URL+'/movie/top_rated')
    oGui.addDir(SITE_IDENTIFIER, 'showMovies', 'Films les mieux notés', 'notes.png', oOutputParameterHandler)
   
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', API_URL+'/genre/movie/list')
    oGui.addDir(SITE_IDENTIFIER, 'showGenre', 'Films Genres', 'genres.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', API_URL+'/tv/popular')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'Séries Populaires', 'series.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', API_URL+'/tv/on_the_air')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'Séries a la tv', 'series.png', oOutputParameterHandler)

    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', API_URL+'/tv/top_rated')
    oGui.addDir(SITE_IDENTIFIER, 'showSeries', 'Séries les mieux notés', 'series.png', oOutputParameterHandler)

    # oOutputParameterHandler = cOutputParameterHandler()
    # oOutputParameterHandler.addParameter('siteUrl', API_URL+'/genre/tv/list')
    # oGui.addDir(SITE_IDENTIFIER, 'showGenre2', 'Séries Genres', 'genres.png', oOutputParameterHandler)
    
    oOutputParameterHandler = cOutputParameterHandler()
    oOutputParameterHandler.addParameter('siteUrl', API_URL+'/person/popular')
    oGui.addDir(SITE_IDENTIFIER, 'showActors', 'Acteurs Populaires', 'films.png', oOutputParameterHandler)
    
    oGui.setEndOfDirectory()
 
    
 
def showGenre():
    oGui = cGui()

    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addParameters('api_key', API_KEY)
    oRequestHandler.addParameters('language', 'fr')
    
    sHtmlContent = oRequestHandler.request(); 
    result = json.loads(sHtmlContent)       

    total = len(sHtmlContent)
    if (total > 0):
        for i in result['genres']:
            sId, sTitle = i['id'], i['name']

            sTitle = sTitle.encode("utf-8")
            sUrl = API_URL+'/genre/'+str(sId)+'/movies'
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', str(sTitle), 'genres.png', oOutputParameterHandler)
           
    oGui.setEndOfDirectory()
    

def showMovies():
    oGui = cGui()
 
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    iPage = 1
    if (oInputParameterHandler.exist('page')):
        iPage = oInputParameterHandler.getValue('page')
   
    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addParameters('api_key', API_KEY)
    oRequestHandler.addParameters('language', 'fr')
    oRequestHandler.addParameters('page', iPage)

    sHtmlContent = oRequestHandler.request();
    result = json.loads(sHtmlContent)
    
    total = len(sHtmlContent)

    if (total > 0):
        for i in result['results']:
            sId, sTitle, sOtitle, sThumbnail, sFanart = i['id'], i['title'], i['original_title'], i['poster_path'], i['backdrop_path']
            if sThumbnail:
                sThumbnail = POSTER_URL+sThumbnail
            else: sThumbnail = ''

            sTitle = sTitle.encode("utf-8")
            if sFanart:
                sFanart = FANART_URL+sFanart
            else : sFanart = ''

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str('none'))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('disp', 'search1')
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
            
            oGui.addMovieDB(SITE_IDENTIFIER, 'showHosters', sTitle, 'films.png', sThumbnail, sFanart, oOutputParameterHandler)
            
        if (iPage > 0):
            iNextPage = int(iPage) + 1
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('page', iNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showMovies', '[COLOR teal]Page '+str(iNextPage)+' >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
    
    #test pr chnagement mode
    xbmc.executebuiltin('Container.SetViewMode(500)')
    #bmcgui.ListItem.select(1)
    
    
def showSeries():
    oGui = cGui()
 
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    iPage = 1
    if (oInputParameterHandler.exist('page')):
        iPage = oInputParameterHandler.getValue('page')
   
    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addParameters('api_key', API_KEY)
    oRequestHandler.addParameters('language', 'fr')
    oRequestHandler.addParameters('page', iPage)

    sHtmlContent = oRequestHandler.request();
    result = json.loads(sHtmlContent)
    
    total = len(sHtmlContent)
    print result['results']
    if (total > 0):
        for i in result['results']:
            sId, sTitle, sOtitle, sThumbnail, sFanart = i['id'], i['name'], i['original_name'], i['poster_path'], i['backdrop_path']
            if sThumbnail:
                sThumbnail = POSTER_URL+sThumbnail
            else: sThumbnail = '' 
                
            if sFanart:
                sFanart = FANART_URL+sFanart
            else : sFanart = ''

            sTitle = sTitle.encode("utf-8")

            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str('none'))
            oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
            oOutputParameterHandler.addParameter('disp', 'search2')
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))          
            
            oGui.addTVDB(SITE_IDENTIFIER, 'showHosters', sTitle, 'series.png', sThumbnail, sFanart, oOutputParameterHandler)
            
        if (iPage > 0):
            iNextPage = int(iPage) + 1
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('page', iNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showSeries', '[COLOR teal]Page '+str(iNextPage)+' >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()
    
    #test pr chnagement mode
    xbmc.executebuiltin('Container.SetViewMode(500)')

def showActors():
    oGui = cGui()
    
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')

    iPage = 1
    if (oInputParameterHandler.exist('page')):
        iPage = oInputParameterHandler.getValue('page')
   
    oRequestHandler = cRequestHandler(sUrl)
    oRequestHandler.addParameters('api_key', API_KEY)
    oRequestHandler.addParameters('language', 'fr')
    oRequestHandler.addParameters('page', iPage)

    sHtmlContent = oRequestHandler.request();
    result = json.loads(sHtmlContent)
    
    total = len(sHtmlContent)

    if (total > 0):
        for i in result['results']:
            #print i['name']
            sName, sThumbnail = i['name'], i['profile_path']
            
            if sThumbnail:
                sThumbnail = POSTER_URL+sThumbnail
            else: sThumbnail = ''
                    
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', str(sUrl))
            oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail)) 
            
            
            oGui.addMovieDB(SITE_IDENTIFIER, 'showActors', '[COLOR red]'+str(sName)+'[/COLOR]', '', sThumbnail, '', oOutputParameterHandler)

            for e in i['known_for']:
                try:                     
                    sTitle = unicodedata.normalize('NFKD', e['title']).encode('ascii','ignore')
                    
                except: sTitle = "Aucune information"
                sId = e['id']
                sFanart = FANART_URL+e['backdrop_path']
                                                                
                if sThumbnail:
                    sThumbnail = POSTER_URL+e['poster_path']
                else: sThumbnail = ''

                #sTitle = sTitle.encode("utf-8")

                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', 'http://venom')
                oOutputParameterHandler.addParameter('sMovieTitle', str(sTitle))
                oOutputParameterHandler.addParameter('disp', 'none')
                oOutputParameterHandler.addParameter('sThumbnail', str(sThumbnail))
                
                oGui.addMovieDB(SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumbnail, sFanart, oOutputParameterHandler)
                
            
        if (iPage > 0):
            iNextPage = int(iPage) + 1
            oOutputParameterHandler = cOutputParameterHandler()
            oOutputParameterHandler.addParameter('siteUrl', sUrl)
            oOutputParameterHandler.addParameter('page', iNextPage)
            oGui.addDir(SITE_IDENTIFIER, 'showActors', '[COLOR teal]Page '+str(iNextPage)+' >>>[/COLOR]', 'next.png', oOutputParameterHandler)

    oGui.setEndOfDirectory()


def __checkForNextPage(sHtmlContent):
    sPattern = "<span class='page-numbers current'>.+?</span><a class='page-numbers' href='([^<]+)'>.+?</a>"
    oParser = cParser()
    aResult = oParser.parse(sHtmlContent, sPattern) 
    if (aResult[0] == True):
        return aResult[1][0]

    return False
    

def showHosters():
    oGui = cGui()
    oInputParameterHandler = cInputParameterHandler()
    sUrl = oInputParameterHandler.getValue('siteUrl')
    sMovieTitle = oInputParameterHandler.getValue('sMovieTitle')
    sThumbnail = oInputParameterHandler.getValue('sThumbnail')
    
    sDisp = oInputParameterHandler.getValue('disp')
    
    dialog2 = xbmcgui.Dialog()
    dialog_select = [cConfig().getSetting('search1_label'), cConfig().getSetting('search2_label'), cConfig().getSetting('search3_label'), cConfig().getSetting('search4_label')]
    
    disp = ['search1','search2','search3','search4']
    
    if (sDisp == 'none'):
        ret = dialog2.select('Select Recherche',dialog_select)
    else:
        ret = disp.index(sDisp)
    
    #nettoyage du nom pr la recherche
    #print 'avant ' + sMovieTitle
    sMovieTitle = unicode(sMovieTitle, 'utf-8')#converti en unicode pour aider aux convertions
    sMovieTitle = unicodedata.normalize('NFD', sMovieTitle).encode('ascii', 'ignore').decode("unicode_escape")#vire accent et '\'
    sMovieTitle = sMovieTitle.encode("utf-8").lower() #on repasse en utf-8
    sMovieTitle = re.sub(r'[^(\w| )]', ' ', sMovieTitle) #vire les caracteres a la con qui peuvent trainer
    sMovieTitle = re.sub('( |^)(le|la|les|du|au|a|l)( |$)',' ', sMovieTitle) #vire les articles
    sMovieTitle = re.sub('\(.+?\)',' ', sMovieTitle) #vire les parentheses
    sMovieTitle = re.sub(' +',' ',sMovieTitle) #vire les espaces multiples et on laisse les espaces sans modifs car certains codent avec %20 d'autres avec +
    #print 'apres ' + sMovieTitle
    
    if ret > -1:
        
        oHandler = cRechercheHandler()
        aPlugins = oHandler.getAvailablePlugins(disp[ret])
        for aPlugin in aPlugins:
            try:                   
                oOutputParameterHandler = cOutputParameterHandler()
                oOutputParameterHandler.addParameter('siteUrl', sUrl)
                oGui.addDir(aPlugin[1], 'load', '[COLOR olive]'+ aPlugin[1] +'[/COLOR]', 'search.png', oOutputParameterHandler)
            
                exec "from resources.sites import "+aPlugin[1]+" as search"
                sUrl = aPlugin[0]+sMovieTitle
                searchUrl = "search.%s('%s')" % (aPlugin[2], sUrl)
                exec searchUrl
            except:       
                pass
                
    oGui.setEndOfDirectory()
    
def addMoviedb(sId, sFunction, sLabel, sIcon, sThumbnail, fanart, oOutputParameterHandler = ''):
    
    #addMoviedb(oGui, SITE_IDENTIFIER, 'showHosters', sTitle, '', sThumbnail, sFanart, oOutputParameterHandler)
    oGui = cGui()
    oGuiElement = cGuiElement()
    oGuiElement.setSiteName(sId)
    oGuiElement.setFunction(sFunction)
    oGuiElement.setTitle(sLabel)
    #oGuiElement.setIcon(sIcon)
    oGuiElement.setMeta(0)
    #oGuiElement.setThumbnail(sThumbnail)
    #oGuiElement.setFanart(fanart)
    
    #cGui.addFolder(oGuiElement, oOutputParameterHandler)
    oGui.addFolder(oGuiElement, oOutputParameterHandler, False)

