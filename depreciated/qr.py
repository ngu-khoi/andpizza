from PIL import Image
from pyzbar.pyzbar import decode

# Convert QR to text
def qr_code():
    global text_code1
    global text_code2
    data1 = decode(Image.open('qr1.png'))
    text_code1 = data1[0].data.decode('UTF-8')
    data2 = decode(Image.open('qr2.png'))
    text_code2 = data2[0].data.decode('UTF-8')
    print("Your discount codes are")
    print(text_code1 + " " + text_code2)