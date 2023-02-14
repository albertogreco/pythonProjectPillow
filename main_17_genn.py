# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Importing Image and ImageFont, ImageDraw module from PIL package

from PIL import ImageFont, ImageDraw



# import image module from pillow
from PIL import Image
# make a copy the image so that
# the original image does not get affected

myPath='/Users/francescopeluso/Documents/FRANK/LAVORO/2023-BYS/CATALOGO/'
myPathImg='/Users/francescopeluso/Documents/FRANK/LAVORO/2023-BYS/CATALOGO/IMMAGINI/'
myPathPage='/Users/francescopeluso/Documents/FRANK/LAVORO/2023-BYS/CATALOGO/PAGINE/'
myPathData='/Users/francescopeluso/Documents/FRANK/LAVORO/2023-BYS/CATALOGO/DATAFILE/'
myPathBase='/Users/francescopeluso/Documents/FRANK/LAVORO/2023-BYS/CATALOGO/BASE/'
X=0 #contatore del numero di record nel datafile
n = 100
Vett1 = [0] * n
Vett2 = [0] * n
Vett2Text = [0] * n
Vett3 = [0] * n
Vett3Text = [0] * n
Vett3TextBar = [0] * n


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
        Vett1[X] = (item[s3+1:s4])  # campo nome file.jpg
        Vett2[X] = (item[s5+1:s5+5]) # prezzo
        Vett3[X] = (item[s1+1:s2])   #codie
        #print("Vett3=", Vett3[X], X)
file.close()

#print(X)


# open the base image
#A4 300 dpi
A4X=2480
A4Y=3508
CellaX=770
CellaY=700
MargL=80 #margine left
MargS=230 #Margine superiore
StepTestoY=80
StepTestoX=150
#base map
Image0 = Image.open(myPathBase+'base-vegas.jpg')
resized_image0= Image0.resize((A4X, A4Y))
Image0copy = resized_image0


