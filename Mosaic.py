from PIL import Image, ImageDraw

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
    for x in range(0, width):
        for y in range(0, height):
            r,g,b =myImage.getpixel((x,y))

            #gets the average of the rgb values
            r_avg =(r+r_avg)/2
            g_avg=(g+g_avg)/2
            b_avg=(b+b_avg)/2
    #returns the average
    return (r_avg, g_avg, b_avg)

#main image
myImage = Image.open("cookieCat.png")

#gets width and height of current image
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

#sends  the image to average_color
average_color = average_image_color(myImage)

#prints the average color value
print(average_color) 
