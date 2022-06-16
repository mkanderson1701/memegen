"""Builds meme."""

from imagetexter import ImageTexter
from imagesizer import ImageSizer
import os
import random
import datetime


class MemeEngine():

    def __init__(self, output_dir):
        self._output_dir = output_dir

    def make_meme(self, imgs_dir, text, author, width=500):
        img_file = self.choose_image(imgs_dir)
        output_file = self.set_outfile(self._output_dir)

        im = ImageSizer.resize_img(img_file, width)
        im = ImageTexter.text_img(im, text, author)

        try:
            im.save(output_file)
        except BaseException as err:
            print(f'Unexpected {err=}, {type(err)=} saving {output_file}')
            raise
        return output_file

    def choose_image(self, img_path):
        try:
            file_arr = os.listdir(img_path)
        except BaseException as err:
            print(f'Unexpected {err=}, {type(err)=} listing {img_path}')
            raise
        return img_path + random.choice(file_arr)

    def set_outfile(self, output_dir):
        if output_dir[::-1] != '/':
            output_dir += '/'
        path_pref = 'img'
        path_suff = datetime.datetime.now().strftime("%y%m%d_%H%M%S") + '.jpg'
        file_name = "_".join([path_pref, path_suff])
        return f'{output_dir}{file_name}'

    def __repr__(self):
        """Machine-friendly representation."""
        return f'MemeEngine.make_meme(path,text,author,width) -> img_path'

    def __str__(self):
        """User-friendly representation."""
        return f'MemeEngine.make_meme(path,text,author,width) -> img_path'


if __name__ == '__main__':
    """Used for testing the module."""
    me = MemeEngine('./images')
    new_img = me.make_meme('./_data/photos/dog/',
                           'What do you want human?',
                           'Luna the Destroyer')
