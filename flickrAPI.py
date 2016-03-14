import requests
import re


#import key from untracked file
keyFile = open('key.txt', 'r')
APIkey = keyFile.readline().strip()

def SearchFlickr( tag ):
	APIendpoint = 'https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=' + APIkey + '&tags=' + tag
	searchResults = requests.get(APIendpoint)

	ids     = re.findall(r'id=\"(.+?)\"', searchResults.text)
	secrets = re.findall(r'secret=\"(.+?)\"', searchResults.text)
	farms   = re.findall(r'farm=\"(.+?)\"', searchResults.text)
	servers = re.findall(r'server=\"(.+?)\"', searchResults.text)

	photoURLs = []

	for i, c, f, r in zip(ids, secrets, farms, servers):
		photoURLs.append('https://farm' + f + '.staticflickr.com/' + r + '/' + i + '_' + c +'.jpg')

	for url in photoURLs:
		print url
