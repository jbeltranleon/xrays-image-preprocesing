import cv2
import numpy as np

class Booster:
    def __init__(self, folder, extension, name, output_folder):
        self.folder = folder
        self.extension = extension
        self.name = name
        self.output_folder = output_folder

    #flip
    def flip_image(self, image, dir):
        image = cv2.flip(image, dir)
        cv2.imwrite(
            self.folder + '/{}-flip-'.format(name) + str(dir) + self.extension,
            image)

    def invert_image(self, image, channel):
        image = (channel - image)
        cv2.imwrite(
            self.folder + '/{}-invert-'.format(self.name) + str(channel) + self.extension,
            image)

    def add_light(self, image, gamma=1.0):
        inv_gamma = 1.0 / gamma
        table = np.array([((i/255.0) ** inv_gamma) * 255
                        for i in np.arange(0,256)]).astype('uint8')

        image = cv2.LUT(image, table)

        if gamma >=1:
            cv2.imwrite(
                self.folder + '/{}-ligth-'.format(self.name) + str(gamma) + self.extension,
                image)
        else:
            cv2.imwrite(
                self.folder + '/{}-dark-'.format(self.name) + str(gamma) + self.extension,
                image)

    def add_light_color(self, image, color, gamma=1.0):
        inv_gamma = 1.0 / gamma
        image = (color - image)
        table = np.array([((i/255.0) ** inv_gamma) * 255
                        for i in np.arange(0,256)]).astype('uint8')

        image = cv2.LUT(image, table)

        if gamma >=1:
            cv2.imwrite(self.folder+'/{}-ligth_color-'.format(self.name) + str(gamma) + self.extension, image)
        else:
            cv2.imwrite(self.folder+'/{}-dark_color-'.format(self.name) + str(gamma) + self.extension, image)

    def saturation_image(self, image, saturation):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        v = image[:, :, 2]
        v = np.where(v <= 255 - saturation, v + saturation, 255)
        image[:, :, 2] = v

        image == cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        cv2.imwrite(self.folder + '/{}-saturation-'.format(self.name) + str(saturation) + self.extension,image)

    def hue_image(self, image, saturation):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        v = image[:, :, 2]
        v = np.where(v <= 255 + saturation, v - saturation, 255)
        image[:, :, 2] = v

        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        cv2.imwrite(self.folder + '/{}-hue-'.format(self.name) + str(saturation) + self.extension,image)

    def multiply_image(self, image, R,G,B):
        image = image*[R,G,B]
        cv2.imwrite(
            self.folder+'/{}-multiply-'.format(self.name)+str(R)+'*'+str(G)+'*'+str(B)+'*'+ self.extension,
            image)

    def gaussian_blur(self, image, blur):
        image = cv2.GaussianBlur(image, (5,5), blur)
        cv2.imwrite(self.folder+'/{}gaussian_blur-'.format(self.name)+str(blur)+self.extension, image)

    def averageing_blur(self, image, shift):
        image = cv2.blur(image, (shift, shift))
        cv2.imwrite(self.folder+'/{}averageing_blur-'.format(self.name)+str(shift)+self.extension, image)

    def median_blur(self, image, shift):
        image = cv2.medianBlur(image, shift)
        cv2.imwrite(self.folder+'/{}-median_blur-'.format(self.name)+str(shift)+self.extension, image)

    def bilateral_blur(self, image, d, color, space):
        image = cv2.bilateralFilter(image, d, color, space)
        cv2.imwrite(
            self.folder+'/{}-bi_blur-'.format(self.name)+str(d)+'*'+str(color)+'*'+str(space)+self.extension,
            image)

    def erosion_image(self, image, shift):
        kernel = np.ones((shift,shift),np.uint8)
        image = cv2.erode(image, kernel, iterations=1)
        cv2.imwrite(self.folder+'/{}-erosion-'.format(self.name)+str(shift)+self.extension, image)

    def dilatation_image(self, image, shift):
        kernel = np.ones((shift,shift),np.uint8)
        image = cv2.dilate(image, kernel, iterations=1)
        cv2.imwrite(self.folder+'/{}-dilatation-'.format(self.name)+str(shift)+self.extension, image)

    def opening_image(self, image, shift):
        kernel = np.ones((shift,shift),np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
        cv2.imwrite(self.folder+'/{}-opening-'.format(self.name)+str(shift)+self.extension, image)

    def closing_image(self, image, shift):
        kernel = np.ones((shift,shift),np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
        cv2.imwrite(self.folder+'/{}-closing-'.format(self.name)+str(shift)+self.extension, image)

    def morphological_gradient_image(self, image, shift):
        kernel = np.ones((shift,shift),np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, kernel)
        cv2.imwrite(
            self.folder+'/{}-morphological_gradient-'.format(self.name)+str(shift)+self.extension,
            image)

    def top_hat_image(self, image, shift):
        kernel = np.ones((shift,shift),np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
        cv2.imwrite(self.folder+'/{}-top_hat-'.format(self.name)+str(shift)+self.extension, image)

    def black_hat_image(self, image, shift):
        kernel = np.ones((shift,shift),np.uint8)
        image = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
        cv2.imwrite(self.folder+'/{}-black_hat-'.format(self.name)+str(shift)+self.extension, image)

    #https://docs.opencv.org/3.1.0/d5/daf/tutorial_py_histogram_equalization.html
    def clahe_image_gray(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        image = clahe.apply(gray_image)
        cv2.imwrite(self.folder+'/{}-clahe_gray'.format(self.name)+self.extension, image)

    # https://stackoverflow.com/questions/25008458/how-to-apply-clahe-on-rgb-color-images
    #Conversion of RGB to LAB(L for lightness and a and b for the color opponents green–red and blue–yellow) will do the work. Apply CLAHE to the converted image in LAB format to only Lightness component and convert back the image to RGB. Here is the snippet.
    def clahe_image_color(self, image):
        lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
        lab_planes = cv2.split(lab)
        clahe = cv2.createCLAHE(clipLimit=2.0,tileGridSize=(8,8))
        lab_planes[0] = clahe.apply(lab_planes[0])
        lab = cv2.merge(lab_planes)
        image = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)
        #cv2.imwrite(self.folder+'/{}-clahe_color'.format(self.name)+self.extension, image)
        #overwrite
        cv2.imwrite(self.output_folder+'/'+format(self.name)+self.extension, image)
        #cv2.imwrite(self.folder+'/{}-clahe_color'.format(self.name)+self.extension, image)