# coding: utf-8

'''
cloud.py 

Vision: 

- cloud.Import: to make the entry curve to using code hosted on GitHub much easier

Credits: 

- cloud.Import: idea and first version by @guerito, future versions on @webmaster4o's GitHub

'''

import bs4, console, html2text, importlib, inspect, os, pickle, plistlib, shutil, urllib2, zipfile

DOCS_DIR = os.path.expanduser('~/Documents')
SITE_DIR = os.path.join(DOCS_DIR, 'site-packages')
CLOUD_PKL = os.path.join(SITE_DIR, 'cloud.pkl')
URL = 'http://forum.omz-software.com/topic/2775/cloud-import'

def Import(sTarget):
	soup = bs4.BeautifulSoup(urllib2.urlopen(URL).read())
	for code in soup.find_all('code', class_='xml'):
		s = code.getText()
		if s.startswith('<?xml'): 
			urlZ = plistlib.readPlistFromString(s)[sTarget]
			break
	d = dict()
	if os.path.isfile(CLOUD_PKL):
		with open(CLOUD_PKL, 'r') as f:
			d = pickle.Unpickler(f).load()
	s = html2text.html2text(urllib2.urlopen(urlZ).read())
	i = s.find('commits')
	iNow = int(s[i - 4:i - 1])
	try:
		iOld = d[sTarget.split('.')[0]]
	except:
		iOld = -1
	d[sTarget.split('.')[0]] = iNow
	with open(CLOUD_PKL, 'w') as f:
		pickle.Pickler(f).dump(d)
	if iNow > iOld:
		console.hud_alert('updating ' + sTarget + ' ...')
		urlZ += '/archive/master.zip'
		sZ = os.path.join(DOCS_DIR, urlZ.split('/')[-1])
		shutil.copyfileobj(urllib2.urlopen(urlZ), open(sZ, 'wb'), length=512*1024)
		with open(sZ, 'rb') as f:
			for member in zipfile.ZipFile(f).namelist():
				l = member.split('/')
				if len(l) <= 2: # module
					if l[-1][-3:] == '.py':
						zipfile.ZipFile(f).extract(member, DOCS_DIR)
						shutil.move(os.path.join(DOCS_DIR, member), os.path.join(SITE_DIR, l[-1]))
				else: # package
					if l[1] == sTarget.split('.')[0] and l[-1] != '':
						zipfile.ZipFile(f).extract(member, DOCS_DIR)
						dest_path = os.path.join(SITE_DIR, l[-2]))
						if not dest_path:
							os.mkdir(dest_path)
						shutil.move(os.path.join(DOCS_DIR, member), os.path.join(dest_path, l[-1]))
		shutil.rmtree(os.path.join(DOCS_DIR, l[0]))
		os.remove(sZ)
	locals()[sTarget.split('.')[0]] = importlib.import_module(sTarget.split('.')[0])
	if len(sTarget.split('.')) != 1: locals()[sTarget.split('.')[1]] = importlib.import_module(sTarget)
	reload(locals()[sTarget.split('.')[0]])
        if len(sTarget.split('.')) != 1: reload(locals()[sTarget.split('.')[1]])
	inspect.currentframe().f_back.f_globals[sTarget.split('.')[0]] = locals()[sTarget.split('.')[0]]
