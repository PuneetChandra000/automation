import cv2
import dropbox
import time
import random

startTime = time.time()

def taking_snapshot() :
    num = random.randint(1,10)

    # image1.png , image5.png ...

    cam = cv2.VideoCapture(0)
    result = True

    while(result) :
        dummy, frame = cam.read()

        imgName = "img" + str(num) + ".png"
        # num = 2 --> img+2+.png --> img2.png
        
        cv2.imwrite(imgName , frame)

        result = False

    return imgName

    cam.release() 
    cv2.destroyAllWindows()


def uploadingPart(imgName) :

    accessToken = "sl.BGwNLDT_mZ-6VbPmIuCEb2ObEfFaq7ScKdkeP7IASY9JAnJVHeRdQnxZwCRkGfEaefz63oaWnZNOqwjP0XE9B7Rh9_1Hm6f2iTC88fNNS2WqpkEClpprIBdABqNX6xdbewigiq6XQZhN"
      
    source = imgName
    destination = "/Images/"+ (imgName)

    dbx = dropbox.Dropbox(accessToken)

    with open(source , 'rb') as f:
        dbx.files_upload(f.read() , destination)
        print("Uploaded")


def main():
    while(True):
        if( time.time() - startTime >= 5 ):
            name = taking_snapshot()
            uploadingPart(name)


main()










