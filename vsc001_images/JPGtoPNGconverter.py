import os
import sys
from PIL import Image


def create_file(file):
    if os.path.exists(file):
        return file
    else:
        return os.makedirs(file, exist_ok=True)


def convert_image(file, img):
    real_img = Image.open(f'./{file}/{img}')
    img_name = os.path.splitext(img)[0]
    return real_img.save(f'{img_name}.png', 'png')


def image_converter(og_file, new_file):
    create_file(new_file)
    img_list = os.listdir(og_file)
    for img in img_list:
        converted_img = convert_image(og_file, img)
        img_basename = f'{os.path.splitext(img)[0]}.png'
        new_file_basename = new_file
        os.rename(f'/Users/yutanamba/Documents/ztm.py/visualStudioCode.proj/vsc001_images/{img_basename}',
                  f'/Users/yutanamba/Documents/ztm.py/visualStudioCode.proj/vsc001_images/{new_file_basename}{img_basename}')


image_converter((sys.argv[1]), (sys.argv[2]))
