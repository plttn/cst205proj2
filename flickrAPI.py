import requests

#import key from untracked file
keyFile = open('key.txt', 'r')

APIkey = keyFile.read()


# APIendpoint = 'https://api.flickr.com/services/rest/?method=flickr.test.echo&api_key=' + APIkey + '&tags=fairies'
#
# print APIendpoint
#
# searchPictures = requests.get(APIendpoint)
#
# print searchPictures.text
#
# url = 'http://placehold.it/350x150'
# response = requests.get(url, stream=True)
# with open('img.png', 'wb') as out_file:
# 	shutil.copyfileobj(response.raw, out_file)
# del response
