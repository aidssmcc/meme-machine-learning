import numpy as np
import cv2
import pytesseract

img_path = "../res/images/"

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
	img = cv2.imread("%stest/testocr.png" % img_path , 0)

	text = pytesseract.image_to_string(img)

	print(text)