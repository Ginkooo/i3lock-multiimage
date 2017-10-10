# Copyright (C) 2017  Piotr Czajka <czajka@protonmail.com>
# Author: Piotr Czajka <czajka@protonmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

    def test_can_be_resized(self):
        img = Image(self.png_path)
        img.size = (23, 32)

        self.assertEqual((23, 32), img.size)

    def test_can_make_new_image_from_resolution(self):
        res = (40, 30)
        img = Image.new(res)

        self.assertEqual((40, 30), img.size)
