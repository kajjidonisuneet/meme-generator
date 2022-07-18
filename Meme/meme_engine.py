"""This module has all the methods and image manipulation functions."""

import os
import random
import textwrap
from PIL import Image, ImageFont, ImageDraw


class MemeEngine:
    """The engine behind the meme genration."""

    def __init__(self, out_dir: str) -> None:
        """Save and creates (if needed) the output director's path.

        :param out_dir: Path of the output director.
        """
        self.out_dir = out_dir

        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """To create the meme.

        To create the meme using given image, text, author and
        width of the image.

        :param img_path: The path of the image file.
        :param text: The text (quote) that needs to be added to the image.
        :param author: The author of the quote that needs to be
        added to the image.
        :param width: The width of the image in pixel.
        """
        try:
            img = Image.open(img_path)
            height = int((width * img.height)/img.width)
            new_img = img.resize((width, height))
        except Exception as error:
            print(f'Error occurred during opening of the Image.'
                  f' Details of error "{error}"')
            raise Exception("Image Opening Error")

        font_quote = ImageFont.truetype(
            font='_data/Font/LilitaOne-Regular.ttf',
            size=25
            )
        font_author = ImageFont.truetype(
            font='_data/Font/LilitaOne-Regular.ttf',
            size=20
            )
        text_colour = (0, 0, 0)
        stroke_colour = (255, 255, 255)

        try:
            draw = ImageDraw.Draw(new_img)
            if font_quote.getsize(text)[0] > new_img.width:
                line_split = int((new_img.width - 60) /
                                 (font_quote.getsize(text)[0]/len(text)))
                multi_line_text = textwrap.wrap(text, width=line_split)
                multi_line_height = ((font_quote.getsize(text)[1] + 5) *
                                     len(multi_line_text))
                text_height_postion = random.randint(50, (height -
                                                     multi_line_height-30))
                for line in multi_line_text:
                    draw.text((30, text_height_postion), line,
                              fill=text_colour,
                              font=font_quote, stroke_width=1,
                              stroke_fill=stroke_colour)
                    text_height_postion = (text_height_postion +
                                           font_quote.getsize(line)[1] + 5)
                draw.text((30, text_height_postion + 5), f'- {author}',
                          fill=text_colour, font=font_author, stroke_width=1,
                          stroke_fill=stroke_colour)
            else:
                text_height_postion = random.randint(50, height-50)
                draw.text((30, text_height_postion), text, fill=text_colour,
                          font=font_quote, stroke_width=1,
                          stroke_fill=stroke_colour)
                draw.text((30, text_height_postion + 25), f'- {author}',
                          fill=text_colour, font=font_author, stroke_width=1,
                          stroke_fill=stroke_colour)

        except Exception as error:
            print(f'Error occurred during manipulation of the image.'
                  f' Details of error "{error}"')
            raise Exception("Image Manipulation Error")

        try:
            outfile_location = os.path.join(self.out_dir,
                                            f'{random.randint(1, 100000)}.png')
            new_img.save(outfile_location)
        except Exception as error:
            print(f'Error occurred during saving of the meme image.'
                  f' Details of error "{error}"')
            raise Exception("Image Saving Error")

        return outfile_location
