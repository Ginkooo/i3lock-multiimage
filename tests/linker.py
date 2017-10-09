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

from src.handles.linker import Linker


class LinkerTests(TestCase):
    """Linker Tests"""

    def test_can_return_image_screen_pairs(self):
        images1 = ('image{}'.format(x) for x in range(4))
        screens1 = ('screen{}'.format(str(x)) for x in range(4))
        images2 = ('image{}'.format(str(x)) for x in range(4))
        screens2 = ('screen{}'.format(str(x)) for x in range(6))
        images3 = ('image{}'.format(str(x)) for x in range(6))
        screens3 = ('screen{}'.format(str(x)) for x in range(4))

        linker1 = Linker(images=images1, screens=screens1)
        linker2 = Linker(images=images2, screens=screens2)
        linker3 = Linker(images=images3, screens=screens3)

        pairs1 = list(linker1.get_pairs())
        pairs2 = list(linker2.get_pairs())
        pairs3 = list(linker3.get_pairs())

        self.assertEqual('screen3', pairs1[3].screen)
        self.assertEqual('image3', pairs1[3].image)

        self.assertEqual(4, len(pairs1))
        self.assertEqual(4, len(pairs2))
        self.assertEqual(4, len(pairs3))

