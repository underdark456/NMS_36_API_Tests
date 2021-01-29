import web_options
import time

def tcp_accel(url,driver):
    driver.get(url)
    web_options.get_element_id(driver, 'remote[accel_enable]').click()
    web_options.get_element_id(driver, 'remote[accel_svlan_from]').clear()
    web_options.get_element_id(driver, 'remote[accel_svlan_from]').send_keys('64000')
    web_options.get_element_id(driver, 'remote[accel_svlan_to]').clear()
    web_options.get_element_id(driver, 'remote[accel_svlan_to]').send_keys('64000')
    web_options.get_element_id(driver, 'remote[accel_mss]').clear()
    web_options.get_element_id(driver, 'remote[accel_mss]').send_keys('1500')
    web_options.get_element_id(driver, 'remote[accel_max_tcp_window]').clear()
    web_options.get_element_id(driver, 'remote[accel_max_tcp_window]').send_keys('65535')
    web_options.get_element_id(driver, 'remote[accel_sessions]').clear()
    web_options.get_element_id(driver, 'remote[accel_sessions]').send_keys('14000')
    web_options.get_element_id(driver, 'remote[accel_buffers]').clear()
    web_options.get_element_id(driver, 'remote[accel_buffers]').send_keys('32')
    web_options.get_element_id(driver, 'remote[accel_max_queue]').clear()
    web_options.get_element_id(driver, 'remote[accel_max_queue]').send_keys('5000')
    web_options.get_element_id(driver, 'remote[accel_max_mod_queue]').clear()
    web_options.get_element_id(driver, 'remote[accel_max_mod_queue]').send_keys('5000')
    web_options.get_element_id(driver, 'remote[accel_retransmit_timeout]').clear()
    web_options.get_element_id(driver, 'remote[accel_retransmit_timeout]').send_keys('255')
    web_options.get_element_id(driver, 'remote[accel_retransmit_tries]').clear()
    web_options.get_element_id(driver, 'remote[accel_retransmit_tries]').send_keys('255')
    web_options.get_element_id(driver, 'remote[accel_inactivity_timeout]').clear()
    web_options.get_element_id(driver, 'remote[accel_inactivity_timeout]').send_keys('255')
    web_options.get_element_id(driver, 'remote[accel_ack_period]').clear()
    web_options.get_element_id(driver, 'remote[accel_ack_period]').send_keys('500')
    # driver.find_element_by_xpath('/html/body/div[7]/div[2]/div[2]/div[3]/form/button').click()


def crypto(url,driver):
    """Добавить проверку AES v3.4/3.5 для UHP 3.5"""
    driver.get(url)
    web_options.get_element_id(driver, 'remote[crypto_flags]').click()
    web_options.get_element_id(driver, 'remote[crypto_key]').clear()
    web_options.get_element_id(driver, 'remote[crypto_key]').send_keys('256')


def dhcp(url,driver):
    driver.get(url)
    web_options.get_element_xpath(driver, '//*[@id="remote[dhcp_enable]"]/option[2]').click()
    web_options.get_element_id(driver, 'remote[dhcp_vlan]').clear()
    web_options.get_element_id(driver, 'remote[dhcp_vlan]').send_keys('4095')
    web_options.get_element_id(driver, 'remote[dhcp_ip_start]').clear()
    web_options.get_element_id(driver, 'remote[dhcp_ip_start]').send_keys('1.1.1.1')
    web_options.get_element_id(driver, 'remote[dhcp_ip_end]').clear()
    web_options.get_element_id(driver, 'remote[dhcp_ip_end]').send_keys('1.1.1.255')
    web_options.get_element_id(driver, 'remote[dhcp_mask]').clear()
    web_options.get_element_id(driver, 'remote[dhcp_mask]').send_keys('24')
    web_options.get_element_id(driver, 'remote[dhcp_gw]').clear()
    web_options.get_element_id(driver, 'remote[dhcp_gw]').send_keys('3.3.3.3')
    web_options.get_element_id(driver, 'remote[dhcp_dns]').clear()
    web_options.get_element_id(driver, 'remote[dhcp_dns]').send_keys('4.4.4.4')
    web_options.get_element_id(driver, 'remote[dhcp_lease]').clear()
    web_options.get_element_id(driver, 'remote[dhcp_lease]').send_keys('86400')


def dns(url,driver):
    driver.get(url)
    driver.execute_script("arguments[0].scrollIntoView()", web_options.get_element_id(driver, 'remote['
                                                                                              'dns_enable]'))
    web_options.get_element_id(driver, 'remote[dns_enable]').click()
    web_options.get_element_id(driver, 'remote[dns_clear_timeout]').clear()
    web_options.get_element_id(driver, 'remote[dns_clear_timeout]').send_keys('60')


def screening(url,driver):
    driver.get(url)
    web_options.get_element_xpath(driver, '//*[@id="remote[ipscreen_enable]"]/option[2]').click()


def snmp(url,driver):
    driver.get(url)
    web_options.get_element_id(driver, 'remote[snmp_ip1]').clear()
    web_options.get_element_id(driver, 'remote[snmp_ip1]').send_keys('255.255.255.255')
    web_options.get_element_id(driver, 'remote[snmp_ip2]').clear()
    web_options.get_element_id(driver, 'remote[snmp_ip2]').send_keys('255.255.255.255')
    web_options.get_element_id(driver, 'remote[snmp_read]').clear()
    web_options.get_element_id(driver, 'remote[snmp_read]').send_keys('0123456789')
    web_options.get_element_id(driver, 'remote[snmp_write]').clear()
    web_options.get_element_id(driver, 'remote[snmp_write]').send_keys('9876543210')


