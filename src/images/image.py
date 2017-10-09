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

import imghdr
import PIL.Image


class BadFileType(Exception):
    pass


class Image():
    """Encapsulates Pillow image"""

    def __init__(self, filepath: str):
        """takes image filepath and makes PIL Image
        from it. Accepts only PNG images.

        :param filepath: path to image file
        :type filepath: str
        """
        Image.__assert_png(filepath)
        self.raw = Image._create_raw_pillow_image_from_file(filepath)

    @staticmethod
    def __assert_png(filepath: str):
        """Raises error if file is not a png

        :param filepath: path to image file
        :type filepath: str
        """
        type_ = imghdr.what(filepath)
        if type_ != 'png':
            raise BadFileType('{} is not a PNG file'.format(filepath))

    @staticmethod
    def _create_raw_pillow_image_from_file(filepath: str) -> PIL.Image:
        """Loads given image file and creates Pillow Image from it

        :param filepath: Path to the image file
        :type filepath: str

        :rtype: PIL.Image
        """
        image = PIL.Image.open(filepath)
        return image

    @property
    def size(self) -> tuple:
        """Gets image size

        :returns: (width, height) pair
        :rtype: tuple
        """
        return self.raw.size

    @size.setter
    def size(self, new_size):
        self.raw = self.raw.resize(new_size)
