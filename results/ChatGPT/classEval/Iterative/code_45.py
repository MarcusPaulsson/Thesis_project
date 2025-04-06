from PIL import Image, ImageEnhance
import os

class ImageProcessor:
    """
    A class to process images, including loading, saving, resizing,
    rotating, and adjusting the brightness of images.
    """

    def __init__(self):
        """
        Initialize self.image to None.
        """
        self.image = None

    def load_image(self, image_path):
        """
        Load an image from the specified path.
        :param image_path: str, path of the image to be loaded.
        :raises FileNotFoundError: If the image file does not exist.
        :raises IOError: If the image cannot be opened.
        """
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"The file {image_path} does not exist.")
        
        try:
            self.image = Image.open(image_path)
        except IOError as e:
            raise IOError(f"Unable to open image file {image_path}: {e}")

    def save_image(self, save_path):
        """
        Save the loaded image to the specified path.
        :param save_path: str, path where the image will be saved.
        :raises ValueError: If there is no image to save.
        """
        if self.image is None:
            raise ValueError("No image loaded. Please load an image before saving.")
        
        self.image.save(save_path)

    def resize_image(self, width, height):
        """
        Resize the loaded image to the specified width and height.
        :param width: int, target width of the image.
        :param height: int, target height of the image.
        :raises ValueError: If there is no image loaded.
        """
        if self.image is None:
            raise ValueError("No image loaded. Please load an image before resizing.")
        
        self.image = self.image.resize((width, height))

    def rotate_image(self, degrees):
        """
        Rotate the loaded image by the specified degrees.
        :param degrees: float, degrees to rotate the image.
        :raises ValueError: If there is no image loaded.
        """
        if self.image is None:
            raise ValueError("No image loaded. Please load an image before rotating.")
        
        self.image = self.image.rotate(degrees)

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of the loaded image.
        :param factor: float, brightness factor (0.0 for black, 1.0 for original).
        :raises ValueError: If there is no image loaded.
        """
        if self.image is None:
            raise ValueError("No image loaded. Please load an image before adjusting brightness.")
        
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)