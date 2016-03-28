from PIL import Image, ImageDraw
from flickrAPI import image_process as flickr
import os
from tint import image_tint

myImage = Image.open("davidTennant.jpg")
myImage.load()

tag = "flowers" #hardcoded flag for just now (possibly user requested list of tags)


flickr(tag) #generates 1-99 in tiles/$tag directory


#build tag list
tagList = []

tagPath = os.path.join ("tiles", tag)

for x in range(1,101):
    filePath = os.path.join(tagPath, str(x).zfill(2) + ".png")
    tagList.append(filePath)

#get width & height of main image
width,height = myImage.size

# function rounds pictures height & width to scale of 50
def roundImage(x, base = 50):
    return int(base * round(float(x)/base))

# rounds width to a multiple of 50
width = roundImage(width)
#rounds height to a multiple of 50
height = roundImage(height)

#resized main image by scale of 50
myImage = myImage.resize((width, height), Image.ANTIALIAS)


tileImage = Image.open(tagList[50])
tileImage.show()

tileWidth = 50

#gets the number of tiles vertically
numOfTilesVert = height / tileWidth
#gets the number of tiles horizontally
numOfTilesHoriz = width / tileWidth

# create two dimensional array to hold crop images
tiledImage = {}

# for loop that crops a copy of the image to 50 * 50
for y in range(0,numOfTilesVert):
    for x in range (0,numOfTilesHoriz):
        cropImage = myImage.crop(((x*50),(y*50),((x+1) * 50),((y+ 1) * 50)))
        tiledImage[x,y] = cropImage

#exampleImage = tiledImage[1,0]

#exampleImage.show()

#tiledImage[0,0].show()
# tiledImage[numOfTilesHoriz-2][numOfTilesVert].show()

#comment
