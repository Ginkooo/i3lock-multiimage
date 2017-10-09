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

from unittest import TestCase, mock
from collections import namedtuple

from src.handles.displayer import Displayer


class DisplayerTests(TestCase):
    """Scaling and displaying images on one big background tests"""

    def test_can_get_full_size(self):

        screen1 = mock.MagicMock()
        screen2 = mock.MagicMock()
        screen3 = mock.MagicMock()
        screen4 = mock.MagicMock()

        # up left screen
        screen1.resolution = (600, 700)
        screen1.offset = (0, 0)
        # up right screen
        screen2.resolution = (1000, 500)
        screen2.offset = (600, 0)
        # down left screen
        screen3.resolution = (400, 300)
        screen3.offset = (0, 700)
        # down right screen
        screen4.resolution = (200, 100)
        screen4.offset = (400, 500)

        screens = [screen1, screen2, screen3, screen4]

        pairs = self._pair_screens_with_images(screens)

        displayer = Displayer(pairs=pairs)

        size = displayer.get_full_size()

        self.assertEqual(tuple([1600, 1000]), size)

    def _pair_screens_with_images(self, screens):
        image = mock.MagicMock()
        for sc in screens:
            pair = namedtuple('pair', 'screen image')
            pair.screen = sc
            pair.image = image
            yield pair

