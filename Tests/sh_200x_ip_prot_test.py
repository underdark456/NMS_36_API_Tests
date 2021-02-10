from objects import sh_200x
import sh_200x_ip_protocols_api
import sh_200x_rf
from Menu import uhp_ip_protocols
from Profiles import star_200x
import unittest

print(sh_200x_rf.tdm_tx())
print(star_200x.tdm_tx())


# class test_ip_prots(unittest.TestCase):
#
#     def test_snmp(self):
#         self.assertEqual(uhp_ip_protocols.SNMP(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.snmp())
#
#     def test_dhcp(self):
#         self.assertEqual(uhp_ip_protocols.DHCP(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.dhcp())
#
#     def test_dns(self):
#         self.assertEqual(uhp_ip_protocols.DNS(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.dns())
#
#     def test_nat(self):
#         self.assertEqual(uhp_ip_protocols.NAT(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.nat())
#
#     def test_rip(self):
#         self.assertEqual(uhp_ip_protocols.RIP(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.rip())
#
#     def test_sntp(self):
#         self.assertEqual(uhp_ip_protocols.SNTP(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.sntp())
#
#     def test_tftp(self):
#         self.assertEqual(uhp_ip_protocols.TFTP(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.tftp())
#
#     def test_multicast(self):
#         self.assertEqual(uhp_ip_protocols.Multicast(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.multicast())
#
#     def test_acceleration(self):
#         self.assertEqual(uhp_ip_protocols.Acceleration_controller(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.acceleration())
#
#     def test_arp(self):
#         self.assertEqual(uhp_ip_protocols.IP_screening(sh_200x.sh_200x_url()[0]), sh_200x_ip_protocols_api.ip_screening())
#
#
# class test_profile(unittest.TestCase):
#     def test_mod(self):
#         self.assertEqual(sh_200x_rf.mod(), sh_200x_rf.mod())
#     def test_tdm_tx(self):
#         self.assertEqual(sh_200x_rf.tdm_tx(), sh_200x_rf.tdm_tx())
#
# if __name__ == '__main__':
#     unittest.main()