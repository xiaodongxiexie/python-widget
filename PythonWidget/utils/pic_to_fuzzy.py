# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   2017-12-30 23:53:04
# @Last Modified by:   liangxiaodong
# @Last Modified time: 2018-02-05 09:50:17

import os

from scipy.ndimage import filters
from pylab import imshow, axis, array, pause, close, imsave
from numpy import array, uint8
from PIL import Image

def fuzzy_pic(path, gray=False, fuzzy=5, save=False, save_name=None, test=False, **kwargs):
    """
    将给定地址的图片做高斯模糊。
    :param path: 图片路径
    :param fuzzy: 模糊度，越大越模糊
    :param save: bool， 是否保存，默认为False
    :param save_name: 保存文件名
    :param test: 测试用，显示5s并退出
    :rtype: 无返回值
    """
    img = Image.open(path)

    if gray:
        img_arr = img.convert("L")
    else:
        img_arr = array(img)
        alen = img_arr.shape[2]

        assert alen == 3, "仅支持RGB图"

        for i in range(3):
            img_arr[:, :, i] = filters.gaussian_filter(img_arr[:, :, i], fuzzy)
        img_arr = img_arr.astype(uint8)

    if save:
        if not save_name:
            full_name = os.path.split(path)[-1].split(".")
            save_name = full_name[0] + "_." + full_name[1]

        imsave(save_name, img_arr)

    if test:
        imshow(img_arr)
        axis("off")
        pause(5)
        close()


if __name__ == "__main__":
    path  = r"D:\lxd\git_\data\empire.jpg"
    gray  = False
    fuzzy = 1
    save  = False
    test  = True

    kwargs = globals()
    fuzzy_pic(**kwargs)