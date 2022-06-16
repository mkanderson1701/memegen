"""ImageText class responsible for adding meme text to the image.
Or other layered effects.
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random


class ImageTexter():
    """This class handles adding text to an image object."""

    font_path = './_data/fonts/impact.ttf'

    @classmethod
    def text_img(cls, im, text, author):
        """Resize an image to maximum (width) while maintaining aspect ratio.

        Return a pillow image object.
        """

        # add text flourishes
        author = '- ' + author
        text = '"' + text + '"'

        # image objects must be RGBA (not RGB/other) for transparency support.
        if im.mode != 'RGBA':
            im = im.convert(mode='RGBA')

        text_x = random.randrange(50, int(im.size[0] / 2))
        text_y = random.randrange(50, int(im.size[1] - 150))
        # print(f'Random location: {text_x}, {text_y}')

        quote_pos = (text_x, text_y)
        auth_pos = (text_x + 50, text_y + 75)

        quote_layer = cls.txt_layer(text, im.size, quote_pos)
        auth_layer = cls.txt_layer(author, im.size, auth_pos, False)

        merged = Image.alpha_composite(im, quote_layer)
        merged = Image.alpha_composite(merged, auth_layer)

        # Convert back to RGB for JPG format
        merged = merged.convert(mode='RGB')

        return merged

    @classmethod
    def txt_layer(cls, text, im_size, t_pos, resize=True):
        """Create a text layer to be merged with main image.

        text: string with quote, author, other
        im_size: pillow size tuple (width, height) for original
        t_pos: pillow coordinate tuple (horiz, vert) for text location

        make blank images for the text and author, same size as im,
        initialized to transparent text color
        """
        font_size = 25
        # random font fill color
        fill_color = (random.choice(range(256)), random.choice(range(256)),
                      random.choice(range(256)), 255)
        # Using the complimentary color for outline seems to be better than
        # white or black ... sometimes.
        stroke_color = (255 - fill_color[0], 255 - fill_color[1],
                        255 - fill_color[2], 255)

        text_layer = Image.new("RGBA", im_size, (255, 255, 255, 0))

        dt = ImageDraw.Draw(text_layer)

        # I don't resize the author
        if resize:
            font_size = cls.resize_font(text, im_size, font_size)

        the_font = ImageFont.truetype(font=cls.font_path, size=font_size)

        # check to make sure the text will fit in this position
        if the_font.getlength(text) + t_pos[0] > im_size[0]:
            new_x = im_size[0] - the_font.getlength(text) - 25
            new_pos = (new_x, t_pos[1])
        else:
            new_pos = t_pos

        dt.text(new_pos, text, font=the_font, fill=fill_color,
                stroke_width=1, stroke_fill=stroke_color)

        # This image object has transparent background with text.
        return text_layer

    @classmethod
    def resize_font(cls, text, im_size, font_size):
        """Recursive method to find a font size that fits the text on the page.

        If the length of the text object isn't close to the width of the page
        plus a margin, update font size and rerun
        """
        test_font = ImageFont.truetype(font=cls.font_path, size=font_size)
        # print(f'font size: {font_size}')
        if test_font.getlength(text) + 50 > im_size[0]:
            font_size -= 1
            # print(f'too big: font size {font_size} length {test_font.getlength(text)} im_size {im_size}')
            font_size = cls.resize_font(text, im_size, font_size)            
        elif test_font.getlength(text) < im_size[0] - 100:
            font_size += 1
            # print(f'too small: font size {font_size} length {test_font.getlength(text)} im_size {im_size}')
            font_size = cls.resize_font(text, im_size, font_size)
        return font_size

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
    im = ImageTexter.text_img(im, 'What do you want human? I have many things to do today.', 'Luna the Destroyer')
    im.save('./images/testimg.jpg')
