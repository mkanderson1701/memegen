"""ImageSizer class responsible for resizing an image.
Or applying other spatial transformations.
"""

from PIL import Image
from PIL import ImageOps
import os


class ImageSizer():
    """This class handles all image spatial translations."""

    @classmethod
    def resize_img(cls, img_path, width):
        """Resize an image to maximum (width) while maintaining aspect ratio.

        Return a pillow image object.
        """
        # print(f'passed dir is {os.path.abspath(img_path)}')
        try:
            im = Image.open(img_path)
        except FileNotFoundError as err:
            print(f'Unexpected {err=}, {type(err)=} opening {img_path}')
            raise
        except BaseException as err:
            print(f'Unexpected {err=}, {type(err)=} opening {img_path}')
            raise

        # Some images are only rotated due to EXIF data, honor that
        im = ImageOps.exif_transpose(im)
        if im.size[0] > width:
            im = im.resize((width, int(im.size[1] * width / im.size[0])))
        return im

    def __repr__(self):
        """Machine-friendly representation."""
        return f'ImageSizer.resize_img(path,width) -> pillow image object'

    def __str__(self):
        """User-friendly representation."""
        return f'ImageSizer.resize_img(path,width) -> pillow image object'


if __name__ == '__main__':
    """Used for testing the module."""
    ImageSizer.resize_img('./_data/photos/dog/luna1.jpg', 500)
