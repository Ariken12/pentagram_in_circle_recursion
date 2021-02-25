GOLDEN = (1 + 5 ** 0.5) / 2
RTOR = 5 ** 0.5 - 1
WIDTH = 10000
HEIGHT = 10000

from PIL import Image, ImageDraw

image = Image.new('RGB', (HEIGHT, WIDTH), 'white')

imagedraw = ImageDraw.Draw(image)

imagedraw.ellipse((0, 0, HEIGHT, WIDTH), 'black')
imagedraw.ellipse((
    HEIGHT / 2 - HEIGHT / 2 / (GOLDEN * RTOR), 
    WIDTH / 2  - WIDTH / 2 / (GOLDEN * RTOR), 
    HEIGHT / 2 + HEIGHT / 2 / (GOLDEN * RTOR), 
    WIDTH / 2 + WIDTH / 2 / (GOLDEN * RTOR)
                  ), 
                  'white')

image.save('circle.png')