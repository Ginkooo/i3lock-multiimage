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
from src.xrandr.xrandr import Xrandr


class XrandrTests(TestCase):

    def setUp(self):
        self.prep = ('Screen 0: minimum 320 x 200, current 3840 x 1080, '
                     ' maximum 8192 x 8192\n'
                     'HDMI-0 connected primary 1920x1080+1920+0 '
                     '(normal left inverted right x axis y axis) 598mm x 336mm\n'
                     '1920x1080     60.00*+  50.00    59.94    30.00    25.00\n'
                     '    24.00    29.97    23.98  \n'
                     '1920x1080i    60.00    50.00    59.94  \n'
                     '1600x1200     60.00  \n'
                     '1680x1050     59.88  \n'
                     '1280x1024     75.02    60.02  \n'
                     '1440x900      74.98    59.90  \n'
                     '1280x960      60.00  \n'
                     '1360x768      60.02  \n'
                     '1280x800      59.91  \n'
                     '1152x864      75.00  \n'
                     '1280x720      60.00    50.00    59.94  \n'
                     '1024x768      75.03    70.07    60.00  \n'
                     '832x624       74.55  \n'
                     '800x600       72.19    75.00    60.32  \n'
                     '720x576       50.00  \n'
                     '720x480       60.00    59.94  \n'
                     '640x480       75.00    72.81    66.67    60.00    59.94 \n'
                     '720x400       70.08  \n'
                     'VGA-0 connected 1920x1080+0+0 '
                     '(normal left inverted right x axis y axis) 521mm x 293mm\n'
                     '1920x1080     60.00*+\n'
                     '1280x1024     60.02  \n'
                     '1440x900      59.89  \n'
                     '1280x800      59.81  \n'
                     '1152x864      75.00  \n'
                     '1024x768      70.07    60.00  \n'
                     '800x600       60.32    56.25  \n'
                     '640x480       66.67    59.94  \n'
                     '720x400       70.08  \n'
                     'DVI-0 disconnected '
                     '(normal left inverted right x axis y axis)\n')

    def test_can_return_correct_screens(self):
        mock.FILTER_DIR = False

        with mock.patch.object(Xrandr, '_Xrandr__get_xrandr_output',
                               return_value=self.prep):
            screens = Xrandr.get_monitors()
            screens = list(screens)

        self.assertEqual(2, len(screens))
        self.assertEqual((1920, 1080), screens[0].resolution)
        self.assertEqual((1920, 1080), screens[1].resolution)

        mock.FILTER_DIR = True
