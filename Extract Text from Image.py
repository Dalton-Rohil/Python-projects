import cv2
import pytesseract

# read image using OpenCV
image = cv2.imread("image.jpg")

# pre-processing the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)

# pass image to Tesseract
text = pytesseract.image_to_string(gray, lang = 'eng',
        config='--psm 11')

print(text)
