#in first step you must install passporteye , pytesseract :
# pip install passporteye
# pip install pytesseract

from passporteye import read_mrz
import pytesseract

#Correct pytesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


# Process image
mrz = read_mrz("pass.jpg")

# Obtain image
mrz_data = mrz.to_dict()

print('Nationality :'+ mrz_data['nationality'])
print('Given Name :'+ mrz_data['names'])
print('Surname :'+ mrz_data['surname'])
print('Passport type :'+ mrz_data['type'])
print('Date of birth :'+ mrz_data['date_of_birth'])
print('ID Number :'+ mrz_data['personal_number'])
print('Gender :'+mrz_data['sex'])
print('Expiration date :'+ mrz_data['expiration_date'])
print(mrz_data,file=open('passportdata.csv',"a"))
