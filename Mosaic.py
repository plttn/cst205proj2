from PIL import Image, ImageDraw

#import key from untracked file
keyFile = open('key.txt', 'r')

APIkey = keyFile.read()

myImage = Image.open("davidTennant.jpg")
myImage.load()

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

myImage.show()

tileWidth = 50

#gets the number of tiles vertically
numOfTilesVert = height / tileWidth
#gets the number of tiles horizontally 
numOfTilesHoriz = width / tileWidth 

# create two dimensional array to hold crop images
tiledImage = [[for row in xrange(numOfTilesHoriz)]:for x in range(numOfTilesVert)]

# for loop that crops a copy of the image to 50 * 50
for y in range(0,numOfTilesVert): 
    tiledImage.append([])
    for x in range (0,numOfTilesHoriz):
        cropImage = myImage.crop(((x*50),(y*50),((x+1) * 50),((y+ 1) * 50))) 
        tiledImage[x][y].append(cropImage)
       
tiledImage[0][0].show()
tiledImage[numOfTilesHoriz-2][numOfTilesVert-2].show()
