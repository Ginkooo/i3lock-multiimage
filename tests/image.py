import os
import tempfile
from unittest import TestCase

import PIL.Image

from src.images.image import Image, BadFileType

class ImageTests(TestCase):
    """Test Image encapsulation class"""

    def setUp(self):
        tmpdir = tempfile.gettempdir()

        img = PIL.Image.new('RGB', (10, 10))
        path = os.path.join(tmpdir, 'test.jpg')
        img.save(path)
        img.close()

        img = PIL.Image.new('RGB', (10, 10))
        path2 = os.path.join(tmpdir, 'asdf.png')
        img.save(path2)
        img.close()

        self.jpg_path = path
        self.png_path = path2

    def tearDown(self):
        os.remove(self.png_path)
        os.remove(self.jpg_path)

    def test_accepts_only_pngs(self):
        with self.assertRaises(BadFileType):
            _ = Image(self.jpg_path)

        _ = Image(self.png_path)

    def test_can_load_image(self):
        img = Image(self.png_path)

        self.assertTrue(hasattr(img, 'raw'))
        self.assertIsInstance(img.raw, PIL.Image.Image)