def tftp(url,driver):
    driver.get(url)
    web_options.get_element_id(driver, 'remote[tftp_ip]').clear()
    web_options.get_element_id(driver, 'remote[tftp_ip]').send_keys('255.255.255.255')
    web_options.get_element_id(driver, 'remote[tftp_vlan]').clear()
    web_options.get_element_id(driver, 'remote[tftp_vlan]').send_keys('4095')


def multicast(url,driver):
    driver.get(url)
    web_options.get_element_xpath(driver, '//*[@id="remote[multicast_mode]"]/option[3]').click()
    web_options.get_element_id(driver, 'remote[multicast_timeout]').clear()
    web_options.get_element_id(driver, 'remote[multicast_timeout]').send_keys('30')


def arp(url,driver):
    driver.get(url)
    web_options.get_element_id(driver, 'remote[arp_timeout]').clear()
    web_options.get_element_id(driver, 'remote[arp_timeout]').send_keys('30')
    web_options.get_element_id(driver, 'remote[arp_proxy_enable]').click()


def nat(url,driver):
    driver.get(url)
    driver.execute_script("arguments[0].scrollIntoView()", web_options.get_element_id(driver, 'remote[nat_enable]'))
    web_options.get_element_id(driver, 'remote[nat_enable]').click()
    web_options.get_element_id(driver, 'remote[nat_external_ip]').clear()
    web_options.get_element_id(driver, 'remote[nat_external_ip]').send_keys('255.255.255.255')
    web_options.get_element_id(driver, 'remote[arp_timeout]').clear()
    web_options.get_element_id(driver, 'remote[arp_timeout]').send_keys('255.255.255.255')
    web_options.get_element_id(driver, 'remote[arp_timeout]').clear()
    web_options.get_element_id(driver, 'remote[arp_timeout]').send_keys('32')


def nat_forwarding(url,driver):
    '''В АПИ нереализовано'''
    driver.get(url)
    driver.execute_script("arguments[0].scrollIntoView()", web_options.get_element_id(driver, 'port-mapping-add'))
    web_options.get_element_id(driver, 'port-mapping-add').click()
    '''Костыль. Возникал эксепшн element not interactable.'''
    while not web_options.get_element_id(driver, 'portmapping[external_port]'): time.sleep()
    web_options.get_element_id(driver, 'portmapping[external_port]').clear()
    web_options.get_element_id(driver, 'portmapping[external_port]').send_keys('5000')
    web_options.get_element_id(driver, 'portmapping[internal_ip]').clear()
    web_options.get_element_id(driver, 'portmapping[internal_ip]').send_keys('255.255.255.254')
    web_options.get_element_id(driver, 'portmapping[internal_port]').clear()
    web_options.get_element_id(driver, 'portmapping[internal_port]').send_keys('10000')
    web_options.get_element_id(driver, 'port-mapping-button-save').click()


def rip(url,driver):
    driver.get(url)
    driver.execute_script("arguments[0].scrollIntoView()", web_options.get_element_id(driver, 'remote['
                                                                                              'rip_enable]'))
    web_options.get_element_id(driver, 'remote[rip_enable]').click()
    web_options.get_element_id(driver, 'remote[rip_gateway_ip]').clear()
    web_options.get_element_id(driver, 'remote[rip_gateway_ip]').send_keys('255.255.255.255')
    web_options.get_element_id(driver, 'remote[rip_omit_down_stations]').click()
    web_options.get_element_id(driver, 'remote[rip_couple_to_sm_alarms]').click()
    web_options.get_element_id(driver, 'remote[rip_routes_cost]').clear()
    web_options.get_element_id(driver, 'remote[rip_routes_cost]').send_keys('16')


def sntp(url,driver):
    driver.get(url)
    web_options.get_element_xpath(driver, '//*[@id="remote[sntp_mode]"]/option[4]').click()
    web_options.get_element_id(driver, 'remote[sntp_ip]').clear()
    web_options.get_element_id(driver, 'remote[sntp_ip]').send_keys('255.255.255.255')
    web_options.get_element_id(driver, 'remote[sntp_vlan]').clear()
    web_options.get_element_id(driver, 'remote[sntp_vlan]').send_keys('4095')


def realtime(url,driver):
    driver.get(url)
    web_options.get_element_id(driver, 'remote[realtime_bw_codec]').clear()
    web_options.get_element_id(driver, 'remote[realtime_bw_codec]').send_keys('65000')
    web_options.get_element_id(driver, 'remote[realtime_bw_threshold]').clear()
    web_options.get_element_id(driver, 'remote[realtime_bw_threshold]').send_keys('200')
    web_options.get_element_id(driver, 'remote[realtime_bw_timeout]').clear()
    web_options.get_element_id(driver, 'remote[realtime_bw_timeout]').send_keys('200')


# if __name__ == '__main__':
#     web_options.nms_login(driver)
#     tcp_accel()

    # try:
    #     driver.close()
    # except Exception as e:
    #     print(e)
