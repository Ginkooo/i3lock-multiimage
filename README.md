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

Run

`sudo ./setup.py`

Then just lock the screen by typing

`lock`

I recommend binding key combination to `lock` in your shortcut manager

CHANGE IMAGES
=============
You can change displayed images by replacing pngs in images folder

REQUIREMENTS
============
Python3+

i3lock (https://github.com/i3/i3lock)

Pillow library for Python3


WHAT WORKS
==========
- Display image on inline-positioned monitors (same height)


WHAT DOESN'T WORK
=================
- Not inline aligned monitors, rotated monitors etc.
- Image count different than monitor count

TODO
====
- Reuse already generated image
