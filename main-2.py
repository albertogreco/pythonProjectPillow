# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# import image module from pillow
from PIL import Image
# make a copy the image so that
# the original image does not get affected

myPath='/Volumes/Samsung_T5/LAVORO-FRANK/2023-BYS/CATALOGO/'
myPathImg='/Users/francescopeluso/Documents/FRANK/LAVORO/2023-BYS/CATALOGO/IMMAGINI/'
myPathPage='/Users/francescopeluso/Documents/FRANK/LAVORO/2023-BYS/CATALOGO/PAGINE/'
myPathData='/Users/francescopeluso/Documents/FRANK/LAVORO/2023-BYS/CATALOGO/DATAFILE/'
myPathBase='/Users/francescopeluso/Documents/FRANK/LAVORO/2023-BYS/CATALOGO/BASE/'
X=0 #contatore del numero di record nel datafile
n = 100
Vett1 = [0] * n
Vett2 = [0] * n
with open(myPathData+"gioielli_ESPORTAZIONE_eCOMM_CAT.csv") as file:
    for item in file:
        #print(item)
        s1 = (item.find(";"))
        s2 = (item.find(";", s1 + 1))
        s3 = (item.find(";", s2 + 1))
        s4 = (item.find(";", s3 + 1))
        s5 = (item.find(";", s4 + 1))
        #print (s1,s2, s3, s4, s5)
        X=X+1
        Vett1[X]=(item[s3+1:s4])
        Vett2[X]=(item[s5+1:s5+5])
        #rint(Vett1[X], Vett2[X])
file.close()

print(X)


# open the base image
#A4 300 dpi
A4X=2480
A4Y=3508
CellaX=770
CellaY=700
MargL=50 #margine left
MargS=200 #Margine superiore
StepTestoY=100
StepTestoX=150
#base map
Image0 = Image.open(myPathBase+'base-vegas.jpg')
resized_image0= Image0.resize((A4X, A4Y))
Image0copy = resized_image0


