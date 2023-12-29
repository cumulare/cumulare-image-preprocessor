# create a function that uses opencv to remove the background of an image and noise
# and returns the image with the background removed
#
# The function should take in an image and return an image
#
# The function should be called remove_background

import cv2
import numpy as np

def remove_background(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    #image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    _, binary = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    inverted = cv2.bitwise_not(binary)
    return inverted

# create a function that uses opencv to remove the background of an image and noise

def remove_noise(image):
    kernel = np.ones((3, 3), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.dilate(image, kernel, iterations=1)
    return image

# create a functiont that reads in an image

def read_image(image_path):
    image = cv2.imread(image_path)
    return image

# create a function to resize an image 256x256

def resize_image(image):
    image = cv2.resize(image, (256, 256))
    return image

# create a function that resizes an image 4 scales starting from 256x256 4 times
# the function should return a list of images

def resize_image_4_scales(image):
    images = []
    #increment by 4 
    j = 0
    for i in range(4):
        images.append(image)
        image = cv2.resize(image, (256 + j, 256 + j))
        #random sample to increase resize
        j+=120
    return images
# create a function that corrects the skew of an image

def correct_skew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    print(angle)
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    print(angle)
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    print(center)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    print(M)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

if __name__ == "__main__":
    image = read_image("/Users/spacious/Documents/cumulare/spacious/ghec/cumulare-image-preprocessor/images/htr/be_thou_my_vision_1.png")
    image = remove_background(image)
    #image = correct_skew(image)
    #image = resize_image(image)
    #image = remove_noise(image)
    # call resize_image_4_scales and save the images to a folder
    images = resize_image_4_scales(image)
    for i in range(len(images)):
        cv2.imwrite("./images/htr/processedB/processed_image" + str(i) + ".png", images[i])

    cv2.imwrite("./processed_image.png", image)