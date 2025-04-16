from PIL import Image, ImageEnhance
from PIL import ImageChops

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
            print(f"Error: Image file not found at {image_path}")
        except Exception as e:
            print(f"Error loading image: {e}")

    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        """
        if self.image:
            try:
                self.image.save(save_path)
            except Exception as e:
                print(f"Error saving image: {e}")
        else:
            print("Error: No image loaded to save.")

    def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image:
            try:
                self.image = self.image.resize((width, height))
            except Exception as e:
                print(f"Error resizing image: {e}")
        else:
            print("Error: No image loaded to resize.")

    def rotate_image(self, degrees):
        """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        """
        if self.image:
            try:
                self.image = self.image.rotate(degrees)
            except Exception as e:
                print(f"Error rotating image: {e}")
        else:
            print("Error: No image loaded to rotate.")

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        """
        if self.image:
            try:
                enhancer = ImageEnhance.Brightness(self.image)
                self.image = enhancer.enhance(factor)
            except Exception as e:
                print(f"Error adjusting brightness: {e}")
        else:
            print("Error: No image loaded to adjust brightness.")