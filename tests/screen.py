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
