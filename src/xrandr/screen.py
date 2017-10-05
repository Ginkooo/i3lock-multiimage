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

import re


class Screen():
    """Represents a single screen"""

    pattern = re.compile(
                    '(.+?)\sconnected\s(?:[a-z]+)?\s?(\d+x\d+)\+(\d+\+\d+)'
                    )

    def __init__(self, xrandrline: str):
        """Decodes primary screen line from xrandr output and
        encapsulates it in self

        :param xrandrline: Line from xrandr output
                           (primary one, (HDMI-1 connected) etc.
        :type xrandrline: str
        """
        name, res, offset = Screen.__get_screen_info(xrandrline)

        self.name = name
        self.resolution = res
        self.offset = offset

    @staticmethod
    def __get_screen_info(xrandrline: str):
        """searches given line for name, resolution and offset
        and returns a tuple containing them

        :param xrandrline:
        :type xrandrline: str
        """
        match = re.search(Screen.pattern, xrandrline)

        name = match.group(1)
        resolution = tuple([int(x) for x in match.group(2).split('x')])
        offset = tuple([int(x) for x in match.group(3).split('+')])

        return tuple([name, resolution, offset])
