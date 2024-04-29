from PIL import Image, ImageFilter
import os

img = Image.open('./Pokedex/pikachu.jpg')

print(img)
print(img.format)
print(img.size)
print(img.mode)

print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('pikachu_blur.png', 'png')

# filtered_img.show()

converted_img = img.convert('L')
crooked_converted_img = converted_img.rotate(90)
crooked_converted_img.save('pikachu_bw.png', 'png')

resized_img = filtered_img.resize((300, 300))
resized_img.save('pikachu_resized.png', 'png')

box = (100, 100, 400, 400)
cropped_img = filtered_img.crop(box)
cropped_img.save('pikachu_crop.png', 'png')

astro_img = Image.open('./astro.jpg')
astro_img.thumbnail((400, 400))
astro_sharpen = astro_img.filter(ImageFilter.SHARPEN)
astro_sharpen.save('astro_resized.png', 'png')
print(astro_img.size)

# print(os.path.abspath('pikachu_crop.png'))

# os.rename(os.path.abspath('pikachu_crop.png'), '/Users/yutanamba/Documents/ztm.py/visualStudioCode.proj/vsc001_images/pikachu_crop.png')

print(os.listdir('Pokedex/'))

print(os.path.basename(os.path.abspath('./astro.jpg')))

print(os.path.abspath('./Pokedex/bulbasaur.jpg'))
print(os.path.commonpath('bulbasaur.jpg'))

Image.open('./Pokedex/bulbasaur.jpg')
print(os.path.splitext('astro.jpg')[0])
