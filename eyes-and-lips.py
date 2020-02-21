import cv2
import os
import numpy as np
from skimage.filters import gaussian
from test import evaluate
import argparse


def parse_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('--img-path', default='images/img1.jpg')
    return parse.parse_args()

	
def mask(image, parsing, part=17, color=[230, 50, 20]):
	b, g, r = color      
	tar_color = np.zeros_like(image)
	tar_color[:, :, 0] = b
	tar_color[:, :, 1] = g
	tar_color[:, :, 2] = r

	image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	tar_hsv = cv2.cvtColor(tar_color, cv2.COLOR_BGR2HSV)

	image_hsv[:, :, 0:2] = tar_hsv[:, :, 0:2]
    #image_hsv[:, :, 0:1] = tar_hsv[:, :, 0:1]

	changed = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)
	changed[parsing != part] = image[parsing != part]
	
	return changed


if __name__ == '__main__':
    # 1  face
	# 4  left eye
	# 5  right eye
    # 12 upper lip
    # 13 lower lip

	args = parse_args()

	table = {
		'left_eye': 4,
		'right_eye': 5,
		'upper_lip': 12,
		'lower_lip': 13
	}

	image_path = args.img_path
	cp = 'cp/79999_iter.pth'
	
	try:
		image = cv2.imread(image_path)
		ori = image.copy()
		im2 = image.copy()
		im2 = cv2.rectangle(im2, (0, 0), (1080, 1080), (255, 255, 255), thickness = 1080)
	except AttributeError:
		print('Image not found. Please enter a valid path.')
		quit()
	
	parsing = evaluate(image_path, cp)
	parsing = cv2.resize(parsing, image.shape[0:2], interpolation=cv2.INTER_NEAREST)

	parts = [table['left_eye'], table['right_eye'], table['upper_lip'], table['lower_lip']]
	color = [139, 0, 139]
	
	for part in parts:
		image = mask(image, parsing, part, color)
		im2 = mask(im2, parsing, part, color)

	cv2.imshow('image', cv2.resize(ori, (512, 512)))
	cv2.imshow('mask', cv2.resize(im2, (512, 512)))
	cv2.imshow('color', cv2.resize(image, (512, 512)))

	cv2.waitKey(0)
	cv2.destroyAllWindows()
