import numpy as np
from PIL import Image

# user custom
step = 4
pic_name = "borner.jpg"
file_name = "borner.txt"

pad_flag = 0
pad_size_top = 140
pad_size_bottom = 60
pad_size_left = 10
pad_size_right = 10


image = Image.open("image\\" + pic_name)
img=np.array(image.convert("RGB").split()[0])

sizey, sizex = img.shape
print("image size:", sizey, sizex)
print("stride:", step)

print("data size:", int(sizey / step), int(sizex / step))

cell_state = [[0] * int(sizex / step) for i in range(int(sizey / step))]
print(len(cell_state))
for i in range(int(sizey / step)):
    for j in range(int(sizex / step)):
        if img[int(i * step + step / 2)][int(j * step + step / 2)] > 200:
            cell_state[i][j] = 1

data = np.array(cell_state)
np.savetxt("data\\" + file_name, data, fmt="%d", delimiter=' ')

# size = 0
# with open("data\\" + file_name) as f:
#     for line in f:
#         # print(line, end='')
#         size += 1
#         # print(len(line))

# print(size)


# padding
if pad_flag:
    # 构造用来扩边的数据
    # 纵向扩边 全是0
    row_adder = []
    for i in range(pad_size_left + pad_size_right + int(sizex / step)):
        if i == pad_size_left + pad_size_right + int(sizex / step) - 1:
            row_adder.append("0")
        else:
            row_adder.append("0 ")
    row_adder.append("\n")
    row_adder = "".join(row_adder)
    # print(row_adder)

    # 横向扩边，左边"0 "，右边" 0"
    row_adder_head_part = []
    row_adder_tail_part = []
    for i in range(pad_size_left):
        row_adder_head_part.append("0 ")
    for i in range(pad_size_right):
        row_adder_tail_part.append(" 0")

    row_adder_tail_part.append("\n")
    row_adder_head_part = "".join(row_adder_head_part)
    row_adder_tail_part = "".join(row_adder_tail_part)

    # 打开文件扩边
    with open("data\\" + file_name) as f:
        file_list = f.readlines()
        # print(file_list)
        # 先对数据左右扩边
        for i in range(int(sizey / step)):
            temp = list(file_list[i])
            temp.pop()
            temp = "".join(temp)
            file_list[i].strip("n")
            file_list[i] = str(row_adder_head_part) + str(temp) + str(row_adder_tail_part)

        # 再对数据上下扩边
        for i in range(pad_size_top):
            file_list.insert(0, row_adder)
        for i in range(pad_size_bottom):
            file_list.insert(-1, row_adder)

        print(file_list)

    # 写成新文件
    f=open("data\\" + file_name,"w")
    f.writelines(file_list)
    f.close()


    print("data size after padding:", int(sizey / step) + pad_size_top + pad_size_bottom, int(sizex / step) + pad_size_left + pad_size_right)
