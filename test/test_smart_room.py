import unittest
import mock.GPIO as GPIO
from unittest.mock import patch, PropertyMock
from unittest.mock import Mock

from mock.adafruit_bmp280 import Adafruit_BMP280_I2C
from src.smart_room import SmartRoom
from mock.senseair_s8 import SenseairS8


class TestSmartRoom(unittest.TestCase):

    @patch.object(GPIO, "input")
    def test_check_room_occupancy(self, mock_input):
        mock_input.return_value = 22
        smart_room = SmartRoom()
        self.assertTrue(smart_room.check_room_occupancy())

    @patch.object(SmartRoom, "check_enough_light")
    def test_check_enough_light(self, mock_check_enough_light):
        smart_room = SmartRoom()
        smart_room.check_enough_light()
        self.assertTrue(mock_check_enough_light)

    @patch.object(SmartRoom, "manage_light_level")
    def test_manage_light_level(self, mock_manage_light_level):
        smart_room = SmartRoom()
        smart_room.manage_light_level()
        self.assertTrue(mock_manage_light_level)

    @patch.object(SmartRoom, "manage_window", new_callable=PropertyMock)
    def test_manage_window(self, mock_manage_window):
        smart_room = SmartRoom()
        smart_room.manage_window()
        self.assertTrue(mock_manage_window)




