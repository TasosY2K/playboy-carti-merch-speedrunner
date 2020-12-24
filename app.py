from PIL import Image

Image1 = Image.open('hoodie.png')

Image1copy = Image1.copy()
Image2 = Image.open('carti.jpg')
Image2copy = Image2.copy()

Image1copy.paste(Image2copy, (295, 225))
Image1copy.save('merch.png')
print("Done")
