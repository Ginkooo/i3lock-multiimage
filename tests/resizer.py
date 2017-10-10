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
from unittest import TestCase, mock

from src.handles.resizer import Resizer


class ResizerTests(TestCase):

    def test_can_resize_images_to_screens(self):
        screen1 = mock.MagicMock()
        screen2 = mock.MagicMock()
        screen3 = mock.MagicMock()

        screen1.resolution = (13, 15)
        screen2.resolution = (12, 12)
        screen3.resolution = (11, 10)

        screens = [screen1, screen2, screen3]

        image1 = mock.MagicMock()
        image2 = mock.MagicMock()
        image3 = mock.MagicMock()

        images = [image1, image2, image3]

        sz = mock.PropertyMock()

        for im in images:
            type(im).size = sz

        pairs = []

        for sc, im in zip(screens, images):
            pair = namedtuple('pair', 'screen image')
            pair.screen = sc
            pair.image = im
            pairs.append(pair)

        Resizer.resize_pairs(pairs)

        call = mock.call

        expected = [call((13, 15)), call((12, 12)), call((11, 10))]

        self.assertEqual(expected, sz.mock_calls)
