# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#formato a4 1654px 2339px

# import image module from pillow
from PIL import Image
# make a copy the image so that
# the original image does not get affected

#print text item on image



# open the base image


Image0 = Image.open('/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/base-vegas.jpg')
Image0copy = Image0.copy()
# open the other image
Image1 = Image.open('/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/DSCN3003-CUT.jpg')
resized_image1= Image1.resize((740, 700))
Image1copy = resized_image1
print(resized_image1.size)
#
Image2 = Image.open('/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/DSCN3003-CUT.jpg')
resized_image2 = Image2.resize((740, 700))
Image2copy = resized_image2
print(resized_image2.size)
#
Image3 = Image.open('/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/DSCN3003-CUT.jpg')
resized_image3 = Image3.resize((740, 700))
Image3copy = resized_image3
#
Image4 = Image.open('/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/DSCN3003-CUT.jpg')
resized_image4 = Image4.resize((740, 700))
Image4copy = resized_image4
#
Image5 = Image.open('/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/DSCN3003-CUT.jpg')
resized_image5 = Image5.resize((740, 700))
Image5copy = resized_image5
#
Image6 = Image.open('/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/DSCN3003-CUT.jpg')
resized_image6 = Image6.resize((740, 700))
Image6copy = resized_image6
#


Image7 = Image.open('/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/DSCN2960M-CUT.jpg')
resized_image7 = Image7.resize((1400, 2150))
Image7copy = resized_image7

#


#print(Image4.size)



# paste image giving dimensions (X and y)
Image0copy.paste(Image1copy, (180, 320))
Image0copy.paste(Image2copy, (950, 320))
Image0copy.paste(Image3copy, (1665, 320))

Image0copy.paste(Image4copy, (180, 1050))
Image0copy.paste(Image5copy, (180, 1750))
Image0copy.paste(Image6copy, (180, 2450))

Image0copy.paste(Image7copy, (950, 1050))



# save the image
Image0copy.save('/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/vegas1.jpg')

#write text items
img = Image.open("/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/vegas1.jpg")
# Importing Image and ImageFont, ImageDraw module from PIL package
from PIL import ImageFont, ImageDraw

# creating a image object
image = Image.open("/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/vegas1.jpg")

draw = ImageDraw.Draw(image)

font = ImageFont.truetype(r'/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/Arial Unicode.ttf', 30)

text = 'ART. 1234455 \nDRIVE'

draw.text((450, 900), text, font=font, fill=(25,0,0,255) )

image.show()


