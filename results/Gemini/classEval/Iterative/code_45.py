from PIL import Image, ImageEnhance


class ImageProcessor:
    """
    This class processes images, including loading, saving, resizing, rotating, and adjusting brightness.
    """

    def __init__(self):
        """
        Initializes the ImageProcessor with no image loaded.
        """
        self.image = None

    def load_image(self, image_path):
        """
        Loads an image from the specified path using PIL.

        Args:
            image_path (str): The path to the image file.

        Raises:
            FileNotFoundError: If the image file is not found.
            Exception: If there is an error opening the image.
        """
        try:
            self.image = Image.open(image_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"Image file not found at {image_path}")
        except Exception as e:
            raise Exception(f"Could not open image at {image_path}: {e}")

    def save_image(self, save_path):
        """
        Saves the currently loaded image to the specified path.

        Args:
            save_path (str): The path to save the image to.

        Raises:
            ValueError: If no image is loaded.
            Exception: If there is an error saving the image.
        """
        if self.image:
            try:
                self.image.save(save_path)
            except Exception as e:
                raise Exception(f"Could not save image to {save_path}: {e}")
        else:
            raise ValueError("No image loaded to save.")

    def resize_image(self, width, height, resample=Image.LANCZOS):
        """
        Resizes the currently loaded image to the specified width and height.

        Args:
            width (int): The target width of the image.
            height (int): The target height of the image.
            resample: Resampling filter. Defaults to LANCZOS

        Raises:
            ValueError: If no image is loaded.
            ValueError: if width or height are not positive integers
            Exception: If there is an error resizing the image.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")

        if self.image:
            try:
                self.image = self.image.resize((width, height), resample=resample)
            except Exception as e:
                raise Exception(f"Could not resize image: {e}")
        else:
            raise ValueError("No image loaded to resize.")

    def rotate_image(self, degrees, expand=False):
        """
        Rotates the currently loaded image by the specified number of degrees.

        Args:
            degrees (float): The number of degrees to rotate the image by (clockwise).
            expand (bool): Whether the image should be expanded to fit the rotated image.

        Raises:
            ValueError: If no image is loaded.
            TypeError: if degrees is not a number
            Exception: If there is an error rotating the image.
        """
        if not isinstance(degrees, (int, float)):
            raise TypeError("Degrees must be a number.")

        if self.image:
            try:
                self.image = self.image.rotate(
                    -degrees, expand=expand
                )  # PIL rotates counterclockwise, so negating degrees
            except Exception as e:
                raise Exception(f"Could not rotate image: {e}")
        else:
            raise ValueError("No image loaded to rotate.")

    def adjust_brightness(self, factor):
        """
        Adjusts the brightness of the currently loaded image.

        Args:
            factor (float): The brightness factor. 1.0 gives the original image.

        Raises:
            ValueError: If no image is loaded.
            TypeError: If factor is not a number.
            ValueError: if factor is negative
            Exception: If there is an error adjusting the brightness.
        """
        if not isinstance(factor, (int, float)):
            raise TypeError("Factor must be a number.")

        if factor < 0:
            raise ValueError("Factor must be non-negative.")

        if self.image:
            try:
                enhancer = ImageEnhance.Brightness(self.image)
                self.image = enhancer.enhance(factor)
            except Exception as e:
                raise Exception(f"Could not adjust brightness: {e}")
        else:
            raise ValueError("No image loaded to adjust brightness.")