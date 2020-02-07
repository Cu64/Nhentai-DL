#----------Libaries----------
import os
import json
import codecs
import logging
import requests
import zipfile36 as zipfile
from win10toast import ToastNotifier

#----------Logger Init----------
logger = logging.getLogger('N-DLer')
logger.setLevel(logging.INFO)
fh = logging.FileHandler('log.txt')
fh.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

#----------Toast Notification Init----------
toaster = ToastNotifier()

#----------Input----------
logger.info('Loaded required libaries')
logger.info('Initialized logger')
code = str(input('Enter code for download: '))
r = requests.get(codecs.decode('uggcf://auragnv.arg/ncv/tnyyrel/', 'rot_13') + code)
logger.info("Sent requests to the site's API")
json_data = json.loads(r.content)
logger.info('Loaded JSON data')

#----------Notifacation----------
toaster.show_toast("Started download", "N-DLer has started download on " + json_data['title']['english'], threaded=True)
logger.info('Started download on %s', json_data['title']['english'])

#----------Essential Variables----------
media_id = str(json_data['media_id'])
counter = 0

#----------Download----------
for page in json_data['images']['pages']:
	if json_data['images']['pages'][counter]['t'] == "p":
		img_type = ".png"
	else:
		img_type = ".jpg"
	r = requests.get(codecs.decode('uggcf://v.auragnv.arg/tnyyrevrf/', 'rot_13') + media_id + '/' + str(counter + 1) + img_type)		
	with open('data/' + str(counter) + img_type, 'wb+') as f:
		f.write(r.content)
		logger.info('Downloaded page ' + str((counter + 1)) + ' of ' + json_data['title']['english'])
	counter = counter + 1
	
##----------Zip compression----------
#zipobj = zipfile.ZipFile(json_data['title']['english'], 'w')
#logger.info("Created zip archive")
#path = os.getcwd() + '\\data\\'
#
#files = []
#for r, d, f in os.walk(path):
#	for file in f:
#		if ('.jpg' in file) or ('.png' in file):
#			files.append(os.path.join(r, file))
#logger.info("Scanning for files in /data")
#
#for f in file:
#	zipobj.write(f)
#logger.info("Adding file to archive")
#
#zipobj.close()
#logger.info("Archive created")