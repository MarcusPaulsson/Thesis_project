from PIL import Image, ImageEnhance

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
        Use Image util in PIL to open an image
        :param image_path: str, path of image that is to be loaded
        >>> processor = ImageProcessor()
        >>> processor.load_image('test.jpg')
        >>> processor.image
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x...>
        """
        self.image = Image.open(image_path)

    def save_image(self, save_path):
        """
        Save image to a path if the image has been opened
        :param save_path: str, the path that the image will be saved
        >>> processor = ImageProcessor()
        >>> processor.load_image('test.jpg')
        >>> processor.save_image('test2.jpg')
        """
        if self.image is not None:
            self.image.save(save_path)

    def resize_image(self, width, height):
        """
        Resize the image if the image has been opened.
        :param width: int, the target width of the image
        :param height: int, the target height of the image
        >>> processor = ImageProcessor()
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(300, 300)
        >>> processor.image.width
        300
        >>> processor.image.height
        300
        """
        if self.image is not None:
            self.image = self.image.resize((width, height))

    def rotate_image(self, degrees):
        """
        Rotate the image if the image has been opened
        :param degrees: float, the degrees that the image will be rotated
        >>> processor = ImageProcessor()
        >>> processor.load_image('test.jpg')
        >>> processor.rotate_image(90)
        """
        if self.image is not None:
            self.image = self.image.rotate(degrees)

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of the image if the image has been opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        >>> processor = ImageProcessor()
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
        if self.image is not None:
            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(factor)