
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project -> File   ：Huawei -> test
@IDE    ：PyCharm
@Author ：Mr. liyuan
@Date   ：2021/12/27 13:15
@User   ：break
'''
import os
from PIL import Image

try:
    ImgFiler = input("输入文件路径+文件名（C:\\1.jpg）:")
    ImgPath = str(ImgFiler).split(',')[0].replace('\'', '').replace('(', '')
    # 取图片当前路径
    save_Path = ImgPath.rpartition('\\')[0] + '\\'
    # 取图片名称
    img_name = ImgPath.split('\\')[-1]
    ico_name = img_name.split('.')[0] + '.ico'

    size_num = int(input("请输入16，32，64，128，256尺寸："))
    if size_num == 16:
        size_ico = (16, 16)
    elif size_num == 32:
        size_ico = (32, 32)
    elif size_num == 64:
        size_ico = (64, 64)
    elif size_num == 128:
        size_ico = (128, 128)
    elif size_num == 256:
        size_ico = (256, 256)
    else:
        print("请输入正确的size")
    ico = Image.open(ImgPath).resize(size_ico)
    path = os.path.join(save_Path, ico_name)
    ico.save(path)
    print('生成完毕，{} --> {}'.format(img_name, ico_name))
except (AttributeError, IOError):
    print("图片路径或尺寸选择错误")

input("按任意键退出")