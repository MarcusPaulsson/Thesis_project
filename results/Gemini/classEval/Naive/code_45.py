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
        :param image_path: str, path of image that is to be loaded
        """
        try:
            self.image = Image.open(image_path)
        except FileNotFoundError:
            print(f"Error: Image file not found at {image_path}")
            self.image = None  # Ensure image is None if loading fails
        except Exception as e:
            print(f"Error: Could not open image. {e}")
            self.image = None

    def save_image(self, save_path):
        """
        Save image to a path if image has opened
        :param save_path: str, the path that the image will be saved
        """
        if self.image:
            try:
                self.image.save(save_path)
            except Exception as e:
                print(f"Error: Could not save image. {e}")
        else:
            print("Error: No image loaded to save.")

    def resize_image(self, width, height):
        """
        Resize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image:
            try:
                self.image = self.image.resize((width, height))
            except Exception as e:
                print(f"Error: Could not resize image. {e}")
        else:
            print("Error: No image loaded to resize.")

    def rotate_image(self, degrees):
        """
        Rotate image if image has opened
        :param degrees: float, the degrees that the image will be rotated
        """
        if self.image:
            try:
                self.image = self.image.rotate(-degrees)  #PIL rotates counterclockwise
            except Exception as e:
                print(f"Error: Could not rotate image. {e}")
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
                print(f"Error: Could not adjust brightness. {e}")
        else:
            print("Error: No image loaded to adjust brightness.")


if __name__ == '__main__':
    # Example Usage (requires a test.jpg file in the same directory)
    processor = ImageProcessor()
    processor.load_image('test.jpg')

    if processor.image: #Only proceed if image loaded successfully
        processor.resize_image(300, 300)
        processor.rotate_image(45)
        processor.adjust_brightness(1.5)
        processor.save_image('test_processed.jpg')

        print("Image processing complete.  Check for test_processed.jpg")
    else:
        print("Image processing failed to load the image.")