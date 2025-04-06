from PIL import Image, ImageEnhance

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
        >>> processor.load_image('test.jpg')
        >>> processor.image
        <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=3072x4096 at 0x194F2412A48>
        """
        try:
            self.image = Image.open(image_path)
        except FileNotFoundError:
            print(f"Error: Image file not found at {image_path}")
        except Exception as e:
            print(f"Error: Could not open image. {e}")

    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        >>> processor.load_image('test.jpg')
        >>> processor.save_image('test2.jpg')
        """
        if self.image:
            try:
                self.image.save(save_path)
            except Exception as e:
                print(f"Error: Could not save image. {e}")
        else:
            print("Error: No image loaded.")

    def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(300, 300)
        >>> processor.image.width
        300
        >>> processor.image.height
        300
        """
        if self.image:
            try:
                self.image = self.image.resize((width, height))
            except Exception as e:
                print(f"Error: Could not resize image. {e}")
        else:
            print("Error: No image loaded.")

    def rotate_image(self, degrees):
        """
        rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(90)
        """
        if self.image:
            try:
                self.image = self.image.rotate(degrees)
            except Exception as e:
                print(f"Error: Could not rotate image. {e}")
        else:
            print("Error: No image loaded.")

    def adjust_brightness(self, factor):
        """
        Adjust the brightness of image if image has opened.
        :param factor: float, brightness of an image. A factor of 0.0 gives a black image. A factor of 1.0 gives the original image.
        >>> processor.load_image('test.jpg')
        >>> processor.adjust_brightness(0.5)
        """
        if self.image:
            try:
                enhancer = ImageEnhance.Brightness(self.image)
                self.image = enhancer.enhance(factor)
            except Exception as e:
                print(f"Error: Could not adjust brightness. {e}")
        else:
            print("Error: No image loaded.")

if __name__ == '__main__':
    processor = ImageProcessor()
    processor.load_image('test.jpg')  # Replace 'test.jpg' with an actual image path
    if processor.image:
        processor.resize_image(300, 300)
        processor.rotate_image(90)
        processor.adjust_brightness(0.5)
        processor.save_image('test_processed.jpg')  # Replace 'test_processed.jpg' with desired save path