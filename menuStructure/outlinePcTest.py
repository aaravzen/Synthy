from PIL import Image, ImageDraw, ImageFont

width = 128 # This is the number of pixels in our onboard screen
height = 128 # This is the number of pixels in our onboard screen

image = Image.new("RGB", (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
image.show()
