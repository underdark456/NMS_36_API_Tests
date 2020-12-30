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

    def test_dns(self):
        self.assertEqual(star_hub_200x_ip_protocols.DNS(),star_hub_200x_ip_protocols_api.dns())

    def test_nat(self):
        self.assertEqual(star_hub_200x_ip_protocols.NAT(),star_hub_200x_ip_protocols_api.nat())

    def test_rip(self):
        self.assertEqual(star_hub_200x_ip_protocols.RIP(),star_hub_200x_ip_protocols_api.rip())

    def test_sntp(self):
        self.assertEqual(star_hub_200x_ip_protocols.SNTP(),star_hub_200x_ip_protocols_api.sntp())

    def test_tftp(self):
        self.assertEqual(star_hub_200x_ip_protocols.TFTP(),star_hub_200x_ip_protocols_api.tftp())

    def test_multicast(self):
        self.assertEqual(star_hub_200x_ip_protocols.Multicast(),star_hub_200x_ip_protocols_api.multicast())

    def test_acceleration(self):
        self.assertEqual(star_hub_200x_ip_protocols.Acceleration(),star_hub_200x_ip_protocols_api.acceleration())

    def test_arp(self):
        self.assertEqual(star_hub_200x_ip_protocols.IP_screening(),star_hub_200x_ip_protocols_api.ip_screening())
if __name__ == '__main__':
    unittest.main()
