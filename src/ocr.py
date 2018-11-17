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



if __name__ == '__main__':

	for file in listdir(img_path):

		img = cv2.imread("%s%s" % (img_path, file), 0)

		text = pytesseract.image_to_string(img)

		print("name: " , file)
		print(text, "\n")
		print("-----------------------------------------")