from PIL import Image, ImageDraw, ImageFont
import os
import random


class MemeGenerator:
    """A class for generating memes."""

    def __init__(self, output_dir):
        """Initialize a new instance of the MemeGenerator class.

        Args:
            output_dir (str): The directory to save generated memes to.
        """
        self.output_dir = output_dir
        self.caption_font_path = "memeengine/fonts/Montserrat-SemiBold.ttf"
        self.author_font_path = "memeengine/fonts/Montserrat-Italic.ttf"

    def _load_image(self, img_path):
        """Load an image from disk using Pillow.

        Args:
            img_path (str): The path to the input image file.

        Returns:
            Image: The loaded image.
        """
        return Image.open(img_path)

    def _resize_image(self, img, width):
        """Resize an image while maintaining the aspect ratio.

        Args:
            img (Image): The input image.
            width (int): The maximum width of the output image.

        Returns:
            Image: The resized image.
        """
        w, h = img.size
        if w > width:
            ratio = width / float(w)
            height = int(ratio * h)
            img = img.resize((width, height), Image.ANTIALIAS)
        return img

    def _add_caption(self, img, text, author):
        """Add caption to the image"""
        width, height = img.size
        draw = ImageDraw.Draw(img)
        caption_font = ImageFont.truetype(self.caption_font_path, size=30)
        author_font = ImageFont.truetype(self.author_font_path, size=25)
    
        # Adjust the size and position of the caption based on the image width
        caption_width, caption_height = draw.textsize(text, font=caption_font)
        if caption_width > width:
            caption_font = ImageFont.truetype(self.caption_font_path, size=20)  # Decrease font size for longer captions
            caption_width, caption_height = draw.textsize(text, font=caption_font)
        caption_x = (width - caption_width) // 2
        caption_y = height - caption_height - 10
    
        draw.text((caption_x, caption_y), text, font=caption_font, fill="white")

        if author:
            author_width, author_height = draw.textsize(author, font=author_font)
            author_x = (width - author_width) // 2
            author_y = caption_y - author_height - 10
            draw.text((author_x, author_y), author, font=author_font, fill="white")

    def make_meme(self, img_path, text, author):
        """Generate a meme given an image path, a quote, and an author.

        Args:
            img_path (str): The path to the input image file.
            text (str): The caption text to add to the image.
            author (str): The author of the caption.

        Returns:
            str: The path to the output image file.
        """
        img = self._load_image(img_path)
        img = self._resize_image(img, 500)
        self._add_caption(img, text, author)
        output_path = os.path.join(self.output_dir, f"meme_{random.randint(0, 1000000)}.jpg")
        img.save(output_path)
        return output_path
