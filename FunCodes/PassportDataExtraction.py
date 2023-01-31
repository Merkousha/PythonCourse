import cv2
import pytesseract

# Load image using OpenCV
img = cv2.imread("pass4.jpg")

#Correct pytesseract Installation Path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
# Apply OCR using pytesseract
text = pytesseract.image_to_string(img)

# Extract relevant information
# Example: extract name, birth date, passport number
data = {}
lines = text.split("\n")
for line in lines:
    if "Name" in line:
        data["Name"] = line.replace("Name:", "").strip()
    elif "Birth" in line:
        data["Birth Date"] = line.replace("Birth Date:", "").strip()
    elif "Passport" in line:
        data["Passport Number"] = line.replace("Passport No:", "").strip()

# Print extracted data
print(lines)
