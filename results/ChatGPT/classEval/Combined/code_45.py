from PIL import Image, ImageEnhance, ImageChops
import os

class ImageProcessor:
    """
    A class to process images, including loading, saving, resizing,
    rotating, and adjusting the brightness of images.
    """

    def __init__(self):
        """Initialize self.image to None."""
        self.image = None

    def load_image(self, image_path: str):
        """
        Load an image from the specified path.
        
        :param image_path: str, path of the image to be loaded.
        """
        self.image = Image.open(image_path)

    def save_image(self, save_path: str):
        """
        Save the current image to the specified path if it is loaded.
        
        :param save_path: str, the path where the image will be saved.
        """
        if self.image is not None:
            self.image.save(save_path)

    def resize_image(self, width: int, height: int):
        """
        Resize the loaded image to the specified width and height.
        
        :param width: int, target width of the image.
        :param height: int, target height of the image.
        """
        if self.image is not None:
            self.image = self.image.resize((width, height))

    def rotate_image(self, degrees: float):
        """
        Rotate the loaded image by the specified degrees.
        
        :param degrees: float, degrees to rotate the image.
        """
        if self.image is not None:
            self.image = self.image.rotate(degrees)

    def adjust_brightness(self, factor: float):
        """
        Adjust the brightness of the loaded image based on the given factor.
        
        :param factor: float, brightness factor. A factor of 0.0 gives a black image,
                       and 1.0 gives the original image.
        """
        if self.image is not None:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)

    def close_image(self):
        """Close the current image if it is loaded."""
        if self.image is not None:
            self.image.close()
            self.image = None

# Unit tests can be added to verify the functionality of the ImageProcessor class.