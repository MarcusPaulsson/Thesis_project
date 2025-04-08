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
        :param image_path: str, path of image that is to be loaded
        """
        try:
            self.image = Image.open(image_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Image file not found at: {image_path}")
        except Exception as e:
            raise Exception(f"Error loading image: {e}")

    def save_image(self, save_path):
        """
        Save image to a path if image has been loaded
        :param save_path: str, the path that the image will be saved to
        """
        if self.image:
            try:
                self.image.save(save_path)
            except Exception as e:
                raise Exception(f"Error saving image: {e}")
        else:
            raise ValueError("No image loaded to save.")

    def resize_image(self, width, height):
        """
        Resize the image if image has been loaded.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image:
            try:
                self.image = self.image.resize((width, height))
            except Exception as e:
                raise Exception(f"Error resizing image: {e}")
        else:
            raise ValueError("No image loaded to resize.")

    def rotate_image(self, degrees):
        """
        Rotate image if image has been loaded
        :param degrees: float, the degrees that the image will be rotated
        """
        if self.image:
            try:
                self.image = self.image.rotate(degrees)
            except Exception as e:
                raise Exception(f"Error rotating image: {e}")
        else:
            raise ValueError("No image loaded to rotate.")

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has been loaded.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        """
        if self.image:
            try:
                enhancer = ImageEnhance.Brightness(self.image)
                self.image = enhancer.enhance(factor)
            except Exception as e:
                raise Exception(f"Error adjusting brightness: {e}")
        else:
            raise ValueError("No image loaded to adjust brightness.")