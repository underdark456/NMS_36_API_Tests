from objects import ss_100x
import ss_100x_ip_protocols_api
from Menu import uhp_ip_protocols
import unittest

class TestingMethods(unittest.TestCase):

    def test_snmp(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.SNMP(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.snmp()])

    def test_dhcp(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.DHCP(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.dhcp()])

    def test_dns(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.DNS(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.dns()])

    def test_arp(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.ARP(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.arp()])

    def test_nat(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.NAT(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.nat()])

    def test_rip(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.RIP(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.rip()])

    def test_sntp(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.SNTP(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.sntp()])

    def test_tftp(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.TFTP(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.tftp()])

    def test_multicast(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.Multicast(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.multicast()])

    def test_acceleration(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.Acceleration_station(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.acceleration()])

    def test_screening(self):
        self.assertEqual([str(i) for i in uhp_ip_protocols.IP_screening(ss_100x.ss_100x_url()[0])],
                         [str(i) for i in ss_100x_ip_protocols_api.ip_screening()])


if __name__ == '__main__':
    unittest.main()

