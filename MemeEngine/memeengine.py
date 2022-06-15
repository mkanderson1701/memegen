"""Builds meme."""

from imagetexter import ImageTexter
from imagesizer import ImageSizer


class MemeEngine():

    def make_meme(cls, img_path, text, author, width=500):
        ImageSizer.resize_img(img_path, width)
        