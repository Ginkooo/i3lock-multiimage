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

from src.images.image import Image


class Reader():
    """Provice image reading methods"""

    @staticmethod
    def get_images(directory: str) -> iter:
        """Gets images from directory and returns a generator containing them

        :param directory: directory containing images
        :type directory: str

        :returns: generator with Images
        :rtype: iter
        """
        for filename in os.listdir(directory):
            yield Image(os.path.join(directory, filename))
