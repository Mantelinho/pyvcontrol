import unittest
from unittest.mock import patch
from pyvcontrol.viTools import vimonitor
from viControlMock import viControlMock


command_set = {
    "Warmwassertemperatur": {
        "address": "010d",
        "length": 2,
        "unit": "IS10",
        "description": "Warmwasser: Warmwassertemperatur oben (0..95)"
    },
    "VorlauftempSek": {
        "address": "0105",
        "length": 2,
        "unit": "IS10",
        "description": "Heizkreis HK1: Vorlauftemperatur Sekundaer 1 (0..95)"
    }
}


class testviTools(unittest.TestCase):

    @unittest.skip("Disabled due to dependency on TERM")
    @patch('pyvcontrol.viTools.viControl', return_value=viControlMock())
    def test_monitor(self, mock1):
        vimonitor(['Warmwassertemperatur', 'VorlauftempSek'])
        self.assertEqual(True, True)  # add assertion here

    @unittest.skip("Disabled due to dependency on TERM")
    @patch('pyvcontrol.viTools.viControl', return_value=viControlMock())
    def test_monitor_unknown_command(self, mock1):
        vimonitor(['Warmwassertemperatur', 'Vorlauftemperatur'])
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()
