import numpy as np
import cv2
import pytesseract
from pathlib import Path

IMG_BASE_PATH = "../res/images/"

'''
* readImgText takes a read cv2 image as an input, and a path to
* the tesseract engine. If "" is supplied, then it uses the default path.
* The function returns the text it could read from the image. Assumes the
* image is preprocessed and ready to read.
'''
def readImgText(img, tesseractEnginePath):
    # Modify tesseract engine path if needed
    if tesseractEnginePath != "":
        pytesseract.pytesseract.tesseract_cmd = tesseractEnginePath

    # Run tesseract engine
    text = pytesseract.image_to_string(img)
    return text

'''
* preprocessImage takes a string which is the filepath to an image.
* This filepath is the extension from the IMG_BASE_PATH from the src folder.
* The image processed and returns an opened opencv image.
'''
def preprocessImage(imgPath, mode):
    img = cv2.imread("%s%s" % (IMG_BASE_PATH, imgPath))

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # if img.empty():
    #   raise InvalidInput("Invalid Input")
    # return img

    # Thresh bin for black text
    if mode == "black":
        ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)
    elif mode == "white":
        ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY_INV)
    thresh = cv2.dilate(thresh, None, iterations=1)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return thresh

if __name__ == '__main__':
    # img = preprocessImage("test/testocr.png")
    # img = preprocessImage("test/pika.jpg", "black")

    for file in Path(IMG_BASE_PATH + "test"):
        # filename = os.fsdecode(file)
        img = preprocessImage("%s" % str(file), "white")
        text = readImgText(img, "")
        print("Black text\n" + text)

        img = preprocessImage("%s" % str(file), "black")
        text = readImgText(img, "")
        print("White text\n" + text)

    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