# open image and crea pages
mStep=0
for mCod in range(1, 9):

    print("mCOD", mCod)
    print("mStep",mStep)
    print("X=",X)

    #1
    mStep += 1
    print("mStep2", mStep)

    if mStep <= X:
        if Vett1[mStep] =='*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image1 = Image.open(mIMG)
            resized_image1 = Image1.resize((CellaX, CellaY))
            Image1copy = resized_image1
        else:
            mIMG=(myPathImg+Vett1[mStep])
            Image1 = Image.open(mIMG)
            resized_image1= Image1.resize((CellaX, CellaY))
            Image1copy = resized_image1
    else:
        mIMG=(myPathImg+'ImageBlank.jpg')
        Image1 = Image.open(mIMG)
        resized_image1 = Image1.resize((CellaX, CellaY))
        Image1copy = resized_image1

    #2
    mStep += 1
    print("mStep3", mStep)
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image2 = Image.open(mIMG)
            resized_image2 = Image2.resize((CellaX, CellaY))
            Image2copy = resized_image2
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image2 = Image.open(mIMG)
            resized_image2 = Image2.resize((CellaX, CellaY))
            Image2copy = resized_image2
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image2 = Image.open(mIMG)
        resized_image2 = Image2.resize((CellaX, CellaY))
        Image2copy = resized_image2


    #3
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image3 = Image.open(mIMG)
            resized_image3 = Image3.resize((CellaX, CellaY))
            Image3copy = resized_image3
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image3 = Image.open(mIMG)
            resized_image3 = Image3.resize((CellaX, CellaY))
            Image3copy = resized_image3
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image3 = Image.open(mIMG)
        resized_image3 = Image3.resize((CellaX, CellaY))
        Image3copy = resized_image3

    #4
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image4 = Image.open(mIMG)
            resized_image4 = Image4.resize((CellaX, CellaY))
            Image4copy = resized_image4
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image4 = Image.open(mIMG)
            resized_image4 = Image4.resize((CellaX, CellaY))
            Image4copy = resized_image4
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image4 = Image.open(mIMG)
        resized_image4 = Image4.resize((CellaX, CellaY))
        Image4copy = resized_image4


    #5
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image5 = Image.open(mIMG)
            resized_image5 = Image5.resize((CellaX, CellaY))
            Image5copy = resized_image5
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image5 = Image.open(mIMG)
            resized_image5 = Image5.resize((CellaX, CellaY))
            Image5copy = resized_image5
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image5 = Image.open(mIMG)
        resized_image5 = Image5.resize((CellaX, CellaY))
        Image5copy = resized_image5

    #6
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image6 = Image.open(mIMG)
            resized_image6 = Image6.resize((CellaX, CellaY))
            Image6copy = resized_image6
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image6 = Image.open(mIMG)
            resized_image6 = Image6.resize((CellaX, CellaY))
            Image6copy = resized_image6
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image6 = Image.open(mIMG)
        resized_image6 = Image6.resize((CellaX, CellaY))
        Image6copy = resized_image6



    #7
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image7 = Image.open(mIMG)
            resized_image7 = Image7.resize((CellaX, CellaY))
            Image7copy = resized_image7
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image7 = Image.open(mIMG)
            resized_image7 = Image7.resize((CellaX, CellaY))
            Image7copy = resized_image7
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image7 = Image.open(mIMG)
        resized_image7 = Image7.resize((CellaX, CellaY))
        Image7copy = resized_image7



    #8
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image8 = Image.open(mIMG)
            resized_image8 = Image8.resize((CellaX, CellaY))
            Image8copy = resized_image8
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image8 = Image.open(mIMG)
            resized_image8 = Image8.resize((CellaX, CellaY))
            Image8copy = resized_image8
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image8 = Image.open(mIMG)
        resized_image8 = Image8.resize((CellaX, CellaY))
        Image8copy = resized_image8


    #9
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image9 = Image.open(mIMG)
            resized_image9 = Image9.resize((CellaX, CellaY))
            Image9copy = resized_image9
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image9 = Image.open(mIMG)
            resized_image9 = Image9.resize((CellaX, CellaY))
            Image9copy = resized_image9
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image9 = Image.open(mIMG)
        resized_image9 = Image9.resize((CellaX, CellaY))
        Image9copy = resized_image9


    #10
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image10 = Image.open(mIMG)
            resized_image10 = Image10.resize((CellaX, CellaY))
            Image10copy = resized_image10
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image10 = Image.open(mIMG)
            resized_image10 = Image10.resize((CellaX, CellaY))
            Image10copy = resized_image10
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image10 = Image.open(mIMG)
        resized_image10 = Image10.resize((CellaX, CellaY))
        Image10copy = resized_image10


    #11
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image11 = Image.open(mIMG)
            resized_image11 = Image11.resize((CellaX, CellaY))
            Image11copy = resized_image11
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image11 = Image.open(mIMG)
            resized_image11 = Image11.resize((CellaX, CellaY))
            Image11copy = resized_image11
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image11 = Image.open(mIMG)
        resized_image11 = Image11.resize((CellaX, CellaY))
        Image11copy = resized_image11



    #12
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image12 = Image.open(mIMG)
            resized_image12 = Image12.resize((CellaX, CellaY))
            Image12copy = resized_image12
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image12 = Image.open(mIMG)
            resized_image12 = Image12.resize((CellaX, CellaY))
            Image12copy = resized_image12
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image12 = Image.open(mIMG)
        resized_image12 = Image12.resize((CellaX, CellaY))
        Image12copy = resized_image12




    # paste image giving dimensions (X and y)
    Image0copy.paste(Image1copy, (MargL, MargS))
    Image0copy.paste(Image2copy, ((CellaX*1), MargS))
    Image0copy.paste(Image3copy, ((CellaX*2), MargS))
    #print((CellaX*2))
    Image0copy.paste(Image4copy, (MargL, MargS+StepTestoY+CellaY))
    Image0copy.paste(Image5copy, ((CellaX*1), MargS+StepTestoY+CellaY))
    Image0copy.paste(Image6copy, ((CellaX*2), MargS+StepTestoY+CellaY))

    Image0copy.paste(Image7copy, (MargL, MargS+(StepTestoY*2)+CellaY*2))
    Image0copy.paste(Image8copy, ((CellaX*1), MargS+(StepTestoY*2)+CellaY*2))
    Image0copy.paste(Image9copy, ((CellaX*2), MargS+(StepTestoY*2)+CellaY*2))

    Image0copy.paste(Image10copy, (MargL, MargS+(StepTestoY*3)+CellaY*3))
    Image0copy.paste(Image11copy, ((CellaX*1), MargS+(StepTestoY*3)+CellaY*3))
    Image0copy.paste(Image12copy, ((CellaX*2), MargS+(StepTestoY*3)+CellaY*3))

    # save the image
    Image0copy.save(myPathPage+'vegas'+str(mCod)+'.jpg')

    #write text items
    img = Image.open(myPathPage+"vegas1.jpg")
    # Importing Image and ImageFont, ImageDraw module from PIL package
    from PIL import ImageFont, ImageDraw

    # creating a image object
    image = Image.open(myPathPage+"vegas1.jpg")

    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(myPath+'Arial Unicode.ttf', 30)

    text = 'ART. 1234455'

    draw.text((StepTestoX, CellaY+MargS), text, font=font, fill=(25,0,0,255) )

    #image.show()



