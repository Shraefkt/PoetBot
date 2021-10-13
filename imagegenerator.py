from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def create_image(text,image):
    font = ImageFont.truetype("imagedata/typewriter.ttf", 30)
    img = Image.open(image)
    width,height = img.size

    draw = ImageDraw.Draw(img)
    draw.text((width/10, height/5), text, (0, 0, 0), font=font)

    imgname = "imagedata/post.jpg"

    img.save(imgname)
    return imgname