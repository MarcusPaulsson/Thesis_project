from PIL import Image, ImageEnhance, ImageChops
import os

class ImageProcessor:
    """
    This is a class to process image, including loading, saving, resizing, rotating, and adjusting the brightness of images.
    """

    def __init__(self):
        """
        Initialize self.image
        """
        self.image = None

    def load_image(self, image_path):
        """
        Use Image util in PIL to open a image
        :param image_path: str, path of image that is to be
        """
        try:
            self.image = Image.open(image_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Image file not found at {image_path}")
        except Exception as e:
            raise Exception(f"Could not open image. {e}")

    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        """
        if not self.image:
            raise ValueError("No image loaded to save.")

        try:
            self.image.save(save_path)
        except Exception as e:
            raise Exception(f"Could not save image. {e}")

    def resize_image(self, width, height):
        """
        Resize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if not self.image:
            raise ValueError("No image loaded to resize.")

        try:
            self.image = self.image.resize((width, height))
        except Exception as e:
            raise Exception(f"Could not resize image. {e}")

    def rotate_image(self, degrees):
        """
        Rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        """
        if not self.image:
            raise ValueError("No image loaded to rotate.")

        try:
            self.image = self.image.rotate(degrees)
        except Exception as e:
            raise Exception(f"Could not rotate image. {e}")

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        """
        if not self.image:
            raise ValueError("No image loaded to adjust brightness.")

        try:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)
        except Exception as e:
            raise Exception(f"Could not adjust brightness. {e}")