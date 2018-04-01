# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
from sklearn.datasets import load_digits
from matplotlib import pyplot as plt
import numpy as np


class Digits:
    def __init__(self, nums, shuffle=False):
        self.nums = nums
        self.shuffle = shuffle

        digits = load_digits(return_X_y=True)
        self.x, self.y = digits

    def get_data(self):
        x, y = self.x, self.y
        x = x[:self.nums]
        y = y[:self.nums]
        return x, y

    def get_shuffle_data(self):
        x, y = self.x, self.y
        nums = np.random.permutation(self.nums)[:self.nums]
        x, y = x.take(nums, axis=0), y.take(nums)
        return x, y



class Draw(Digits):
    def __init__(self, nums, shuffle=False, figsize=(12, 12)):
        self.figsize = figsize
        super().__init__(nums, shuffle=shuffle)

    def __call__(self):
        return self.draw()

    def draw(self):
        if self.shuffle:
            x, y = self.get_shuffle_data()
        else:
            x, y = self.get_data()

        row, resid = divmod(self.nums, 8)
        if resid > 0:
            row += 1

        fig, axes = plt.subplots(row, 8, figsize=self.figsize)
        for i, ax in enumerate(axes.flat):
            if i >= np.alen(x):
                break
            ax.imshow(x[i].reshape(8,8), cmap='binary')
            ax.text(0, 0, y[i], fontdict={'color': 'red'})
            ax.set_xticks([])
            ax.set_yticks([])
        plt.pause(5)



if __name__ == "__main__":
    draw = Draw(17, shuffle=True)
    draw()
