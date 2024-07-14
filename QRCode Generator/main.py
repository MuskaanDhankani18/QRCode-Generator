import qrcode as qr

img = qr.make("https://www.youtube.com/codewithharry")
img.save("Code_youtube.png")