en = ['controlleredit[mon_enable]']

checks = ['controlleredit[mon_ping]','controlleredit[mon_lost]']

host_1 = ['controlleredit[mon_local_link_enable]','controlleredit[mon_local_vlan]','controlleredit[mon_local_ip]',
          'controlleredit[mon_local_delay_enable]','controlleredit[mon_local_delayms]']

host_2 = ['controlleredit[mon_hub_link_enable]','controlleredit[mon_hub_vlan]','controlleredit[mon_hub_ip]',
          'controlleredit[mon_hub_delay_enable]','controlleredit[mon_hub_delayms]']

tr_checks = ['controlleredit[mon_lanrx]','controlleredit[mon_lanrx_val]','controlleredit[mon_lantx]',
             'controlleredit[mon_lantx_val]']

switchover = ['controlleredit[mon_backup_enable]','controlleredit[mon_backup_ip]']

reboot = ['controlleredit[mon_reboot_enable]','controlleredit[mon_reboot_delay]']