import requests
import re
from PIL import Image
from StringIO import StringIO
import os


#import key from untracked file
keyFile = open('key.txt', 'r')
APIkey = keyFile.readline().strip()

def image_process( tag ):
	APIendpoint = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=' + APIkey + '&tags=' + tag
	searchResults = requests.get(APIendpoint)

	ids     = re.findall(r'id=\"(.+?)\"', searchResults.text)
	secrets = re.findall(r'secret=\"(.+?)\"', searchResults.text)
	farms   = re.findall(r'farm=\"(.+?)\"', searchResults.text)
	servers = re.findall(r'server=\"(.+?)\"', searchResults.text)

	photoURLs = []

	for i, c, f, r in zip(ids, secrets, farms, servers):
		photoURLs.append('https://farm' + f + '.staticflickr.com/' + r + '/' + i + '_' + c +'.jpg')

	dirName = os.path.join ("tiles", tag)

	if not os.path.exists(dirName):
		os.makedirs(dirName)


	increment = 1
	for url in photoURLs:
		r = requests.get(url)
		image = Image.open(StringIO(r.content))
		path = os.path.join(dirName, str(increment)) + ".png"
		image = image.resize((25,25))
		image.save(path, "PNG")
		increment += 1
