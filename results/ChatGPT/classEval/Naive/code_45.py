from PIL import Image, ImageEnhance

class ImageProcessor:
    """
    This class processes images, including loading, saving, resizing, rotating, and adjusting brightness.
    """

    def __init__(self):
        """Initialize the image attribute."""
        self.image = None

    def load_image(self, image_path):
        """
        Load an image using PIL.
        :param image_path: str, path of the image to be loaded.
        """
        self.image = Image.open(image_path)

    def save_image(self, save_path):
        """
        Save the image to a specified path if an image has been loaded.
        :param save_path: str, the path where the image will be saved.
        """
        if self.image is not None:
            self.image.save(save_path)
        else:
            raise ValueError("No image has been loaded to save.")

    def resize_image(self, width, height):
        """
        Resize the image if it has been loaded.
        :param width: int, target width of the image.
        :param height: int, target height of the image.
        """
        if self.image is not None:
            self.image = self.image.resize((width, height))
        else:
            raise ValueError("No image has been loaded to resize.")

    def rotate_image(self, degrees):
        """
        Rotate the image if it has been loaded.
        :param degrees: float, degrees to rotate the image.
        """
        if self.image is not None:
            self.image = self.image.rotate(degrees)
        else:
            raise ValueError("No image has been loaded to rotate.")

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of the image if it has been loaded.
        :param factor: float, brightness factor (0.0 for black, 1.0 for original).
        """
        if self.image is not None:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)
        else:
            raise ValueError("No image has been loaded to adjust brightness.")