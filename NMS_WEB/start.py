from Tabs import controller_ip_protocols_selenium
from Tabs import station_ip_protocols_selenium
import objects
import web_options
from selenium import webdriver

driver = webdriver.Chrome()
def sh_200x():
    web_options.nms_login(driver)
    controller_ip_protocols_selenium.tcp_accel(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.crypto(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.dhcp(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.dns(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.screening(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.snmp(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.tftp(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.multicast(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.arp(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.nat(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.nat_forwarding(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.sntp(objects.sh_200x_url()[1], driver)
    controller_ip_protocols_selenium.realtime(objects.sh_200x_url()[1], driver)


def ss_100x():
    web_options.nms_login(driver)
    station_ip_protocols_selenium.tcp_accel(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.crypto(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.dhcp(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.dns(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.screening(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.snmp(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.tftp(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.multicast(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.arp(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.nat(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.nat_forwarding(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.sntp(objects.ss_100x_url()[1], driver)
    station_ip_protocols_selenium.realtime(objects.ss_100x_url()[1], driver)

if __name__ == '__main__':
    ss_100x()
    try:
        driver.close()
    except Exception as e:
        print(e)
