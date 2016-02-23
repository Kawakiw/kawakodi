# -*- coding: utf-8 -*-
 
import os,base64,json,re,urllib,urllib2
from urlparse import urlparse
useragent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"

def get_code(url,refer):
	hdr = {'User-Agent': useragent, 'Referer': refer}
	req = urllib2.Request(url, headers=hdr)
	page = urllib2.urlopen(req)
	return page.read()
	
def detect(source):
    source = source.replace(' ', '')
    if re.search('eval\(function\(p,a,c,k,e,(?:r|d)', source): return True
    else: return False

def unpack(source):
    payload, symtab, radix, count = _filterargs(source)
    if count != len(symtab):
        raise UnpackingError('Malformed p.a.c.k.e.r. symtab.')
    try:
        unbase = Unbaser(radix)
    except TypeError:
        raise UnpackingError('Unknown p.a.c.k.e.r. encoding.')
    def lookup(match):
        word = match.group(0)
        return symtab[unbase(word)] or word
    source = re.sub(r'\b\w+\b', lookup, payload)
    return _replacestrings(source)

def _filterargs(source):
    argsregex = (r"}\('(.*)', *(\d+), *(\d+), *'(.*?)'\.split\('\|'\)")
    args = re.search(argsregex, source, re.DOTALL).groups()
    try:
        return args[0], args[3].split('|'), int(args[1]), int(args[2])
    except ValueError:
        raise UnpackingError('Corrupted p.a.c.k.e.r. data.')

def _replacestrings(source):
    match = re.search(r'var *(_\w+)\=\["(.*?)"\];', source, re.DOTALL)
    if match:
        varname, strings = match.groups()
        startpoint = len(match.group(0))
        lookup = strings.split('","')
        variable = '%s[%%d]' % varname
        for index, value in enumerate(lookup):
            source = source.replace(variable % index, '"%s"' % value)
        return source[startpoint:]
    return source

class Unbaser(object):
    ALPHABET = {
        62: '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ',
        95: (' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ'
             '[\]^_`abcdefghijklmnopqrstuvwxyz{|}~')
    }
    
    def __init__(self, base):
        self.base = base
        if 2 <= base <= 36:
            self.unbase = lambda string: int(string, base)
        else:
            if base < 62:
                self.ALPHABET[base] = self.ALPHABET[62][0:base]
            elif 62 < base < 95:
                self.ALPHABET[base] = self.ALPHABET[95][0:base]
            try:
                self.dictionary = dict((cipher, index) for index, cipher in enumerate(self.ALPHABET[base]))
            except KeyError:
                raise TypeError('Unsupported base encoding.')
            self.unbase = self._dictunbaser

    def __call__(self, string):
        return self.unbase(string)

    def _dictunbaser(self, string):
        ret = 0
        for index, cipher in enumerate(string[::-1]):
            ret += (self.base ** index) * self.dictionary[cipher]
        return ret

class UnpackingError(Exception):
    pass


def url_convert(url):
	url = base64.b64decode(url)

	if "youwatch.org" in url: 
		html = get_code(url, url)
		embed_url = re.search('class="embed-responsive-item" src="(.*?)"',html.replace('\n', '').replace('\r', '')).group(1)
		html = get_code("http:"+embed_url, url)
		ext_url = re.search('src="(.*?)"',html).group(1)
		parsed_uri = urlparse(ext_url)
		html = get_code(ext_url, '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri))
		url = re.search('file:"(.*?)"',html).group(1)

	if "videomega.tv" in url: 
		match = re.findall('eval(.*?){}\)\)', get_code(url,url))
		html = unpack('eval'+match[0]+'{}\)\)')
		mp4 = re.findall('src","(.*?)"', html)
		url = mp4[0]

	if "uptostream.com" in url:
		match = re.findall("src='(.*?)/0' type='video/mp4", get_code(url,url))
		url = "http:"+match[-1]+"/0|User-agent="+useragent

	return url
