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
from unittest import TestCase, mock

from src.images.reader import Reader


class ReaderTests(TestCase):
    """Reader class tests"""

    def setUp(self):
        filename = 'exaplefilename'
        self.tmpdir = tempfile.gettempdir()
        self.path = os.path.join(self.tmpdir, filename)
        with open(self.path, 'w'):
            pass

    def tearDown(self):
        os.remove(self.path)

    @mock.patch('src.images.image.Image')
    def test_can_return_images_iter(self, Image):
        images = Reader.get_images(self.tmpdir)
        self.assertTrue(images)
        self.assertEqual('Image', next(images).__class__.__name__)
