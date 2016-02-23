#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib, urllib2
import xbmcplugin, xbmcaddon, xbmcgui, xbmc
import sys, os, re, json, base64, operator, datetime, time
from decimal import *
from resources.parsers.main import *

pluginhandle = int(sys.argv[1])
addon = xbmcaddon.Addon()
settings = xbmcaddon.Addon( id = "plugin.video.streamingvf" )
domain = base64.b64decode(settings.getSetting("domain"))
nb_content = int(float(settings.getSetting("nb_movies")))
debug = ( settings.getSetting( "debug" ) == "true" )
reso_select = ( settings.getSetting( "reso_select" ) == "true" )
email = settings.getSetting( "email" )
password = settings.getSetting( "password" )

icon_path = os.path.join(xbmc.translatePath(os.path.join(xbmc.translatePath(os.path.join(xbmc.translatePath(os.path.join("special://","home")),"addons")),"plugin.video.streamingvf")),"icon.png")

def parameters_string_to_dict(parameters):
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict
    
def translation(id):
    return addon.getLocalizedString(id).encode('utf-8','ignore')
    
def get_list(query,data):
	try:
		req = urllib2.Request(domain+'api2-json/'+query+'.php')
		f = urllib2.urlopen(req,data)
		html = f.read()
		f.close()
		return html
	except:
		exit()

def index():
    addDir(translation(30001) % nb_content, "", 'lastmovies', "", "", 0)
    addDir(translation(30010) % nb_content, "", 'popular', "", "", 0)
    addDir(translation(30006), "", 'genres', "", "", 0)
    addDir(translation(30023), "", 'countries', "", "", 0)
    addDir(translation(30012), "", 'titles', "", "", 0)
    addDir(translation(30008), "", 'years', "", "", 0)
    addDir(translation(30009) % nb_content, "", 'votes', "", "", 0)
    addDir(translation(30026) % nb_content, "", 'random', "", "", 0)
    addDir(translation(30011), "", 'search', "", "", 0)
    xbmcplugin.endOfDirectory(pluginhandle)
    
def addDir(name, url, mode, iconimage, fanart, desc="", start=0):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&start="+str(start)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    if ( fanart != '' ):
        liz.setProperty("Fanart_Image", fanart)
    liz.setInfo(type="movies", infoLabels={"Title": name, "Plot": desc})
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok

def addMovie(name, url, mode, iconimage, fanart, release, genre, date_added, desc, runtime, vote, studio, trailer):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)
    xbmcplugin.setContent(pluginhandle, 'movies')
    ok = True
    if debug:
        name = name+" [COLOR orange]f"+url+"[/COLOR]"
    liz = xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
    liz.addContextMenuItems([(translation(30014), 'Action(Info)')])
    if ( fanart != '' ):
        liz.setProperty("Fanart_Image", fanart)
    liz.setInfo(type="video", infoLabels={"Title": name, "Plot": desc, "Year": release, "Genre": genre, "Rating": vote, "Duration": int(runtime)*60, "Studio": studio, "Trailer" : trailer})
    if ( trailer != '' ):
        liz.setInfo(type="video", infoLabels={"Trailer" : "plugin://plugin.video.youtube/?action=play_video&videoid="+trailer})
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok
    
def lastmovies(mode):
    data_list = json.loads(get_list( mode, urllib.urlencode({'nb_items': nb_content})))
    movarray = data_list.items()
    movarray = sorted(movarray, key=lambda movie: movie[0],reverse=True)
    for (movie_id, movie_info) in movarray:
        addMovie(movie_info[0], movie_id, 'sources', movie_info[5], movie_info[6], movie_info[2], movie_info[3], movie_info[4], movie_info[1], movie_info[7], movie_info[8], movie_info[9], movie_info[11])
    xbmcplugin.endOfDirectory(pluginhandle)
    
def genrelist(mode,genre_id,start):
	data_list = json.loads(get_list( mode, urllib.urlencode({'nb_items': nb_content, 'id': genre_id, 'start': start})))
	movarray = data_list.items()
	movarray = sorted(movarray, key=lambda movie: movie[1])
	for (movie_id, movie_info) in movarray:
		addMovie(movie_info[0], movie_id, 'sources', movie_info[5], movie_info[6], movie_info[2], movie_info[3], movie_info[4], movie_info[1], movie_info[7], movie_info[8], movie_info[9], movie_info[12])
	if ( int(start)+nb_content <= movie_info[11]):
		addDir("...", genre_id, 'genre', "", "", "",int(start)+nb_content)
	xbmcplugin.endOfDirectory(pluginhandle)

