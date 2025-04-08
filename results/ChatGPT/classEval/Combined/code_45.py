from PIL import Image, ImageEnhance, ImageChops
import os


class ImageProcessor:
    """
    A class to process images, including loading, saving, resizing,
    rotating, and adjusting brightness.
    """

    def __init__(self):
        """Initialize an empty image."""
        self.image = None

    def load_image(self, image_path: str):
        """Load an image from the specified path.

        :param image_path: Path to the image file.
        """
        self.image = Image.open(image_path)

    def save_image(self, save_path: str):
        """Save the current image to the specified path.

        :param save_path: Path where the image will be saved.
        :raises ValueError: If no image is loaded.
        """
        if self.image is None:
            raise ValueError("No image loaded. Please load an image before saving.")
        
        self.image.save(save_path)

    def resize_image(self, width: int, height: int):
        """Resize the loaded image to the specified dimensions.

        :param width: Target width of the image.
        :param height: Target height of the image.
        :raises ValueError: If no image is loaded.
        """
        if self.image is None:
            raise ValueError("No image loaded. Please load an image before resizing.")
        
        self.image = self.image.resize((width, height))

    def rotate_image(self, degrees: float):
        """Rotate the loaded image by the specified degrees.

        :param degrees: Degrees to rotate the image.
        :raises ValueError: If no image is loaded.
        """
        if self.image is None:
            raise ValueError("No image loaded. Please load an image before rotating.")
        
        self.image = self.image.rotate(degrees)

    def adjust_brightness(self, factor: float):
        """Adjust the brightness of the loaded image.

        :param factor: Brightness adjustment factor (0.0 produces black, 1.0 is original).
        :raises ValueError: If no image is loaded.
        """
        if self.image is None:
            raise ValueError("No image loaded. Please load an image before adjusting brightness.")
        
        enhancer = ImageEnhance.Brightness(self.image)
        self.image = enhancer.enhance(factor)