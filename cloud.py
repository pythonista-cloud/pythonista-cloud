# coding: utf-8

'''
cloud.py 

Vision: 

- cloud.Import: to make the entry curve to using code hosted on GitHub much easier

Credits: 

- cloud.Import: idea and first version by @guerito, future versions on @webmaster4o's GitHub

'''

import bs4, urllib2, plistlib, shutil, zipfile, os, importlib, inspect, html2text, pickle, console

def Import(sTarget):
	for code in bs4.BeautifulSoup(urllib2.urlopen('http://forum.omz-software.com/topic/2775/cloud-import').read()).find_all('code'):
		s = code.getText()
		if s[:5] == '<?xml': 
			urlZ = plistlib.readPlistFromString(s)[sTarget]
			break
	d = dict()
	if os.path.isfile(os.path.expanduser('~/Documents/site-packages/' + 'cloud.pkl')):
		with open(os.path.expanduser('~/Documents/site-packages/' + 'cloud.pkl'), 'r') as f:
			d = pickle.Unpickler(f).load()
	s = html2text.html2text(urllib2.urlopen(urlZ).read())
	i = s.find('commits')
	iNow = int(s[i - 4:i - 1])
	try:
		iOld = d[sTarget.split('.')[0]]
	except:
		iOld = -1
	d[sTarget.split('.')[0]] = iNow
	with open(os.path.expanduser('~/Documents/site-packages/' + 'cloud.pkl'), 'w') as f:
		pickle.Pickler(f).dump(d)
	if iNow > iOld:
		console.hud_alert('updating ' + sTarget + ' ...')
		urlZ += '/archive/master.zip'
		sZ = os.path.expanduser('~/Documents/'+  urlZ.split('/')[-1])
		shutil.copyfileobj(urllib2.urlopen(urlZ), open(sZ, 'wb'), length=512*1024)
		with open(sZ, 'rb') as f:
			for member in zipfile.ZipFile(f).namelist():
				l = member.split('/')
				if len(l) <= 2: # module
					if l[-1][-3:] == '.py':
						zipfile.ZipFile(f).extract(member, os.path.expanduser('~/Documents/'))
						shutil.move(os.path.expanduser('~/Documents/'+ member), os.path.expanduser('~/Documents/site-packages/' + l[-1]))
				else: # package
					if l[1] == sTarget.split('.')[0] and l[-1] != '':
						zipfile.ZipFile(f).extract(member, os.path.expanduser('~/Documents/'))
						if not os.path.exists(os.path.expanduser('~/Documents/site-packages/' + l[-2])):
							os.mkdir(os.path.expanduser('~/Documents/site-packages/' + l[-2]))
						shutil.move(os.path.expanduser('~/Documents/'+ member), os.path.expanduser('~/Documents/site-packages/' + l[-2] + '/' + l[-1]))
		shutil.rmtree(os.path.expanduser('~/Documents/' + l[0]))
		os.remove(sZ)
	locals()[sTarget.split('.')[0]] = importlib.import_module(sTarget.split('.')[0])
	if len(sTarget.split('.')) != 1: locals()[sTarget.split('.')[1]] = importlib.import_module(sTarget)
	reload(locals()[sTarget.split('.')[0]])
        if len(sTarget.split('.')) != 1: reload(locals()[sTarget.split('.')[1]])
	inspect.currentframe().f_back.f_globals[sTarget.split('.')[0]] = locals()[sTarget.split('.')[0]]
