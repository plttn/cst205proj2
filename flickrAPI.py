import requests

#import key from untracked file
keyFile = open('key.txt', 'r')

APIkey = keyFile.readline().strip()


APIendpoint = 'https://api.flickr.com/services/rest/?method=flickr.test.echo&api_key=' + APIkey + '&tags=fairies'

print APIendpoint

searchPictures = requests.get(APIendpoint)

print searchPictures.text
