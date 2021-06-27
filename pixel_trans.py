from PIL import Image
import numpy as np

filename = 'self.jpg'
pixel_size = 2

black = 0
white = 255
dithers = {
	0: [[black] * pixel_size] * pixel_size,
	63: [[black, black] * int(pixel_size / 2), [black, white] * int(pixel_size / 2)] * int(pixel_size / 2),
	127: [[black, white] * int(pixel_size / 2), [white, black] * int(pixel_size / 2)] * int(pixel_size / 2),
	191: [[black, white] * int(pixel_size / 2), [white, white] * int(pixel_size / 2)] * int(pixel_size / 2),
	255: [[white] * pixel_size] * pixel_size
}

img = Image.open(filename)

w = img.size[0]
h = img.size[1]

w = int(w / pixel_size) * pixel_size
h = int(h / pixel_size) * pixel_size

r, g, b = img.split()

arr_in = np.array(img.convert('L'))
arr_out = np.zeros((h,w))

for i in range(int(h / pixel_size)):
    for j in range(int(w / pixel_size)):
        a = i * pixel_size + int(pixel_size / 2)
        b = j * pixel_size + int(pixel_size / 2)
        if (0 <= arr_in[a][b] < 63):
            arr_out[i * pixel_size:i * pixel_size + pixel_size, j * pixel_size:j * pixel_size + pixel_size] = dithers[0]
        elif (63 <= arr_in[a][b] < 127):
            arr_out[i * pixel_size:i * pixel_size + pixel_size, j * pixel_size:j * pixel_size + pixel_size] = dithers[63]
        elif (127 <= arr_in[a][b] < 191):
            arr_out[i * pixel_size:i * pixel_size + pixel_size, j * pixel_size:j * pixel_size + pixel_size] = dithers[127]
        elif (191 <= arr_in[a][b] < 255):
            arr_out[i * pixel_size:i * pixel_size + pixel_size, j * pixel_size:j * pixel_size + pixel_size] = dithers[191]
        else:
            arr_out[i * pixel_size:i * pixel_size + pixel_size, j * pixel_size:j * pixel_size + pixel_size] = dithers[255]


im = Image.fromarray(arr_out).convert('L')
im.show()
im.save("pixel" + filename)


