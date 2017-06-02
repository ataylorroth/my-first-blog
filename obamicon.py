from PIL import Image

im = Image.open ( "shelby.jpg")
new_image = Image.new(im.mode, im.size)


pixels = list(im.getdata())

darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)

new_pic = []
for pixel in pixels:
    intensity = pixel[0] + pixel[1] + pixel[2]
    if intensity <= 182:
        pixel = darkBlue
    if 182 < intensity <= 364:
        pixel = red
    if 364 < intensity <= 546:
        pixel = lightBlue
    if intensity > 546:
        pixel = yellow
    new_pic.append(pixel)

new_image.putdata(new_pic)
new_image.save( "output.jpg", "jpeg")
