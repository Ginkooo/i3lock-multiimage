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

from collections import namedtuple

from src.xrandr.screen import Screen
from src.images.image import Image


class Linker():
    """Class linking images to monitors"""

    def __init__(self, *, images: iter=None, screens: iter=None):
        """__init__

        :param images: all images
        :type images: iter of Images
        :param screens: all screens
        :type screens: iter of Screens
        """
        self.images = images
        self.screens = screens

    def get_pairs(self) -> iter:
        """Pairs images and screen


        :returns: (image, screen pairs)
        :rtype: iter
        """
        pair = namedtuple('pair', 'image screen')

        zipped = zip(self.images, self.screens)

        pairs = (pair(image, screen) for image, screen in zipped)
        return pairs
