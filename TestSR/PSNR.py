'''import cv2
import numpy as np
import math
def psnr(img1, img2):
   mse = np.mean( (img1/255. - img2/255.) ** 2 )
   if mse < 1.0e-10:
      return 100
   PIXEL_MAX = 1
   return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
if __name__ == '__main__':
   gt = cv2.imread('00003.png')
   img= cv2.imread('00003_out.png')
   print(psnr(gt,img))'''
from skimage.metrics import peak_signal_noise_ratio as psnr
from PIL import Image
import numpy as np
import cv2
img1 = np.array(Image.open('00003.png'))
img2 = np.array(Image.open('00003_out_mix_interpolation.png'))
img2=cv2.resize(img2, (512, 256))

if __name__ == "__main__":
    print(psnr(img1, img2))