def countrylist(mode,country_id,start):
	data_list = json.loads(get_list( mode, urllib.urlencode({'nb_items': nb_content, 'id': country_id, 'start': start})))
	movarray = data_list.items()
	movarray = sorted(movarray, key=lambda movie: movie[1])
	for (movie_id, movie_info) in movarray:
		addMovie(movie_info[0], movie_id, 'sources', movie_info[5], movie_info[6], movie_info[2], movie_info[3], movie_info[4], movie_info[1], movie_info[7], movie_info[8], movie_info[9], movie_info[12])
	if ( int(start)+nb_content <= movie_info[11]):
		addDir("...", country_id, 'country', "", "", "",int(start)+nb_content)
	xbmcplugin.endOfDirectory(pluginhandle)

def titlelist(mode,letter_id,start):
	data_list = json.loads(get_list( mode, urllib.urlencode({'nb_items': nb_content, 'id': letter_id, 'start': start})))
	movarray = data_list.items()
	movarray = sorted(movarray, key=lambda movie: movie[1])
	for (movie_id, movie_info) in movarray:
		addMovie(movie_info[0], movie_id, 'sources', movie_info[5], movie_info[6], movie_info[2], movie_info[3], movie_info[4], movie_info[1], movie_info[7], movie_info[8], movie_info[9], movie_info[12])
	if ( int(start)+nb_content <= movie_info[11]):
		addDir("...", letter_id, 'title', "", "", "",int(start)+nb_content)
	xbmcplugin.endOfDirectory(pluginhandle)

def yearlist(mode,year_id,start):
	data_list = json.loads(get_list( mode, urllib.urlencode({'nb_items': nb_content, 'id': year_id, 'start': start})))
	movarray = data_list.items()
	movarray = sorted(movarray, key=lambda movie: movie[1])
	for (movie_id, movie_info) in movarray:
		addMovie(movie_info[0], movie_id, 'sources', movie_info[5], movie_info[6], movie_info[2], movie_info[3], movie_info[4], movie_info[1], movie_info[7], movie_info[8], movie_info[9], movie_info[12])
	if ( int(start)+nb_content <= movie_info[11]):
		addDir("...", year_id, 'year', "", "", "",int(start)+nb_content)
	xbmcplugin.endOfDirectory(pluginhandle)

def votes(mode):
    data_list = json.loads(get_list( mode, urllib.urlencode({'nb_items': nb_content})))
    movarray = data_list.items()
    movarray = sorted(movarray, key=lambda movie: movie[1][8],reverse=True)
    for (movie_id, movie_info) in movarray:
        addMovie(movie_info[0], movie_id, 'sources', movie_info[5], movie_info[6], movie_info[2], movie_info[3], movie_info[4], movie_info[1], movie_info[7], movie_info[8], movie_info[9], movie_info[10])
    xbmcplugin.endOfDirectory(pluginhandle)
    
def popular(mode):
    data_list = json.loads(get_list( mode, urllib.urlencode({'nb_items': nb_content})))
    movarray = data_list.items()
    movarray = sorted(movarray, key=lambda movie: Decimal(movie[1][10]),reverse=True)
    for (movie_id, movie_info) in movarray:
        addMovie(movie_info[0], movie_id, 'sources', movie_info[5], movie_info[6], movie_info[2], movie_info[3], movie_info[4], movie_info[1], movie_info[7], movie_info[8], movie_info[9], movie_info[11])
    xbmcplugin.endOfDirectory(pluginhandle)
    
def random(mode):
    data_list = json.loads(get_list( mode, urllib.urlencode({'nb_items': nb_content})))
    movarray = data_list.items()
    movarray = sorted(movarray, key=lambda movie: Decimal(movie[1][10]),reverse=True)
    for (movie_id, movie_info) in movarray:
        addMovie(movie_info[0], movie_id, 'sources', movie_info[5], movie_info[6], movie_info[2], movie_info[3], movie_info[4], movie_info[1], movie_info[7], movie_info[8], movie_info[9], movie_info[11])
    xbmcplugin.endOfDirectory(pluginhandle)

def search(mode):
	dialog = xbmcgui.Dialog()
	keyboard = xbmc.Keyboard("",translation(30011))
	keyboard.doModal()
	if (keyboard.isConfirmed()):
		data_list = json.loads(get_list( mode, urllib.urlencode({'nb_items': nb_content, 'query': keyboard.getText()})))
		if len(data_list) != 0:
			movarray = data_list.items()
			movarray = sorted(movarray, key=lambda movie: movie[1])
			for (movie_id, movie_info) in movarray:
				addMovie(movie_info[0], movie_id, 'sources', movie_info[5], movie_info[6], movie_info[2], movie_info[3], movie_info[4], movie_info[1], movie_info[7], movie_info[8], movie_info[9], movie_info[10])
			xbmcplugin.endOfDirectory(pluginhandle)
		else:
			xbmcgui.Dialog().ok(translation(30015), translation(30013) % keyboard.getText(), "")

