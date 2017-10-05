# Copyright (C) 2017  Piotr Czajka <digitalplasma@protonmail.com>
# Author: Piotr Czajka <digitalplasma@protonmail.com>
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

from unittest import TestCase
from src.xrandr.screen import Screen


class ScreenTests(TestCase):

    def setUp(self):
        self.hdmi0 = ('HDMI-0 connected primary 1920x1080+1920+0'
                      '(normal left invertex right x axis y axis)'
                      '598mm x 336 mm')
        self.vga0 = ('VGA-0 connected 1920x1080+0+0'
                     '(normal left inverted right x axis y axis)'
                     '521mm x 293mm')

    def test_can_encapsulate_xrandr_line(self):
        screen1 = Screen(self.hdmi0)
        screen2 = Screen(self.vga0)

        self.assertEqual('HDMI-0', screen1.name)
        self.assertEqual((1920, 1080), screen1.resolution)
        self.assertEqual((1920, 0), screen1.offset)

        self.assertEqual('VGA-0', screen2.name)
        self.assertEqual((1920, 1080), screen2.resolution)
        self.assertEqual((0, 0), screen2.offset)
