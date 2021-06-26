import numpy as np
from PIL import Image

step = 10

image = Image.open("Gosper-glider-gun.jpg")
img=np.array(image.convert("RGB").split()[0])

# print(img)

sizey, sizex = img.shape
print(sizey, sizex)

cell_state = [[0] * int(sizex / step) for i in range(int(sizey / step))]
print(len(cell_state))
for i in range(int(sizey / step)):
    for j in range(int(sizex / step)):
        if img[int(i * step + step / 2)][int(j * step + step / 2)] > 200:
            cell_state[i][j] = 1

data = np.array(cell_state)
np.savetxt('out.txt', data, fmt="%d", delimiter=' ')

size = 0
with open('out.txt') as f:
    for line in f:
        # print(line, end='')
        size += 1
        # print(len(line))

print(size)


