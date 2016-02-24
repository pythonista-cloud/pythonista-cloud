# coding: utf-8

'''
cloud.py 

Vision: 

- cloud.Import: to make the entry curve to using code hosted on GitHub much easier

Credits: 

- cloud.Import: idea and first version by @guerito, future versions on @webmaster4o's GitHub

'''

import bs4, console, cStringIO, html2text, importlib, inspect, os, pickle, plistlib, requests, shutil, zipfile

DOCS_DIR = os.path.expanduser('~/Documents')
SITE_DIR = os.path.join(DOCS_DIR, 'site-packages')
CLOUD_PKL = os.path.join(SITE_DIR, 'cloud.pkl')
URL = 'http://forum.omz-software.com/topic/2775/cloud-import'

def Import(sTarget):
	soup = bs4.BeautifulSoup(requests.get(URL).text)
	for code in soup.find_all('code', class_='xml'):
		s = code.getText()
		if s.startswith('<?xml'): 
			urlZ = plistlib.readPlistFromString(s)[sTarget]
			break
	d = dict()
	if os.path.isfile(CLOUD_PKL):
		with open(CLOUD_PKL, 'r') as f:
			d = pickle.Unpickler(f).load()
	s = html2text.html2text(requests.get(urlZ).text)
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
		content = requests.get(urlZ, stream=True).content
		with zipfile.ZipFile(cStringIO.StringIO(content)) as zip_file:
			for member in zip_file.namelist():
				l = member.split('/')
				if len(l) <= 2: # module
					if l[-1][-3:] == '.py':
						zip_file.extract(member, DOCS_DIR)
						shutil.move(os.path.join(DOCS_DIR, member), os.path.join(SITE_DIR, l[-1]))
				else: # package
					if l[1] == sTarget.split('.')[0] and l[-1] != '':
						zip_file.extract(member, DOCS_DIR)
						dest_path = os.path.join(SITE_DIR, l[-2])
						if not dest_path:
							os.mkdir(dest_path)
						shutil.move(os.path.join(DOCS_DIR, member), os.path.join(dest_path, l[-1]))
		shutil.rmtree(os.path.join(DOCS_DIR, l[0]))
	locals()[sTarget.split('.')[0]] = importlib.import_module(sTarget.split('.')[0])
	if len(sTarget.split('.')) != 1: locals()[sTarget.split('.')[1]] = importlib.import_module(sTarget)
	reload(locals()[sTarget.split('.')[0]])
        if len(sTarget.split('.')) != 1: reload(locals()[sTarget.split('.')[1]])
	inspect.currentframe().f_back.f_globals[sTarget.split('.')[0]] = locals()[sTarget.split('.')[0]]
