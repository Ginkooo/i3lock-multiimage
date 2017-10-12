# i3lock-multiimage

Uses i3lock to display different image on each monitor

HOW TO USE
==========
```
cd ~
git clone https://github.com/ginkooo/i3lock-multiimage
cd i3lock-multiimage
python3 -m pip install --user -r requirements
```

change FOLDER in config.py to path of your script if you want to run it without doing next steps

Run

`sudo ./setup.py`

change FOLDER to new location

Then just lock the screen by typing

`lock`

I recommend binding key combination to `lock` in your shortcut manager

CHANGE IMAGES
=============
You can change displayed images by replacing pngs in images folder

SET WHICH IMAGE DISPLAYS ON WHICH MONITOR
=========================================
To achieve this, you must name images in a right alphabetical order, and match the order with `xrandr` output. For example:

You have three images and three monitors.

Images are:

`a.png`, `b.png`, `c.png`

Output from xrandr is like:

```
HDMI-0 connected
[...]
VGA-0 connected
[...]
HDMI-1 connected
[...]
```

So HDMI-0 is first, VGA-0 is second and HDMI-1 is third.

a.png would be on HDMI-0,

b.png would be on VGA-0,

c.png would be on HDMI-1

REQUIREMENTS
============
Python3+

i3lock (https://github.com/i3/i3lock)

Pillow library for Python3


WHAT WORKS
==========
- Display image on inline-positioned monitors (same height)
- Not inline aligned monitors, rotated monitors etc.


WHAT DOESN'T WORK
=================
- Image count different than monitor count

TODO
====
- Reuse already generated image
