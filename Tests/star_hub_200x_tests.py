import star_hub_200x_ip_protocols_api
import star_hub_200x_ip_protocols
import star_hub_200x_modulator

import unittest


class TestingMethods(unittest.TestCase):
    def test_modulator(self):
        self.assertEqual(star_hub_200x_modulator.star_hub_txlvl(), star_hub_200x_modulator.star_hub_txlvl())

    def test_snmp(self):
        self.assertEqual(star_hub_200x_ip_protocols.SNMP(), star_hub_200x_ip_protocols_api.snmp())

    def test_dhcp(self):
        self.assertEqual(star_hub_200x_ip_protocols.DHCP(),star_hub_200x_ip_protocols_api.dhcp())


if __name__ == '__main__':
    unittest.main()
