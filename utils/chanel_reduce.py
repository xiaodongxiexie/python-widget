from PIL import Image


class ChannelTransform(object):
    def __init__(self, img_path):
        self.img = self.read_img(img_path)

    def read_img(self, img_path):
        img = Image.open(img_path)
        return img

    def change_image_channels(self):
        img = self.img
        if img.mode == "RGBA":
            r, g, b, a = img.split()
            img = Image.merge("RGB", (r, g, b))
            return img
