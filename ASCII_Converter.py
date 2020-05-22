#Importing the assets
from PIL import Image, ImageDraw, ImageFont
import math
from time import sleep

#Introduction
print('''
            _____  _____ _____ _____            
     /\    / ____|/ ____|_   _|_   _|           
    /  \  | (___ | |      | |   | |             
   / /\ \  \___ \| |      | |   | |             
  / ____ \ ____) | |____ _| |_ _| |_            
 /_/___ \_\_____/ \_____|_____|_____|           
 |_   _|                                        
   | |  _ __ ___   __ _  __ _  ___              
   | | | '_ ` _ \ / _` |/ _` |/ _ \             
  _| |_| | | | | | (_| | (_| |  __/             
 |_____|_| |_| |_|\__,_|\__, |\___|             
  / ____|                __/ |   | |            
 | |     ___  _ ____   _|___/_ __| |_ ___ _ __  
 | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__| 
 | |___| (_) | | | \ V /  __/ |  | ||  __/ |    
  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|    
_________________________________________________                                               
                                                  
Warning: if improper or nonexistent filenames and values are inputted
		 the program will close''')

#Choose the image to convert here
print('\n' + 'The image must come from the resources folder that is in the same location as this program' + '\n')
print('Input the image using the exact filepath:')
newimage = input()
image = Image.open(newimage)

#Choose the image scale
print("Choose the ratio to scale the image (1.0 = same size, 0.5 = 1/2 size):")
scale = input()
scale = float(scale)
#A 4k image scaled to 1920x600 (0.5) took 3 minutes to render

#ASCII substitute array
charWidth = 10
charHeight = 18

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"[::-1]
chararray = list(chars)
arraylength = len(chararray)
interval = arraylength/256

#Substitution function
def getChar(inputInt):
	return chararray[math.floor(inputInt*interval)]

#Creating the text file
textFile = open('output.txt', 'w')

#Loading and formatting the image
print('Image loaded!')
imageWidth, imageHeight = image.size
print('Initial image dimensions: %s x %s' % (imageWidth, imageHeight))

image = image.resize((int(scale*imageWidth), int(scale*imageHeight*(charWidth/charHeight))), Image.NEAREST)
scaledimageWidth, scaledimageHeight = image.size
print('Scaled image dimensions: %s x %s' % (scaledimageWidth, scaledimageHeight))
pixels = image.load()

#Creating the output image and the font to be used
outputImage = Image.new('RGB', (charWidth*scaledimageWidth, charHeight*scaledimageHeight), color = (75,75,75))
finalImage = ImageDraw.Draw(outputImage)
style = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf', 16)

#Running through the dimensions
print('Parsing pixel data and substituting characters...  (this may take a while!)')
for i in range(scaledimageHeight):
	for j in range(scaledimageWidth):

		#Retrieving pixel RGB data
		r,g,b = pixels[j, i]

		#Converting to brightness
		bright = int(math.sqrt((0.241*(r **2))+(0.691*(g **2))+(0.068*(b **2))))

		#Subbing brightness into the picture
		pixels[j, i] = (bright, bright, bright)

		#Substituting ASCII characters
		textFile.write(getChar(bright))

		#Making the image
		finalImage.text((j*charWidth, i*charHeight), getChar(bright), font = style, fill = (r,g,b))

	#Writing a new line	
	textFile.write('\n')

#Saving the image
outputImage.save('output.jpg')
print('Image creation completed!')
sleep(0.5)
print('\n' + '''The new image was saved as output.jpg and the raw text was created at output.txt
The program will close in 10 seconds.''')
sleep(10)





