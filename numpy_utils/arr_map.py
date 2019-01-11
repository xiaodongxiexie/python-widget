# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import numpy as np

from typing import Callable


def arr_map(arr: np.array, function: Callable) -> np.array:
    shape = arr.shape
    arr = np.array(list(map(function, arr.ravel()))).reshape(shape)
    return arr


if __name__ == "__main__":
    arr = np.random.randn(3,4,3)

    arr2int = arr_map(arr, int)
    arr_plus_10 = arr_map(arr, lambda x: x+10)
    # 效果同
    arr_plus_10 = np.apply_along_axis(lambda x: x+10, 1, arr)
    print(arr2int)
    print(arr_plus_10)
