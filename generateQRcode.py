import qrcode

#.strip() is used to remove any extra spaces before or after the URL
url=input("Enter the URL: ").strip()

#Specify the path where you want to save the QR code image
file_path="C:\\Users\\ACER\\Desktop\\QRcode.png"

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print("QR code generated !")