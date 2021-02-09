from objects import sh_200x
import sh_200x_ip_protocols_api
from Menu import uhp_ip_protocols
import unittest

class TestingMethods(unittest.TestCase):

    def test_snmp(self):
        self.assertEqual(uhp_ip_protocols.SNMP(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.snmp())

    def test_dhcp(self):
        self.assertEqual(uhp_ip_protocols.DHCP(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.dhcp())

    def test_dns(self):
        self.assertEqual(uhp_ip_protocols.DNS(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.dns())

    def test_nat(self):
        self.assertEqual(uhp_ip_protocols.NAT(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.nat())

    def test_rip(self):
        self.assertEqual(uhp_ip_protocols.RIP(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.rip())

    def test_sntp(self):
        self.assertEqual(uhp_ip_protocols.SNTP(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.sntp())

    def test_tftp(self):
        self.assertEqual(uhp_ip_protocols.TFTP(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.tftp())

    def test_multicast(self):
        self.assertEqual(uhp_ip_protocols.Multicast(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.multicast())

    def test_acceleration(self):
        self.assertEqual(uhp_ip_protocols.Acceleration_controller(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.acceleration())

    def test_arp(self):
        self.assertEqual(uhp_ip_protocols.IP_screening(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.ip_screening())
if __name__ == '__main__':
    unittest.main()

