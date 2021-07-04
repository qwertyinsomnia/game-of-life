import matplotlib.pyplot as plt

from PIL import Image
import os
folder = "20210704-1151"
path = "screenshots\\" + str(folder)

pic_cnt = len(os.listdir(path))
# for filename in os.listdir(path):              #listdir的参数是文件夹的路径
#      print (filename)
im = Image.open(path + "\\" + "screenshot_1.jpg")
images=[]
for i in range(2, pic_cnt + 1):
    images.append(Image.open(path + "\\" + "screenshot_" + str(i) + ".jpg"))
im.save("gif\\" + folder + ".gif", save_all=True, append_images = images, loop = 1, duration = 0.2, comment=b"aaabb")