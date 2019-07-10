import cv2
from filters import *
from datetime import datetime
import os
import argparse

print('Inicio del Proceso')
start = datetime.now()

parser = argparse.ArgumentParser(description='Recive Paths')
parser.add_argument('directory', type=str, help='input path')
parser.add_argument('output', type=str, help='output path')

args = parser.parse_args()
folder = args.directory + '/'
output_folder = args.output + '/'

filenames = os.listdir(folder)
print(filenames[0])
print(filenames[:5])
print(len(filenames))

from random import shuffle
from math import floor

shuffle(filenames)
print(filenames[:5])
# reduction = floor(len(filenames)*0.4)
# filenames = filenames[:reduction]
print(len(filenames))
print(filenames[:5])

extension='.png'

counter = 0
for image_file in filenames:
    #image_file = '/home/jf/Documents/estudio/xrays/augmentation/consolidation.png'
    counter += 1
    print('Image: ' + image_file + ' ' + str(counter) + ' of ' + str(len(filenames)))
    name = image_file[:len(image_file)-4]
    image = cv2.imread(folder + image_file)
    print("Read Complete")

    print(output_folder)
    booster = Booster(folder, extension, name, output_folder)


    # booster.flip_image(image, 0)#Horizontal
    # booster.flip_image(image, 1)#Vertical
    # booster.flip_image(image, -1)#Both
    ## booster.invert_image(image, 255)
    # booster.invert_image(image, 200)
    # booster.invert_image(image, 150)
    # booster.invert_image(image, 100)
    # booster.invert_image(image, 50)
    ## booster.add_light(image, 1.5)
    # booster.add_light(image, 2.0)
    # booster.add_light(image, 2.5)
    # booster.add_light(image, 3.0)
    # booster.add_light(image, 4.0)
    # booster.add_light(image, 5.0)
    # booster.add_light(image, 0.7)
    print("Revisión")
    # booster.clahe_image_gray(image)
    booster.clahe_image_color(image)
    # booster.add_light(image, 0.3)
    # booster.add_light(image, 0.1)
    ## booster.add_light_color(image, 255 ,1.5)
    # booster.add_light_color(image, 200 ,2.0)
    # booster.add_light_color(image, 150 ,2.5)
    # booster.add_light_color(image, 100 ,3.0)
    # booster.add_light_color(image, 50 ,4.0)
    # booster.add_light_color(image, 255 ,5.0)
    # booster.add_light_color(image, 150 ,0.7)
    ## booster.add_light_color(image, 100 ,0.3)
    # booster.add_light_color(image, 200 ,0.1)
    # booster.saturation_image(image, 50)
    # booster.saturation_image(image, 100)
    # booster.saturation_image(image, 150)
    # booster.saturation_image(image, 200)
    # booster.hue_image(image, 50)
    # booster.hue_image(image, 100)
    # booster.hue_image(image, 150)
    # booster.hue_image(image, 200)
    # booster.multiply_image(image, 0.5, 1, 1)
    # booster.multiply_image(image, 1, 0.5, 1)
    # booster.multiply_image(image, 1, 1, 0.5)
    # booster.multiply_image(image, 0.5, 0.5, 0.5)
    # booster.multiply_image(image, 0.25, 1, 1)
    # booster.multiply_image(image, 1, 0.25, 1)
    # booster.multiply_image(image, 1, 1, 0.25)
    # booster.multiply_image(image, 0.25, 0.25, 0.25)
    # booster.multiply_image(image, 1.25, 1, 1)
    # booster.multiply_image(image, 1, 1.25, 1)
    # booster.multiply_image(image, 1, 1, 1.25)
    # booster.multiply_image(image, 1.25, 1.25, 1.25)
    # booster.multiply_image(image, 1.5, 1, 1)
    # booster.multiply_image(image, 1, 1.5, 1)
    # booster.multiply_image(image, 1, 1, 1.5)
    # booster.multiply_image(image, 1.5, 1.5, 1.5)
    # booster.gaussian_blur(image, 0.25)
    # booster.gaussian_blur(image, 0.50)
    # booster.gaussian_blur(image, 1)
    # booster.gaussian_blur(image, 2)
    # booster.gaussian_blur(image, 4)
    # booster.averageing_blur(image, 5)
    # booster.averageing_blur(image, 4)
    # booster.averageing_blur(image, 6)
    ## booster.median_blur(image, 3)
    # booster.median_blur(image, 5)
    # booster.median_blur(image, 7)
    # booster.bilateral_blur(image, 9, 75, 75)
    # booster.bilateral_blur(image, 12, 100, 100)
    # booster.bilateral_blur(image, 25, 100, 100)
    # booster.bilateral_blur(image, 40, 75, 75)
    # booster.erosion_image(image, 1)
    # booster.erosion_image(image, 3)
    # booster.erosion_image(image, 6)
    # booster.dilatation_image(image, 1)
    # booster.dilatation_image(image, 3)
    # booster.dilatation_image(image, 5)
    ## booster.opening_image(image, 1)
    # booster.opening_image(image, 3)
    # booster.opening_image(image, 5)
    ## booster.morphological_gradient_image(image, 5)
    # booster.morphological_gradient_image(image, 10)
    # booster.morphological_gradient_image(image, 15)
    # booster.top_hat_image(image, 200)
    # booster.top_hat_image(image, 300)
    # booster.top_hat_image(image, 500)
    # booster.black_hat_image(image, 200)
    # booster.black_hat_image(image, 300)
    ## booster.black_hat_image(image, 500)

end = datetime.now()

print('Final del proceso')
print('Duracion: {}'.format(end-start))
