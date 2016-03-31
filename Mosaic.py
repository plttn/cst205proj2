from PIL import Image, ImageDraw
from flickrAPI import image_process as flickr
import os
from tint import image_tint
import pprint

#import key from untracked file
#keyFile = open('key.txt', 'r')
#APIkey = keyFile.readline().strip()
#print APIkey

def average_image_color(myImage):
#get width & height of image sent in
    width,height = myImage.size
    r_avg =0
    g_avg=0
    b_avg=0
    #goes through checking the rgb values in the image demensions and finding average
    for y in range(0, height):
        for x in range(0, width):
            r,g,b =myImage.getpixel((x,y))

            #gets the average of the rgb values
            r_avg =(r+r_avg)
            g_avg =(g+g_avg)
            b_avg =(b+b_avg)
    total = height * width
    #returns the average
    return (r_avg/total, g_avg/total, b_avg/total)

#main image
myImage = Image.open("davidTennant.jpg")

tag = "flowers" #hardcoded flag for just now (possibly user requested list of tags)

#flickr(tag) #generates 1-99 in tiles/$tag directory

#build tag list
tagList = []

tagPath = os.path.join ("tiles", tag)

for x in range(1,101):
    filePath = os.path.join(tagPath, str(x).zfill(2) + ".png")
    tagList.append(filePath)

width,height = myImage.size

#resizing the image
# function rounds pictures height & width to scale of 50
def roundImage(x, base = 50):
    return int(base * round(float(x)/base))

# rounds width to a multiple of 50
width = roundImage(width)
#rounds height to a multiple of 50
height = roundImage(height)

#resized main image by scale of 50
myImage = myImage.resize((width, height), Image.ANTIALIAS)


tileWidth = 25

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

averageTileColors = {}


for y in range(0, numOfTilesVert): #this is the user provided image
    for x in range(0, numOfTilesHoriz):
        averageColor = average_image_color(tiledImage[x,y]) #gets the average color of the tile
        averageTileColors[x,y] = averageColor #stores it in the matrix

# calculate mosaic averages
averageMosaicColors = [] # these are the downloaded pictures
for j in range(0, len(tagList)):
    currentImage = Image.open(tagList[j])
    averageMosaicColors.append(average_image_color(currentImage))


def margin_of_error(value1, value2):
    if value1 == 0 or value2 == 0:
        return 0

    difference = value1-value2
    difference = difference / value1
    difference = difference * 100
    return difference
    pass


mosaicImageMatrix = {}

for y in range(0, numOfTilesVert):
    for x in range(0, numOfTilesHoriz):
        print "checking tile: ", x, y
        checkColor = averageTileColors[x, y]
        closestMargin = [10, 10, 10]
        for z in range(0, len(tagList)):
            currentTileColor = averageMosaicColors[z]
            currentMargin = (margin_of_error(checkColor[0], averageMosaicColors[z][0]), margin_of_error(checkColor[1], averageMosaicColors[z][1]), margin_of_error(checkColor[2], averageMosaicColors[z][2]))
            if (currentMargin[0] < 5 and currentMargin[1] < 5 and currentMargin[2] < 5): #this is within 5 percent of the original
                if currentMargin[0] < closestMargin[1] and currentMargin[1] < closestMargin[1] and currentMargin[2] < closestMargin[2]:
                    currentTileWinner = z;
                    closestMargin[0] = currentMargin[0]
                    closestMargin[1] = currentMargin[1]
                    closestMargin[2] = currentMargin[2]
                    print "found a new tile winner ", z
        if closestMargin == [10, 10 ,10]:
            abc = 1    #we didn't find a close match, tint a tile instead
        else:
            currentTileWinner = z + 1;
            mosaicImageMatrix[x, y] = currentTileWinner; #store tile index in position it needs to be in matrix


#pprint.pprint(mosaicImageMatrix)
#prints the average color value
#print(average_color)
