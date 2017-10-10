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

from PIL import Image


class Displayer():
    """Scales images to screens and displays them"""

    def __init__(self, *, pairs: iter=[]):
        """Takes screen-image pairs

        :param pairs: iterable with screen-image pairs in a namedtuple
        """
        self.pairs = list(pairs)

    def make_background(self):
        """Makes one big Pillow image to put others image into"""
        size = self.get_full_size()
        bg = Image.new('RGB', size, color='#ffffff')
        for pair in self.pairs:
            image = pair.image
            screen = pair.screen
            print(screen.offset)
            bg.paste(image.raw, screen.offset)
        return bg

    def get_full_size(self):
        """Gets full background size

        :returns: (width, height) pair
        :rtype: tuple
        """
        width = self.get_full_width()
        height = self.get_full_height()

        return tuple([width, height])

    def get_full_width(self):
        """Get full background image width

        :returns: width
        :rtype: int
        """
        screens = (pair.screen for pair in self.pairs)
        max_ = 0
        for screen in screens:
            tmp = screen.resolution[0] + screen.offset[0]
            if tmp > max_:
                max_ = tmp
        return max_

    def get_full_height(self):
        """Gets full background image height

        :returns: height
        :rtype: int
        """
        screens = (pair.screen for pair in self.pairs)
        max_ = 0
        for screen in screens:
            tmp = screen.resolution[1] + screen.offset[1]
            if tmp > max_:
                max_ = tmp
        return max_
