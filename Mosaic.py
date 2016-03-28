from PIL import Image, ImageDraw

#import key from untracked file
#keyFile = open('key.txt', 'r')

#APIkey = keyFile.readline().strip()

#print APIkey
#pixels = myImage.load()
def average_image_color(myImage):
    
#get width & height of image sent in
    width,height = myImage.size
    r_avg =0
    g_avg=0
    b_avg=0
    for x in range(0, width):
        for y in range(0, height):
            r,g,b =myImage.getpixel((x,y))
            r_avg =(r+r_avg)/2
            g_avg=(g+g_avg)/2
            b_avg=(b+b_avg)/2
    return (r_avg, g_avg, b_avg)

#creates image
myImage = Image.open("cookieCat.png")
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

tileWidth = 50

average_color = average_image_color(myImage)

print(average_color) 
