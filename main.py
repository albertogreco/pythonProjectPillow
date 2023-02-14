# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# Importing Image and ImageFont, ImageDraw module from PIL package

# import image module from pillow
from PIL import Image
from PIL import ImageFont, ImageDraw

# Importing library
import qrcode


# make a copy the image so that
# the original image does not get affected

myBase='/Users/francescopeluso/Documents/FRANK/LAVORO/2023-BYS'
myPath=myBase+'/CATALOGO/'
myPathImg=myBase+'/CATALOGO/IMMAGINI/'
myPathImgQr=myBase+'/CATALOGO/QR/'
myPathPage=myBase+'/CATALOGO/PAGINE/'
myPathData=myBase+'/CATALOGO/DATAFILE/'
myPathBase=myBase+'/CATALOGO/BASE/'
myFileName="file_py_test.txt"

X=0 #contatore del numero di record nel datafile
mNumGioie=12  #numero gioielli per pagina

#function
def my_functionQr(mCodart, mImageN):
    # Encoding data using make()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=4,
    )
    #
    qr.add_data(mCodart)
    qr.make()
    #img = qr.make_image(fill_color="red", back_color="#23dda0")
    img = qr.make_image()
    img.save(myPathImgQr + mCodart+'.png')

    # Saving as an image file

with open(myPathData+myFileName) as file:
    for item in file:
        X=X+1
        #print("X=",X)
file.close()
mPages=X/mNumGioie
#print (mPages-int(mPages))
if (mPages-int(mPages)) >0:
    mPages=int(mPages)+1


mPages=int(mPages)
print("Catalogo di:",mPages," pagine")
#n = X+1
n=X*mNumGioie
#print("n=", n)
Vett1 = ['*'] * n
Vett2 = ['*'] * n
Vett2Text = ['*'] * n
Vett3 = ['*'] * n
Vett3Text = ['*'] * n
Vett3TextBar = ['*'] * n

X=0
with open(myPathData+myFileName) as file:
    for item in file:
        # print("item=",item)
        s1 = (item.find(";"))
        s2 = (item.find(";", s1 + 1))
        s3 = (item.find(";", s2 + 1))
        s4 = (item.find(";", s3 + 1))
        s5 = (item.find(";", s4 + 1))
        s6 = (item.find(";", s5 + 1))
        s7 = (item.find(";", s6 + 1))
        #print (s1,s2, s3, s4, s5)
        X=X+1
        Vett1[X] = (item[s2+1:s3])  # campo nome file.jpg
        Vett2[X] = (item[s6+1:s7]) # prezzo
        Vett3[X] = (item[0:s1])   #codiCe
        #print(Vett2[X])
file.close()

# open the base image
#A4 300 dpi
A4X=2480
A4Y=3508
CellaX=720
CellaY=720
ImgX=700
ImgY=700
MargL=120 #margine left
MargS=130 #Margine superiore
StepTestoY=80
StepTestoX=150
#base map
Image0 = Image.open(myPathBase+'base.jpg')
resized_image0= Image0.resize((A4X, A4Y))
Image0copy = resized_image0

# open image and crea pages
mStep=0
mEuro="€ "
mAster="*"

