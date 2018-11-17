import numpy as np
import cv2
import pytesseract
from os import listdir

img_path = "../res/images/"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

'''
* readImgText takes a read cv2 image as an input, and a path to
* the tesseract engine. If "" is supplied, then it uses the default path.
* The function returns the text it could read from the image. Assumes the
* image is preprocessed and ready to read.
'''
def readImgText(img, tesseractEnginePath):
	if tesseractEnginePath != "":
		pytesseract.pytesseract.tesseract_cmd = tesseractEnginePath

	text = pytesseract.image_to_string(img)
	return text

def preprocessImage(img_name):

	# read the image
	img = cv2.imread("%s%s" % (img_path, img_name))

	# grayscale and binarization
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# assumes white mode
	ret,thresh = cv2.threshold(gray,240,255,cv2.THRESH_BINARY_INV)

	img = thresh
	return img


if __name__ == '__main__':

        for file in listdir(img_path):
        	img = preprocessImage(file)
        	text = pytesseract.image_to_string(img)
        	print("name: " , file)
        	print(text, "\n")
        	print("-----------------------------------------")
