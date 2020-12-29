import qrcode
import datetime

input_data = input("Kindly enter the URL: ") #Creating an instance of qrcode
print('You have entered: ', input_data)

qr = qrcode.QRCode(
        version=1,   # version parameter is an integer from 1 to 40 that controls the size of the QR Code
        box_size=10, # Determines the number of pixels for each box of the QR code
        border=5     # Determines the thickness of the border of the boxes
    )


qr.add_data(input_data)
qr.make(fit=True)

# make and save image on current directory
img = qr.make_image(fill='black', back_color='white')
img.save('QR_'+str(datetime.datetime.now())+'.png')
print("Saved the QR code on at the codes directory")