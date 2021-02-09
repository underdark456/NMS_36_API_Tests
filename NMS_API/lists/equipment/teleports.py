tp = ['teleport[name]','teleport[latitude_deg]','teleport[latitude_min]','teleport[latitude_dir]',
                       'teleport[longitude_deg]','teleport[longitude_min]','teleport[longitude_dir]']

sat = ['satellite[name]','satellite[longitude_deg]','satellite[longitude_min]','satellite[longitude_dir]']

rf = ['rffeed[name]','rffeed[teleport_id]','rffeed[satellite_id]']

rx1 = ['rffeed[rx_lo]','rffeed[rx_power_enable]','rffeed[rx_power_voltage]','rffeed[rx_spinv_enable]'
    ,'rffeed[rx_freqadjust_scpc]']

rx2 = ['rffeed[rx_lo2]','rffeed[rx_power_enable]','rffeed[rx_power_voltage2]','rffeed[rx_tenmhz_enable2]',
       'rffeed[rx_spinv_enable2]','rffeed[rx_freqadjust_tdma]']

transmit = ['rffeed[tx_lo]','rffeed[tx_power_enable]','rffeed[tx_tenmhz_enable]','rffeed[tx_spinv_enable]',
            'rffeed[tx_freqadjust]']

carrier = ['rffeed[ca_scpc_mode]','rffeed[ca_tdma_mode]']

permisions = ['rffeed[allow_local_config]']

modem = ['modem[name]','modem[ip_addr]','modem[password]','modem[timeout]','modem[serial_num]','modem[rack_number]',
         'modem[rack]']

m_tp = ['modem[teleport_id]','modem[rffeed_id]']

hw_plat = ['modem[platform]']

tx_cor = ['modem[tx_level_correction]']

rf_int = ['modem[power_10mhz]']