def genreslist(mode):
	data_list = json.loads(get_list(mode, ""))
	movarray = data_list.items()
	movarray = sorted(movarray, key=lambda movie: movie[1])
	for (genre_id, genre_info) in movarray:
		addDir(genre_info[0], genre_id, 'genre', "", "", "",0)
	xbmcplugin.endOfDirectory(pluginhandle)

def countrieslist(mode):
	data_list = json.loads(get_list(mode, ""))
	movarray = data_list.items()
	movarray = sorted(movarray, key=lambda movie: movie[1])
	for (genre_id, genre_info) in movarray:
		addDir(genre_info[0], genre_id, 'country', "", "", "",0)
	xbmcplugin.endOfDirectory(pluginhandle)

def titleslist(mode):
	data_list = json.loads(get_list(mode, ""))
	movarray = data_list.items()
	movarray = sorted(movarray, key=lambda movie: movie[1])
	for (title_id, title_info) in movarray:
		addDir(title_info[0], title_id, 'title', "", "", "",0)
	xbmcplugin.endOfDirectory(pluginhandle)

def yearslist(mode):
	data_list = json.loads(get_list(mode, ""))
	movarray = data_list.items()
	movarray = sorted(movarray, key=lambda movie: movie[1],reverse=True)
	for (year_id, year_info) in movarray:
		addDir(year_info[0], year_id, 'year', "", "", "",0)
	xbmcplugin.endOfDirectory(pluginhandle)

def sources(mode,url):
	source_list = []
	stream_url = []
	display_list = []
	data_list = json.loads(get_list(mode,urllib.urlencode({'source_id': url, 'email': email, 'password': password})))
	if (len(data_list) > 0):
		dialog = xbmcgui.Dialog()
		try:
			for (source_id, source_info) in data_list.items():
				source_list.append(source_id)
				stream_txt = translation(30016) % source_info[2]
				if debug:
					stream_txt = stream_txt+" [COLOR orange]s"+source_id+"[/COLOR]"
				display_list.append(stream_txt)
				stream_url.append(source_info[3])
			if (reso_select):
				video_source = dialog.select(translation(30003), display_list)
				if (not video_source == -1 ):
					play_video("play_video", source_list[video_source],stream_url[video_source])
			else:
					play_video("play_video", source_list[0],stream_url[0])
		except:
			xbmcgui.Dialog().ok(translation(30004), '[B]'+translation(30018)+'...[/B]', translation(30017))
	else:
		xbmcgui.Dialog().ok(translation(30004), '[B]'+translation(30018)+'...[/B]', translation(30017))

def play_video(mode,source_id,stream_url):
    xbmc.executebuiltin("XBMC.Notification(%s,%s,%s,%s)" % (translation(30004),translation(30005)+'...',3000,icon_path))
    data_list = json.loads(get_list(mode,urllib.urlencode({'source_id': source_id, 'stream_url': stream_url})))
    if (len(data_list) > 0):
        for (stream_id, stream_info) in data_list.items():
			liz = xbmcgui.ListItem(stream_info[1], iconImage=stream_info[2], thumbnailImage=stream_info[2])
			liz.setInfo(type="video", infoLabels={"Title": stream_info[1], "Plot": stream_info[3], "Year": stream_info[4], "Rating": stream_info[5], "Genre": stream_info[6], "Studio": stream_info[7], "Duration": int(stream_info[8])*60})
			vid_url = url_convert(stream_info[0])
			xbmc.Player().play(vid_url,listitem=liz)
            
params = parameters_string_to_dict(sys.argv[2])
mode = urllib.unquote_plus(params.get('mode', ''))
start = urllib.unquote_plus(params.get('start', ''))
url = urllib.unquote_plus(params.get('url', ''))
name = urllib.unquote_plus(params.get('name', ''))

try:
    start
except:
    start = 0
    
if mode == 'play_video':
    play_video(mode,url)
elif mode == 'lastmovies':
    lastmovies(mode)
elif mode == 'genres':
    genreslist(mode)
elif mode == 'countries':
    countrieslist(mode)
elif mode == 'titles':
    titleslist(mode)
elif mode == 'years':
    yearslist(mode)
elif mode == 'votes':
    votes(mode)
elif mode == 'popular':
    popular(mode)
elif mode == 'random':
    random(mode)
elif mode == 'search':
    search(mode)
elif mode == 'genre':
    genrelist(mode,url,start)
elif mode == 'country':
    countrylist(mode,url,start)
elif mode == 'title':
    titlelist(mode,url,start)
elif mode == 'year':
    yearlist(mode,url,start)
elif mode == 'sources':
    sources(mode,url)
elif email == '' or password == '':
    settings.openSettings()
else:
    index()
