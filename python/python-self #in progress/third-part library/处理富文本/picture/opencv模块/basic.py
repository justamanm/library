# pip install opencv-python
import cv2
import numpy as np

# img = cv2.imread('../num_pic/7.png')
# print(img.shape)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(gray.shape)
# ret = cv2.resize(gray, (56, 56))

ret = np.load("./some_array.npy")
print(ret)
cv2.imshow("img", ret)
cv2.waitKey(0)
# print("-" * 50)
# ret_combine = ret.reshape(28*28)
# print(ret_combine.shape)
# print(ret)

