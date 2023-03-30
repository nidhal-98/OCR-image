import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Lenovo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
import re
import datetime





# Load Image and Preprocess
img = cv2.imread('C:\\Users\\Lenovo\\Downloads\\image1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Perform OCR
text = pytesseract.image_to_string(gray)



# Print Results
print(text)
