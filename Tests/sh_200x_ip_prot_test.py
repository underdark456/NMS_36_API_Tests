from objects import sh_200x_url
from sh_200x import sh_200x_ip_protocols_api, sh_200x_rf
from Menu import uhp_ip_protocols
from Profiles import star_200x
import unittest


class test_ip_prots(unittest.TestCase):

    def test_snmp(self):
        self.assertEqual(uhp_ip_protocols.SNMP(sh_200x_url()[0]), sh_200x_ip_protocols_api.snmp())

    def test_dhcp(self):
        self.assertEqual(uhp_ip_protocols.DHCP(sh_200x_url()[0]), sh_200x_ip_protocols_api.dhcp())

    def test_dns(self):
        self.assertEqual(uhp_ip_protocols.DNS(sh_200x_url()[0]), sh_200x_ip_protocols_api.dns())

    def test_nat(self):
        self.assertEqual(uhp_ip_protocols.NAT(sh_200x_url()[0]), sh_200x_ip_protocols_api.nat())

    def test_rip(self):
        self.assertEqual(uhp_ip_protocols.RIP(sh_200x_url()[0]), sh_200x_ip_protocols_api.rip())

    def test_sntp(self):
        self.assertEqual(uhp_ip_protocols.SNTP(sh_200x_url()[0]), sh_200x_ip_protocols_api.sntp())

    def test_tftp(self):
        self.assertEqual(uhp_ip_protocols.TFTP(sh_200x_url()[0]), sh_200x_ip_protocols_api.tftp())

    def test_multicast(self):
        self.assertEqual(uhp_ip_protocols.Multicast(sh_200x_url()[0]), sh_200x_ip_protocols_api.multicast())

    def test_acceleration(self):
        self.assertEqual(uhp_ip_protocols.Acceleration_controller(sh_200x_url()[0]), sh_200x_ip_protocols_api.acceleration())

    def test_arp(self):
        self.assertEqual(uhp_ip_protocols.IP_screening(sh_200x_url()[0]), sh_200x_ip_protocols_api.ip_screening())


class test_profile(unittest.TestCase):
    def test_tdm_rx(self):
        self.assertEqual(sh_200x_rf.tdm_rx(), star_200x.tdm_rx())

    def test_tdm_tx(self):
        self.assertEqual(sh_200x_rf.tdm_tx(), star_200x.tdm_tx())

    def test_mod(self):
        self.assertEqual(sh_200x_rf.mod(), star_200x.mod())

    def test_time(self):
        self.assertEqual(sh_200x_rf.tdma_time(), star_200x.timing())

    def test_tlc(self):
        self.assertEqual(sh_200x_rf.tlc(), star_200x.tlc())

    def test_tdm_acm(self):
        self.assertEqual(sh_200x_rf.acm(), star_200x.tdm_acm())

    def test_tdma_rf(self):
        lst = list(sh_200x_rf.tdma_rf())
        lst[1] = sh_200x_rf.tdma_modcod
        self.assertEqual(tuple(lst), star_200x.tdma_rf())

    def test_tdma_prot(self):
        self.assertEqual(sh_200x_rf.tdma_prot(), star_200x.tdma_prot())

    def test_tdma_bw(self):
        self.assertEqual(sh_200x_rf.tdma_bw(), star_200x.tdma_bw())

    def test_tdma_acm(self):
        lst = list(sh_200x_rf.tdma_acm()[2:14])
        for i, v in enumerate(lst):
            if v!= 0:
                lst[i] = '1'
        cn = sh_200x_rf.tdma_acm()[14]
        cn = cn,
        self.assertEqual(sh_200x_rf.tdma_acm()[0:2] + tuple(lst) + cn, star_200x.tdma_acm())

    def roaming(self):
        self.assertEqual(sh_200x_rf.roaming(), star_200x.roaming())

if __name__ == '__main__':
    unittest.main()

