from skimage.metrics import structural_similarity as ssim
from PIL import Image
import numpy as np
import cv2

img1 = np.array(Image.open('00003.png'))
img2 = np.array(Image.open('00003_out_mix_interpolation.png'))
img2 = cv2.resize(img2, (512, 256))


if __name__ == "__main__":
	# If the input is a multichannel (color) image, set multichannel=True.
    print(ssim(img1, img2, multichannel=True))
