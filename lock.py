#!/usr/bin/env python3

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

import config
import tempfile
import os
import subprocess
from src.xrandr.xrandr import Xrandr
from src.images.reader import Reader
from src.handles.linker import Linker
from src.handles.resizer import Resizer
from src.handles.displayer import Displayer


def main():
    screens = Xrandr.get_monitors()
    images = Reader.get_images(config.IMAGE_FOLDER)
    images = list(images)
    screens = list(screens)
    linker = Linker(images=images, screens=screens)
    pairs = linker.get_pairs()
    pairs = list(pairs)
    pairs = Resizer.resize_pairs(pairs)
    displayer = Displayer(pairs=pairs)
    final_image = displayer.make_background()
    final_image.save('/tmp/dupa.png')
    with tempfile.TemporaryDirectory() as tmpdir:
        path = os.path.join(tmpdir, 'image.png')
        final_image.save(path)
        subprocess.check_output('i3lock -i %s' % path, shell=True)


if __name__ == '__main__':
    main()
