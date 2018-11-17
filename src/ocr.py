import numpy as np
import cv2
import pytesseract
import sys

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
    # print(imgPath)
    # Open image
    img = cv2.imread("%s%s" % (IMG_BASE_PATH, imgPath))
    # if img.empty():
    #   raise InvalidInput("Invalid Input")
    # return img

    # Rescale
    width, height = img.shape[:2]
    if width < 300 and width < height:
        newWidth = 300
        newHeight = int((300 / float(width)) * height)
        img = cv2.resize(img, None, (newWidth,newHeight))
    elif height < 300:
        newHeight = 300
        newWidth = int((300 / float(height)) * width)
        img = cv2.resize(img, None, (newWidth,newHeight))

    # grayscale and binarization
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    if mode == "black":
        ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)  # 240
    elif mode == "white":
        ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY_INV)

    # Noise Reduction
    thresh = cv2.fastNlMeansDenoising(thresh, None, h=50)

    # Remove borders/excess stuff


    
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',thresh)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return thresh

if __name__ == '__main__':
    # load_system_dawg and load_freq_dawg to false
    img = preprocessImage(sys.argv[1], sys.argv[2])
    text = readImgText(img, "")
    print("Black text\n" + text)

    # img = preprocessImage("test/meme2.jpg", "white")
    # text = readImgText(img, "")
    # print("White text\n" + text)

    # img = preprocessImage("test/meme3.jpg", "white")
    # text = readImgText(img, "")
    # print("White text\n" + text)
    
    # img = preprocessImage("test/meme4.jpg", "white")
    # text = readImgText(img, "")
    # print("White text\n" + text)

    # cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    # cv2.imshow('image',img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
