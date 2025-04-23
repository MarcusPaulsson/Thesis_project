from PIL import Image, ImageEnhance

class ImageProcessor:
    """
    A class to process images, including loading, saving, resizing, rotating, and adjusting brightness.
    """

    def __init__(self):
        """Initialize the image processor with no image loaded."""
        self.image = None

    def load_image(self, image_path: str) -> None:
        """
        Load an image from the specified path.
        
        :param image_path: str, path of the image to load.
        """
        self.image = Image.open(image_path)

    def save_image(self, save_path: str) -> None:
        """
        Save the currently loaded image to the specified path.
        
        :param save_path: str, the path where the image will be saved.
        """
        if self.image is not None:
            self.image.save(save_path)

    def resize_image(self, width: int, height: int) -> None:
        """
        Resize the currently loaded image to the specified dimensions.
        
        :param width: int, the target width of the image.
        :param height: int, the target height of the image.
        """
        if self.image is not None:
            self.image = self.image.resize((width, height))

    def rotate_image(self, degrees: float) -> None:
        """
        Rotate the currently loaded image by the specified degrees.
        
        :param degrees: float, the degrees to rotate the image.
        """
        if self.image is not None:
            self.image = self.image.rotate(degrees)

    def adjust_brightness(self, factor: float) -> None:
        """
        Adjust the brightness of the currently loaded image.
        
        :param factor: float, brightness factor (0.0 for black, 1.0 for original).
        """
        if self.image is not None:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)