"""ImageText class responsible for adding meme text to the image.
Or other layered effects.
"""

import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


class ImageTexter():
    """This class handles adding text to an image object."""

    font_path = './_data/fonts/impact.ttf'

    @classmethod
    def text_img(cls, im, text, author):
        """Resize an image to maximum (width) while maintaining aspect ratio.

        Return a pillow image object.
        """

        # add the little hyphen to the author
        author = '- ' + author
        path_pref = 'img'
        path_suff = datetime.datetime.now().strftime("%y%m%d_%H%M%S") + '.png'
        file_name = "_".join([path_pref, path_suff])
        out_path = f'./images/{file_name}'

        # image objects must be RGBA (not RGB/other) for transparency support.
        if im.mode != 'RGBA':
            im = im.convert(mode='RGBA')

        quote_pos = (int(im.size[0] / 12), int(im.size[1] / 1.5))
        auth_pos = (int(im.size[0] / 2), int(im.size[1] / 1.25))

        quote_layer = cls.txt_layer(text, im.size, quote_pos)
        auth_layer = cls.txt_layer(author, im.size, auth_pos)

        merged = Image.alpha_composite(im, quote_layer)
        merged = Image.alpha_composite(merged, auth_layer)

        merged.save(out_path)

        return out_path

    @classmethod
    def txt_layer(cls, text, im_size, t_pos):
        """Create a text layer to be merged with main image.

        text: string with quote, author, other
        im_size: pillow size tuple (width, height) for original
        t_pos: pillow coordinate tuple (horiz, vert) for text location

        make blank images for the text and author, same size as im,
        initialized to transparent text color
        """
        text_layer = Image.new("RGBA", im_size, (255, 255, 255, 0))

        dt = ImageDraw.Draw(text_layer)
        the_font = ImageFont.truetype(font=cls.font_path, size=25)
        dt.text(t_pos, text, font=the_font, fill=(0, 0, 255, 255))

        # This image object has transparent background with text.
        return text_layer

    def __repr__(self):
        """Machine-friendly representation."""
        return f'ImageTexter.text_img(im,text,author) -> finished file path'

    def __str__(self):
        """User-friendly representation."""
        return f'ImageTexter.text_img(im,text,author) -> finished file path'


if __name__ == '__main__':
    """Used for testing the module."""
    im = Image.open('./_data/photos/dog/luna1.jpg')
    if im.size[0] > 500:
        im = im.resize((500, int(im.size[1] * 500 / im.size[0])))
    ImageTexter.text_img(im, 'What do you want human?', 'Luna the Destroyer')
