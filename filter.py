from PIL import Image
import numpy as np


def crop_img(img_data, mosaic_width, mosaic_height):
    height_diff = len(img_data) % mosaic_height
    width_diff = len(img_data[1]) % mosaic_width
    return img_data[:len(img_data) - height_diff, :len(img_data[1]) - width_diff]


def get_pixel_color_sum(img_data, x, y):
    r = img_data[y][x][0]
    g = img_data[y][x][1]
    b = img_data[y][x][2]
    return int(r) + int(g) + int(b)


def set_pixel(img_data, x, y, sum, gradation):
    img_data[y][x][0] = int(sum // gradation) * gradation
    img_data[y][x][1] = int(sum // gradation) * gradation
    img_data[y][x][2] = int(sum // gradation) * gradation


img = Image.open("img2.jpg")

mosaic_width = int(input("Ширина мозайки: "))
mosaic_height = int(input("Высота мозайки: "))
gradation = 256 / int(input("Градация: "))
img_data = crop_img(np.array(img), mosaic_width, mosaic_height)
height = len(img_data)
width = len(img_data[1])
y = 0
while y < height:
    x = 0
    while x < width:
        sum = 0
        for y1 in range(y, y + mosaic_height):
            for x1 in range(x, x + mosaic_width):
                sum += get_pixel_color_sum(img_data, x1, y1)
        sum = int(sum // (mosaic_width * mosaic_height))
        for y1 in range(y, y + mosaic_height):
            for x1 in range(x, x + mosaic_width):
                set_pixel(img_data, x1, y1, sum / 3, gradation)
        x = x + mosaic_width
    y = y + mosaic_height
res = Image.fromarray(img_data)
res.save('res.jpg')
