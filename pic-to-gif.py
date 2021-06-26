import matplotlib.pyplot as plt
# import imageio,os

# images = []
# filenames=sorted((fn for fn in os.listdir('.') if fn.endswith('.png')))
# for filename in filenames:
#     images.append(imageio.imread(filename))
# imageio.mimsave('gif.gif', images,duration=1)

from PIL import Image
import os
folder = "20210626-1133"
path = "screenshots\\" + str(folder)

pic_cnt = len(os.listdir(path))
# for filename in os.listdir(path):              #listdir的参数是文件夹的路径
#      print (filename)
im = Image.open(path + "\\" + "screenshot_1.jpg")
images=[]
for i in range(2, pic_cnt + 1):
    images.append(Image.open(path + "\\" + "screenshot_" + str(i) + ".jpg"))
im.save('gif.gif', save_all=True, append_images = images, loop = 1, duration = 0.2, comment=b"aaabb")