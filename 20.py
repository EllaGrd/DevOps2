from PIL import Image

width = 400
height = 300

img  = Image.new( mode = "RGB", size = (width, height) )
img.show()


from Pillow import Image

img = Image.new('RGB', (60, 30), color = (73, 109, 137))
img.save('c:/Users/BWX367/PycharmProjects/DevOps2/pil_color.png')


