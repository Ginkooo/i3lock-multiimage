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

import subprocess
from src.xrandr.screen import Screen


class Xrandr():
    """Contains methods to deal with xrandr program"""

    @staticmethod
    def get_monitors() -> iter:
        """Gets monitors info and returns iterator with Screens

        :rtype: iter
        """

        try:
            output = Xrandr.__get_xrandr_output()
        except:
            raise Exception('Please install xrandr '
                            'or give this script permissions to install it')
        for line in output.splitlines():
            if 'connected' in line and 'disconnected' not in line:
                yield Screen(line)

    @staticmethod
    def __get_xrandr_output() -> str:
        """calls xrandr to get output and returns it as str

        :returns: xrand output
        :rtype: str
        """
        output = subprocess.check_output(['xrandr'])
        output = output.decode('ascii')
        return output
