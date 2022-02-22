import qrcode

data = 'Allahu Akbar'

img = qrcode.QRCode(version=2, box_size=15, border=1)


img.add_data(data)
img.make(fit=True)


code = img.make_image(fill_color='blue', back_color='lime')


code.save('text.png')






