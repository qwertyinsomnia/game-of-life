import sys
from PIL import Image, ImageDraw, ImageOps

img = Image.open("image\\borner2.jpg")
resize_ratio = 4

stride = 4
offset_x = 0
offset_y = 0


x, y = img.size
img = ImageOps.invert(img)
img = img.resize((x * resize_ratio, y * resize_ratio),Image.NEAREST)
draw = ImageDraw.Draw(img) #实例化一个对象
print(img.size)
x, y = img.size


# 划分图像，直到找到合适的网格大小，然后计算偏移量切割图像
for i in range(int(x / stride)):
    draw.line((i * stride + offset_x, 0, i * stride + offset_x, y), fill=128, width=1)
for i in range(int(y / stride)):
    draw.line((0, i * stride + offset_y, x, i * stride + offset_y), fill=128, width=1)

img.show()

# 切割图象并保存
cropped = img.crop((offset_x, offset_y, int((x - offset_x) / stride) * stride + offset_x, int((y - offset_y) / stride) * stride + offset_y))  # (left, upper, right, lower)
print("pic size:", int((x - offset_x) / stride) * stride, int((y - offset_y) / stride) * stride)
print("grid size :", stride)
cropped.save("image\\borner.jpg")