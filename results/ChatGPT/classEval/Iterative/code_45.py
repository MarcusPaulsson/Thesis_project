from PIL import Image, ImageEnhance, ImageChops
import os

class ImageProcessor:
    """
    This is a class to process images, including loading, saving, resizing, rotating, and adjusting the brightness of images.
    """

    def __init__(self):
        """
        Initialize self.image
        """
        self.image = None

    def load_image(self, image_path):
        """
        Open an image using PIL.
        :param image_path: str, path of the image to be loaded
        """
        try:
            self.image = Image.open(image_path)
        except Exception as e:
            raise ValueError(f"Error loading image: {e}")

    def save_image(self, save_path):
        """
        Save the image to a specified path if the image is loaded.
        :param save_path: str, path where the image will be saved
        """
        if self.image is None:
            raise ValueError("No image loaded to save.")
        self.image.save(save_path)

    def resize_image(self, width, height):
        """
        Resize the loaded image to the specified dimensions.
        :param width: int, target width of the image
        :param height: int, target height of the image
        """
        if self.image is None:
            raise ValueError("No image loaded to resize.")
        self.image = self.image.resize((width, height))

    def rotate_image(self, degrees):
        """
        Rotate the loaded image by a specified number of degrees.
        :param degrees: float, degrees to rotate the image
        """
        if self.image is None:
            raise ValueError("No image loaded to rotate.")
        self.image = self.image.rotate(degrees, expand=True)

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of the loaded image.
        :param factor: float, brightness factor. 0.0 gives a black image, 1.0 gives the original image.
        """
        if self.image is None:
            raise ValueError("No image loaded to adjust brightness.")
        if factor < 0:
            raise ValueError("Brightness factor must be non-negative.")
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)