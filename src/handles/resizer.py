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


class Resizer():
    """It is to contain image sequences rezisement tools"""

    @staticmethod
    def resize_pairs(pairs: iter):
        """Takes screen image pair and resizes each image to the screen

        :param pairs: image, screen pair
        :type pairs: namedtuple

        :returns: new resized pairs
        :rtype: iter
        """
        for pair in pairs:
            image = pair.image
            screen = pair.screen
            image.size = screen.resolution

        return pairs
