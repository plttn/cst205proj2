from PIL import Image

#import key from untracked file
keyFile = open('key.txt', 'r')

APIkey = keyFile.read()

print APIkey

myImage = Image.open("davidTennant.jpg")
myImage.load()
width = 500
height = 325
size = (50, 50)
myImage = myImage.resize((500, height), Image.ANTIALIAS)
myImage.show()

tileWidth = 50
numOfTilesVert = height / tileWidth
numOfTilesHoriz = width / tileWidth
print numOfTiles

#tile[10][10]
#for y in range(10)
#    for x in range(10)