for mCod in range(1, mPages+1):

    #1
    mStep += 1
    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image1 = Image.open(mIMG)
            resized_image1 = Image1.resize((ImgX,ImgY))
            Image1copy = resized_image1
            Vett3Text[mStep]=" "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "  # price
            mIMGqr1 = Image.open(myPathBase + 'blankQR.png')
        else:

            mIMG=(myPathImg+Vett1[mStep])
            Image1 = Image.open(mIMG)
            resized_image1= Image1.resize((ImgX,ImgY))
            Image1copy = resized_image1
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster+Vett3[mStep]+mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            # print ("codart",Vett3Text[mStep])
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr1 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')


    else:
        mIMG=(myPathBase + 'ImageBlank.jpg')
        Image1 = Image.open(mIMG)
        resized_image1 = Image1.resize((ImgX,ImgY))
        Image1copy = resized_image1
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "
        mIMGqr1 = Image.open(myPathBase + 'blankQR.png')

    #2
    mStep += 1

    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image2 = Image.open(mIMG)
            resized_image2 = Image2.resize((ImgX,ImgY))
            Image2copy = resized_image2
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
            mIMGqr2 = Image.open(myPathBase + 'blankQR.png')
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image2 = Image.open(mIMG)
            resized_image2 = Image2.resize((ImgX,ImgY))
            Image2copy = resized_image2
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr2 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')
    else:
        mIMG = (myPathBase+ 'ImageBlank.jpg')
        Image2 = Image.open(mIMG)
        resized_image2 = Image2.resize((ImgX,ImgY))
        Image2copy = resized_image2
        Vett3Text[mStep] = " "
        Vett3TextBar[mStep] = " "
        Vett2Text[mStep] = " "
        mIMGqr2 = Image.open(myPathBase + 'blankQR.png')


    #3
    mStep += 1
    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')

            Image3 = Image.open(mIMG)
            resized_image3 = Image3.resize((ImgX,ImgY))
            Image3copy = resized_image3
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
            mIMGqr3 = Image.open(myPathBase + 'blankQR.png')
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image3 = Image.open(mIMG)
            resized_image3 = Image3.resize((ImgX,ImgY))
            Image3copy = resized_image3
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr3 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')
    else:
        mIMG = (myPathBase + 'ImageBlank.jpg')
        Image3 = Image.open(mIMG)
        resized_image3 = Image3.resize((ImgX,ImgY))
        Image3copy = resized_image3
        mIMGqr3 = Image.open(myPathBase + 'blankQR.png')


    #4
    mStep += 1
    if mStep <= X:
        if Vett3[mStep] == '':

            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image4 = Image.open(mIMG)
            resized_image4 = Image4.resize((ImgX,ImgY))
            Image4copy = resized_image4
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
            mIMGqr4 = Image.open(myPathBase + 'blankQR.png')
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image4 = Image.open(mIMG)
            resized_image4 = Image4.resize((ImgX,ImgY))
            Image4copy = resized_image4
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr4 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')
    else:
        mIMG = (myPathBase + 'ImageBlank.jpg')
        Image4 = Image.open(mIMG)
        resized_image4 = Image4.resize((ImgX,ImgY))
        Image4copy = resized_image4
        mIMGqr4 = Image.open(myPathBase + 'blankQR.png')



    #5
    mStep += 1
    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image5 = Image.open(mIMG)
            resized_image5 = Image5.resize((ImgX,ImgY))
            Image5copy = resized_image5
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
            mIMGqr5 = Image.open(myPathBase + 'blankQR.png')

        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image5 = Image.open(mIMG)
            resized_image5 = Image5.resize((ImgX,ImgY))
            Image5copy = resized_image5
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr5 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')
    else:
        mIMG = (myPathBase + 'ImageBlank.jpg')
        Image5 = Image.open(mIMG)
        resized_image5 = Image5.resize((ImgX,ImgY))
        Image5copy = resized_image5
        mIMGqr5 = Image.open(myPathBase + 'blankQR.png')


    #6
    mStep += 1
    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image6 = Image.open(mIMG)
            resized_image6 = Image6.resize((ImgX,ImgY))
            Image6copy = resized_image6
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
            mIMGqr6 = Image.open(myPathBase + 'blankQR.png')
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image6 = Image.open(mIMG)
            resized_image6 = Image6.resize((ImgX,ImgY))
            Image6copy = resized_image6
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro + Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr6 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')
    else:
        mIMG = (myPathBase + 'ImageBlank.jpg')
        Image6 = Image.open(mIMG)
        resized_image6 = Image6.resize((ImgX,ImgY))
        Image6copy = resized_image6
        mIMGqr6 = Image.open(myPathBase + 'blankQR.png')


    #7
    mStep += 1
    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image7 = Image.open(mIMG)
            resized_image7 = Image7.resize((ImgX,ImgY))
            Image7copy = resized_image7
            Vett3Text[mStep] = " "
            Vett2Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            mIMGqr7 = Image.open(myPathBase + 'blankQR.png')
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image7 = Image.open(mIMG)
            resized_image7 = Image7.resize((ImgX,ImgY))
            Image7copy = resized_image7
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr7 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')
    else:
        mIMG = (myPathBase + 'ImageBlank.jpg')
        Image7 = Image.open(mIMG)
        resized_image7 = Image7.resize((ImgX,ImgY))
        Image7copy = resized_image7
        mIMGqr7 = Image.open(myPathBase + 'blankQR.png')




    #8
    mStep += 1
    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image8 = Image.open(mIMG)
            resized_image8 = Image8.resize((ImgX,ImgY))
            Image8copy = resized_image8
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
            mIMGqr8 = Image.open(myPathBase + 'blankQR.png')
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image8 = Image.open(mIMG)
            resized_image8 = Image8.resize((ImgX,ImgY))
            Image8copy = resized_image8
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr8 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')
    else:
        mIMG = (myPathBase + 'ImageBlank.jpg')
        Image8 = Image.open(mIMG)
        resized_image8 = Image8.resize((ImgX,ImgY))
        Image8copy = resized_image8
        mIMGqr8 = Image.open(myPathBase + 'blankQR.png')



    #9
    mStep += 1
    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image9 = Image.open(mIMG)
            resized_image9 = Image9.resize((ImgX,ImgY))
            Image9copy = resized_image9
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
            mIMGqr9 = Image.open(myPathBase + 'blankQR.png')
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image9 = Image.open(mIMG)
            resized_image9 = Image9.resize((ImgX,ImgY))
            Image9copy = resized_image9
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr9 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')
    else:
        mIMG = (myPathBase + 'ImageBlank.jpg')
        Image9 = Image.open(mIMG)
        resized_image9 = Image9.resize((ImgX,ImgY))
        Image9copy = resized_image9
        mIMGqr9 = Image.open(myPathBase + 'blankQR.png')



    #10
    mStep += 1
    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image10 = Image.open(mIMG)
            resized_image10 = Image10.resize((ImgX,ImgY))
            Image10copy = resized_image10
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
            mIMGqr10 = Image.open(myPathBase+ 'blankQR.png')
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image10 = Image.open(mIMG)
            resized_image10 = Image10.resize((ImgX,ImgY))
            Image10copy = resized_image10
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr10 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')
    else:
        mIMG = (myPathBase + 'ImageBlank.jpg')
        Image10 = Image.open(mIMG)
        resized_image10 = Image10.resize((ImgX,ImgY))
        Image10copy = resized_image10
        mIMGqr10 = Image.open(myPathBase+ 'blankQR.png')




    #11
    mStep += 1
    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image11 = Image.open(mIMG)
            resized_image11 = Image11.resize((ImgX,ImgY))
            Image11copy = resized_image11
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
            mIMGqr11 = Image.open(myPathBase+ 'blankQR.png')
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image11 = Image.open(mIMG)
            resized_image11 = Image11.resize((ImgX,ImgY))
            Image11copy = resized_image11
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr11 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')
    else:
        mIMG = (myPathBase + 'ImageBlank.jpg')
        Image11 = Image.open(mIMG)
        resized_image11 = Image11.resize((ImgX,ImgY))
        Image11copy = resized_image11
        mIMGqr11 = Image.open(myPathBase+ 'blankQR.png')




    #12
    mStep += 1

    if mStep <= X:
        if Vett3[mStep] == '':
            mIMG = (myPathBase + 'ImageBlank.jpg')
            Image12 = Image.open(mIMG)
            resized_image12 = Image12.resize((ImgX,ImgY))
            Image12copy = resized_image12
            Vett3Text[mStep] = " "
            Vett3TextBar[mStep] = " "
            Vett2Text[mStep] = " "
            mIMGqr12 = Image.open(myPathBase+ 'blankQR.png')
        else:
            mIMG = (myPathImg + Vett1[mStep])
            Image12 = Image.open(mIMG)
            resized_image12 = Image12.resize((ImgX,ImgY))
            Image12copy = resized_image12
            Vett3Text[mStep] = Vett3[mStep]
            Vett3TextBar[mStep] = mAster + Vett3[mStep] + mAster
            Vett2Text[mStep] = mEuro+Vett2[mStep]
            my_functionQr(Vett3Text[mStep],"")
            mIMGqr12 = Image.open(myPathImgQr + Vett3Text[mStep]+'.png')


    else:
        mIMG = (myPathBase + 'ImageBlank.jpg')
        Image12 = Image.open(mIMG)
        resized_image12 = Image12.resize((ImgX,ImgY))
        Image12copy = resized_image12
        mIMGqr12 = Image.open(myPathBase+ 'blankQR.png')





    # paste image giving dimensions (X and y)
    OffSet0=60

    Image0copy.paste(Image1copy, (MargL, MargS))
    Image0copy.paste(Image2copy, ((CellaX*1)+MargL+OffSet0, MargS))
    Image0copy.paste(Image3copy, ((CellaX*2)+MargL+OffSet0*2, MargS))


    Image0copy.paste(Image4copy, (MargL, MargS+StepTestoY+CellaY))
    Image0copy.paste(Image5copy, ((CellaX*1)+MargL+OffSet0, MargS+StepTestoY+CellaY))
    Image0copy.paste(Image6copy, ((CellaX*2)+MargL+OffSet0*2, MargS+StepTestoY+CellaY))

    Image0copy.paste(Image7copy, (MargL, MargS+(StepTestoY*2)+CellaY*2))
    Image0copy.paste(Image8copy, ((CellaX*1)+MargL+OffSet0, MargS+(StepTestoY*2)+CellaY*2))
    Image0copy.paste(Image9copy, ((CellaX*2)+MargL+OffSet0*2, MargS+(StepTestoY*2)+CellaY*2))

    Image0copy.paste(Image10copy, (MargL, MargS+(StepTestoY*3)+CellaY*3))
    Image0copy.paste(Image11copy, ((CellaX*1)+MargL+OffSet0, MargS+(StepTestoY*3)+CellaY*3))
    Image0copy.paste(Image12copy, ((CellaX * 2)+MargL+OffSet0*2, MargS + (StepTestoY * 3) + CellaY * 3))

    #qrcode

    Image0copy.paste(mIMGqr1, (180, 810))
    Image0copy.paste(mIMGqr2, (960, 810))
    Image0copy.paste(mIMGqr3, (1740, 810))

    #secondo rigo
    Image0copy.paste(mIMGqr4, (180, 1610))
    Image0copy.paste(mIMGqr5, (960, 1610))
    Image0copy.paste(mIMGqr6, (1740, 1610))

    #terzo rigo
    Image0copy.paste(mIMGqr7, (180, 2410))
    Image0copy.paste(mIMGqr8, (960, 2410))
    Image0copy.paste(mIMGqr9, (1740, 2410))

    #quarto rigo
    Image0copy.paste(mIMGqr10, (180, 3210))
    Image0copy.paste(mIMGqr11, (960, 3210))
    Image0copy.paste(mIMGqr12, (1740, 3210))

    #fine qrcode





    print("Page N. ",mCod,mStep, X)

    # save the image (page)
    Image0copy.save(myPathPage+'bys'+str(mCod)+'.jpg')
    #Image0copy.show()
    # creating a image object
    image = Image.open(myPathPage+'bys'+str(mCod)+'.jpg')
    draw = ImageDraw.Draw(image)

    font = ImageFont.truetype(myPath+'Arial Unicode.ttf', 36)
    fontBar = ImageFont.truetype(myPath+'LibreBarcode39-Regular.ttf', 36)
    #print("start",mCod)
    mXXX=0

    if mCod==1:
        mXXX=1
    else:
        mXXX=(mCod-1)*12+1




    OffSet1=350
    mContaText=1
    #primo rigo
    text = Vett3Text[mXXX]
    draw.text((360, CellaY+MargS), text, font=font, fill=(25,0,0,255) )
    text=Vett2Text[mXXX]
    draw.text((570, CellaY+MargS), text, font=font, fill=(25,0,0,255) )

    if (mXXX+1) <= X:
        text = Vett3Text[mXXX+1]
        draw.text((1150, CellaY+MargS), text, font=font, fill=(25,0,0,255) )
        text=Vett2Text[mXXX+1]
        draw.text((1360, CellaY + MargS), text, font=font, fill=(25, 0, 0, 255))

    if (mXXX+2) <= X:
        text = Vett3Text[mXXX+2]
        draw.text((1930, CellaY+MargS), text, font=font, fill=(25,0,0,255) )
        text=Vett2Text[mXXX+2]
        draw.text((2140, CellaY+MargS), text, font=font, fill=(25,0,0,255) )

    #secondo rigo
    if (mXXX+3) <= X:
        text = Vett3Text[mXXX+3]
        draw.text( (360, CellaY*2+MargS+StepTestoY), text, font=font, fill=(25,0,0,255) )
        #text = Vett3TextBar[mXXX+3]
        #draw.text( (StepTestoX+190, CellaY*2+MargS+StepTestoY+10), text, font=fontBar, fill=(25,0,0,255) )
        text=Vett2Text[mXXX+3]
        draw.text( (570, CellaY*2+MargS+StepTestoY), text, font=font, fill=(25,0,0,255) )

    if (mXXX+4) <= X:
        text = Vett3Text[mXXX+4]
        draw.text((1150, CellaY*2+MargS+StepTestoY), text, font=font, fill=(25,0,0,255) )
        text=Vett2Text[mXXX+4]
        draw.text((1360, CellaY * 2 + MargS + StepTestoY), text, font=font, fill=(25, 0, 0, 255))

    if (mXXX+5) <= X:
        text = Vett3Text[mXXX+5]
        draw.text((1930, CellaY*2+MargS+StepTestoY), text, font=font, fill=(25,0,0,255) )
        #text = Vett3TextBar[mXXX+5]
        #draw.text((StepTestoX+190+(CellaX*2), CellaY*2+MargS+StepTestoY+10), text, font=fontBar, fill=(25,0,0,255) )
        text= Vett2Text[mXXX+5]
        draw.text((2140, CellaY * 2 + MargS + StepTestoY), text, font=font, fill=(25, 0, 0, 255))

    if (mXXX+6) <= X:
    #terzo rigo
        text = Vett3Text[mXXX+6]
        draw.text((360, CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )
        text=Vett2Text[mXXX+6]
        draw.text((570, CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )
    if (mXXX+7) <= X:
        text = Vett3Text[mXXX+7]
        draw.text((1150, CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )
        text=Vett2Text[mXXX+7]
        draw.text((1360, CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )

    if (mXXX+8) <= X:
        text = Vett3Text[mXXX+8]
        draw.text((1930, CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )
        #text = Vett3TextBar[mXXX+8]
        #draw.text((StepTestoX+(CellaX*2)+190, CellaY*3+MargS+10+(StepTestoY*2)), text, font=fontBar, fill=(25,0,0,255) )
        text=Vett2Text[mXXX+8]
        draw.text((2140, CellaY*3+MargS+(StepTestoY*2)), text, font=font, fill=(25,0,0,255) )

    #quarto riigo
    if (mXXX+9) <= X:
        text = Vett3Text[mXXX+9]
        draw.text((360, CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )
        text=Vett2Text[mXXX+9]
        draw.text((570, CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )
    if (mXXX+10) <= X:
        text = Vett3Text[mXXX+10]
        draw.text((1150, CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )
        #text = Vett3TextBar[mXXX+10]
        #draw.text((StepTestoX+(CellaX*1)+190, CellaY*4+MargS+10+(StepTestoY*3)), text, font=fontBar, fill=(25,0,0,255) )
        text=Vett2Text[mXXX+10]
        draw.text((1360, CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )

    if (mXXX+11) <= X:
        text = Vett3Text[mXXX+11]
        draw.text((1930, CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )
        text=Vett2Text[mXXX+11]
        draw.text((2140, CellaY*4+MargS+(StepTestoY*3)), text, font=font, fill=(25,0,0,255) )

    #image.show()
    image.save(myPathPage + 'bys' + str(mCod) + '.jpg')



