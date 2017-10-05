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
    """Represents a single screen (to be honest, output)"""

    pattern = re.compile(
                    '(.+?)\sconnected\s'
                    '(?:[a-z]+)?\s?(\d+x\d+)\+(\d+\+\d+)\s?(\w*)'
                    )

    def __init__(self, xrandrline: str):
        """Decodes primary screen line from xrandr output and
        encapsulates it in self

        :param xrandrline: Line from xrandr output
                           (primary one, (HDMI-1 connected) etc.
        :type xrandrline: str
        """
        name, res, offset, rotation = Screen.__get_screen_info(xrandrline)

        self.name = name
        self.resolution = res
        self.offset = offset
        self.rotation = rotation

    @staticmethod
    def __map_rotation_to_int(rotation: str) -> int:
        """Takes xrandr rotation string and returns rotation angle

        :param rotation: xrandr rotation string
        :type rotation: str

        :returns: rotation
        :rtype: int
        """
        mapping = {
                'right': 90,
                'left': -90,
                'inverted': 180,
                '': 0,
                }

        try:
            rotation = mapping[rotation]
        except KeyError:
            raise ValueError('Unsupported monitor rotation {}'
                             .format(rotation))
        return rotation

    @staticmethod
    def __get_screen_info(xrandrline: str) -> tuple:
        """searches given line for name, resolution and offset
        and returns a tuple containing them

        :param xrandrline: "connected" line from xrandr
        :type xrandrline: str

        :returns: tuple containing information about display in format
                    (name, resolution, offset, rotation)
        """
        match = re.search(Screen.pattern, xrandrline)

        name = match.group(1)
        resolution = tuple([int(x) for x in match.group(2).split('x')])
        offset = tuple([int(x) for x in match.group(3).split('+')])
        rotation = match.group(4)
        rotation = Screen.__map_rotation_to_int(rotation)

        return tuple([name, resolution, offset, rotation])
