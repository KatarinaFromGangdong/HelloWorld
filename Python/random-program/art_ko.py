from PIL import Image, ImageDraw, ImageFont
import math

# chars = "#Wo- "[::-1]
chars = "10"[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = 0.4

oneCharWidth = 8
oneCharHeight = 18


def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]


text_file = ("Output.txt", "w")

filePath = 'sample-image'
imageName = (f'{filePath}.JPEG')

im = Image.open(imageName)

fnt = ImageFont.truetype('C://Windows//Font//lucon.ttf', 35)

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height *
               (oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new(
    'RGB', (oneCharWidth*width, oneCharHeight*height), color=(0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        # text_file.__new__(getChar(h))
        # text_file.write(getChar(h))
        d.text((j*oneCharWidth, i*oneCharHeight),
               getChar(h), font=fnt, fill=(r, g, b))
    # text_file.write('\n')
outputImage.save(f'{filePath}.png')
