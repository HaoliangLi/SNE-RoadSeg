import os
import cv2
import glob
import numpy as np

path = 'datasets/rtks/training/labels'
path = 'datasets/rtks/validation/labels'

names = sorted(glob.glob(os.path.join(path, '*.png')))
max_label = -1
for name in names:
    img = cv2.imread(name)
    max_label_cur = np.max(img)
    max_label = max(max_label, max_label_cur)
print(max_label)
