import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw, ImageFont

# read image and convert to RGB
image = Image.open("readonly/msi_recruitment.gif")
image = image.convert('RGB')

# intializing variables
channel = 0
x = 0
y = 0
img_lst = []
cs_lst = []

# creating a blank back page
cs_main = PIL.Image.new(image.mode, (image.width * 3, (image.height + 80) * 3))

# method to return intensities
count = 0


def intensity(ct):
    if ct % 3 == 0:
        return ( 0.1)
    elif ct % 3 == 1:
        return ( 0.5)
    else:
        return ( 0.9)


# creating a list of images
for i in range(1, 10):
    img_lst.append(image)

# adding text to image and changing the intenity and channel of image and appending those images in a new list cs_lst
for img in img_lst:
    if count < 3:
        channel = 0
    elif 3 <= count < 6:
        channel = 1
    else:
        channel = 2
    ct = intensity(count)
    cs = PIL.Image.new(image.mode, (image.width, image.height + 80))
    cs.paste(img, (0, 0))
    txt = Image.new('RGB', (image.width, 80), (0, 0, 0))
    fnt = ImageFont.truetype('readonly/fanwood-webfont.ttf', 75)
    d = ImageDraw.Draw(txt)
    d.text((10, 10), "channel {} intensity {}".format(channel, ct), font=fnt, fill=(255, 255, 255, 128))
    cs.paste(txt, (0, 450))

    for x in range(cs.width):
        for y in range(cs.height):
            if count < 3:
                r, g, b = cs.getpixel((x, y))
                cs.putpixel((x, y), (int(r*ct), g, b))
            elif 3 <= count < 6:
                r, g, b = cs.getpixel((x, y))
                cs.putpixel((x, y), (r, int(g*ct), b))
            else:
                r, g, b = cs.getpixel((x, y))
                cs.putpixel((x, y), (r, g, int(b*ct)))
    count += 1

    cs_lst.append(cs)

x = 0
y = 0

# adding the images in the contact sheet
for cs in cs_lst:

    cs_main.paste(cs, (x, y))
    if x + image.width == cs_main.width:
        x = 0
        y = y + image.height + 80
        channel += 1
    else:
        x = x + image.width

cs_main.show()