# open image and crea pages
mStep=0
mEuro="€ "
mAster="*"
for mCod in range(1, 9):

    #print("mCOD", mCod)
    #print("mStep",mStep)
    #print("X=",X)

    #1
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] =='*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image1 = Image.open(mIMG)
            resized_image1 = Image1.resize((CellaX, CellaY))
            Image1copy = resized_image1
            Vett3Text[mStep]=" "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "  # price
        else:
            mIMG=(myPathImg+Vett1[mStep])
            Image1 = Image.open(mIMG)
            resized_image1= Image1.resize((CellaX, CellaY))
            Image1copy = resized_image1
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster+Vett3[mStep]+mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG=(myPathImg+'ImageBlank.jpg')
        Image1 = Image.open(mIMG)
        resized_image1 = Image1.resize((CellaX, CellaY))
        Image1copy = resized_image1
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "

    #2
    mStep += 1

    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image2 = Image.open(mIMG)
            resized_image2 = Image2.resize((CellaX, CellaY))
            Image2copy = resized_image2
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image2 = Image.open(mIMG)
            resized_image2 = Image2.resize((CellaX, CellaY))
            Image2copy = resized_image2
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image2 = Image.open(mIMG)
        resized_image2 = Image2.resize((CellaX, CellaY))
        Image2copy = resized_image2
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "


    #3
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image3 = Image.open(mIMG)
            resized_image3 = Image3.resize((CellaX, CellaY))
            Image3copy = resized_image3
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image3 = Image.open(mIMG)
            resized_image3 = Image3.resize((CellaX, CellaY))
            Image3copy = resized_image3
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image3 = Image.open(mIMG)
        resized_image3 = Image3.resize((CellaX, CellaY))
        Image3copy = resized_image3
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "

    #4
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image4 = Image.open(mIMG)
            resized_image4 = Image4.resize((CellaX, CellaY))
            Image4copy = resized_image4
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image4 = Image.open(mIMG)
            resized_image4 = Image4.resize((CellaX, CellaY))
            Image4copy = resized_image4
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image4 = Image.open(mIMG)
        resized_image4 = Image4.resize((CellaX, CellaY))
        Image4copy = resized_image4
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "


    #5
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image5 = Image.open(mIMG)
            resized_image5 = Image5.resize((CellaX, CellaY))
            Image5copy = resized_image5
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image5 = Image.open(mIMG)
            resized_image5 = Image5.resize((CellaX, CellaY))
            Image5copy = resized_image5
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image5 = Image.open(mIMG)
        resized_image5 = Image5.resize((CellaX, CellaY))
        Image5copy = resized_image5
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "

    #6
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image6 = Image.open(mIMG)
            resized_image6 = Image6.resize((CellaX, CellaY))
            Image6copy = resized_image6
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image6 = Image.open(mIMG)
            resized_image6 = Image6.resize((CellaX, CellaY))
            Image6copy = resized_image6
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro + Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image6 = Image.open(mIMG)
        resized_image6 = Image6.resize((CellaX, CellaY))
        Image6copy = resized_image6
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "



    #7
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image7 = Image.open(mIMG)
            resized_image7 = Image7.resize((CellaX, CellaY))
            Image7copy = resized_image7
            Vett3Text[mStep] = " "
            Vett2Text[mStep] = " "
            Vett3TextBar[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image7 = Image.open(mIMG)
            resized_image7 = Image7.resize((CellaX, CellaY))
            Image7copy = resized_image7
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image7 = Image.open(mIMG)
        resized_image7 = Image7.resize((CellaX, CellaY))
        Image7copy = resized_image7
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "



    #8
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image8 = Image.open(mIMG)
            resized_image8 = Image8.resize((CellaX, CellaY))
            Image8copy = resized_image8
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image8 = Image.open(mIMG)
            resized_image8 = Image8.resize((CellaX, CellaY))
            Image8copy = resized_image8
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image8 = Image.open(mIMG)
        resized_image8 = Image8.resize((CellaX, CellaY))
        Image8copy = resized_image8
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "


    #9
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image9 = Image.open(mIMG)
            resized_image9 = Image9.resize((CellaX, CellaY))
            Image9copy = resized_image9
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image9 = Image.open(mIMG)
            resized_image9 = Image9.resize((CellaX, CellaY))
            Image9copy = resized_image9
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image9 = Image.open(mIMG)
        resized_image9 = Image9.resize((CellaX, CellaY))
        Image9copy = resized_image9
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "


    #10
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image10 = Image.open(mIMG)
            resized_image10 = Image10.resize((CellaX, CellaY))
            Image10copy = resized_image10
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image10 = Image.open(mIMG)
            resized_image10 = Image10.resize((CellaX, CellaY))
            Image10copy = resized_image10
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image10 = Image.open(mIMG)
        resized_image10 = Image10.resize((CellaX, CellaY))
        Image10copy = resized_image10
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "


    #11
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image11 = Image.open(mIMG)
            resized_image11 = Image11.resize((CellaX, CellaY))
            Image11copy = resized_image11
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image11 = Image.open(mIMG)
            resized_image11 = Image11.resize((CellaX, CellaY))
            Image11copy = resized_image11
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image11 = Image.open(mIMG)
        resized_image11 = Image11.resize((CellaX, CellaY))
        Image11copy = resized_image11
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "



    #12
    mStep += 1
    if mStep <= X:
        if Vett1[mStep] == '*':
            mIMG = (myPathImg + 'ImageBlank.jpg')
            Image12 = Image.open(mIMG)
            resized_image12 = Image12.resize((CellaX, CellaY))
            Image12copy = resized_image12
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image12 = Image.open(mIMG)
            resized_image12 = Image12.resize((CellaX, CellaY))
            Image12copy = resized_image12
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
    else:
        mIMG = (myPathImg + 'ImageBlank.jpg')
        Image12 = Image.open(mIMG)
        resized_image12 = Image12.resize((CellaX, CellaY))
        Image12copy = resized_image12
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "



    OffSet0=0
    # paste image giving dimensions (X and y)
    Image0copy.paste(Image1copy, (MargL, MargS))
    #Image0copy.paste(Image2copy, (400, MargS)
    Image0copy.paste(Image3copy, ((CellaX*2)+OffSet0, MargS))

    Image0copy.paste(Image4copy, (MargL, MargS+StepTestoY+CellaY))
    Image0copy.paste(Image5copy, ((CellaX*1)+OffSet0, MargS+StepTestoY+CellaY))
    Image0copy.paste(Image6copy, ((CellaX*2)+OffSet0, MargS+StepTestoY+CellaY))

    Image0copy.paste(Image7copy, (MargL, MargS+(StepTestoY*2)+CellaY*2))
    Image0copy.paste(Image8copy, ((CellaX*1)+OffSet0, MargS+(StepTestoY*2)+CellaY*2))
    Image0copy.paste(Image9copy, ((CellaX*2)+OffSet0, MargS+(StepTestoY*2)+CellaY*2))

    Image0copy.paste(Image10copy, (MargL, MargS+(StepTestoY*3)+CellaY*3))
    Image0copy.paste(Image11copy, ((CellaX*1)+OffSet0, MargS+(StepTestoY*3)+CellaY*3))
    Image0copy.paste(Image12copy, ((CellaX*2)+OffSet0, MargS+(StepTestoY*3)+CellaY*3))

    # save the image (page)
    Image0copy.save(myPathPage+'vegas'+str(mCod)+'.jpg')

    # creating a image object
    image = Image.open(myPathPage+'vegas'+str(mCod)+'.jpg')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(myPath+'Arial Unicode.ttf', 30)
    fontBar = ImageFont.truetype(myPath+'LibreBarcode39-Regular.ttf', 36)
    #print("start",mCod)
    mXXX=0

    if mCod==1:
        mXXX=1
    else:
        mXXX=(mCod-1)*12+1

    print("mXXX",mXXX)



    mContaText=1
    #primo rigo
    text = Vett3Text[mXXX]
    draw.text((StepTestoX, CellaY+MargS), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX]
    draw.text((StepTestoX+190, CellaY+MargS+10), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX]
    draw.text((StepTestoX+420, CellaY+MargS), text, font=font, fill=(25,0,0,255) )

    text = Vett3Text[mXXX+1]
    draw.text((StepTestoX+(CellaX*1), CellaY+MargS), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX+1]
    draw.text((StepTestoX+190+(CellaX*1), CellaY+MargS+10), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX+1]
    draw.text((StepTestoX +420+ (CellaX * 1), CellaY + MargS), text, font=font, fill=(25, 0, 0, 255))

    text = Vett3Text[mXXX+2]
    draw.text((StepTestoX+(CellaX*2), CellaY+MargS), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX+2]
    draw.text((StepTestoX+190+(CellaX*2), CellaY+MargS+10), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX+2]
    draw.text((StepTestoX+420+(CellaX*2), CellaY+MargS), text, font=font, fill=(25,0,0,255) )

    #secondo rigo
    text = Vett3Text[mXXX+3]
    draw.text( (StepTestoX, CellaY*2+MargS+StepTestoY), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX+3]
    draw.text( (StepTestoX+190, CellaY*2+MargS+StepTestoY+10), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX+3]
    draw.text( (StepTestoX+420, CellaY*2+MargS+StepTestoY), text, font=font, fill=(25,0,0,255) )

    text = Vett3Text[mXXX+4]
    draw.text((StepTestoX+(CellaX*1), CellaY*2+MargS+StepTestoY), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX+4]
    draw.text((StepTestoX+190+(CellaX*1), CellaY*2+MargS+StepTestoY+10), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX+4]
    draw.text((StepTestoX + 420+ (CellaX * 1), CellaY * 2 + MargS + StepTestoY), text, font=font, fill=(25, 0, 0, 255))

    text = Vett3Text[mXXX+5]
    draw.text((StepTestoX+(CellaX*2), CellaY*2+MargS+StepTestoY), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX+5]
    draw.text((StepTestoX+190+(CellaX*2), CellaY*2+MargS+StepTestoY+10), text, font=fontBar, fill=(25,0,0,255) )
    text= Vett2Text[mXXX+5]
    draw.text((StepTestoX + 420+ (CellaX * 2), CellaY * 2 + MargS + StepTestoY), text, font=font, fill=(25, 0, 0, 255))


    #terzo rigo
    text = Vett3Text[mXXX+6]
    draw.text((StepTestoX, CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX+6]
    draw.text((StepTestoX+190, CellaY*3+MargS+(StepTestoY*2)+10), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX+6]
    draw.text((StepTestoX +420, CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )

    text = Vett3Text[mXXX+7]
    draw.text((StepTestoX+(CellaX*1), CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )
    Vett3TextBar[mXXX+7]
    draw.text((StepTestoX+190+(CellaX*1), CellaY*3+MargS+10+(StepTestoY*2)), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX+7]
    draw.text((StepTestoX+420+(CellaX*1), CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )

    text = Vett3Text[mXXX+8]
    draw.text((StepTestoX+(CellaX*2), CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX+8]
    draw.text((StepTestoX+(CellaX*2)+190, CellaY*3+MargS+10+(StepTestoY*2)), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX+8]
    draw.text((StepTestoX+420+(CellaX*2), CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )

    #quarto riigo
    text = Vett3Text[mXXX+9]
    draw.text((StepTestoX, CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX+9]
    draw.text((StepTestoX+190, CellaY*4+MargS+10+(StepTestoY*3)), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX+9]
    draw.text((StepTestoX+420, CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )

    text = Vett3Text[mXXX+10]
    draw.text((StepTestoX+(CellaX*1), CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX+10]
    draw.text((StepTestoX+(CellaX*1)+190, CellaY*4+MargS+10+(StepTestoY*3)), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX+10]
    draw.text((StepTestoX+420+(CellaX*1), CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )

    text = Vett3Text[mXXX+11]
    draw.text((StepTestoX+(CellaX*2), CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )
    text = Vett3TextBar[mXXX+11]
    draw.text((StepTestoX+190+(CellaX*2), CellaY*4+MargS+10+(StepTestoY*3)), text, font=fontBar, fill=(25,0,0,255) )
    text=Vett2Text[mXXX+11]
    draw.text((StepTestoX+420+(CellaX*2), CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )
    #image.show()
    image.save(myPathPage + 'vegas' + str(mCod) + '.jpg')



